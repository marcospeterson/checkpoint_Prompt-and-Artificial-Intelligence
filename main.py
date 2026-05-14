import json

from dotenv import load_dotenv

from src.tasks import tarefas

from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)

from src.llm_client import LLMClient

from src.evaluator import (
    medir_acuracia,
    testar_temperatura
)

from src.report import (
    gerar_tabela,
    grafico_acuracia,
    grafico_custo,
    grafico_temperatura,
    recomendar
)


# Carrega variáveis de ambiente
load_dotenv()

def main():

    print("=" * 60)
    print("PROMPT TOOLKIT - FIAP")
    print("=" * 60)

    # Cliente do Ollama
    client = LLMClient()

    # Carrega inputs
    with open(
        "data/inputs.json",
        "r",
        encoding="utf-8"
    ) as arquivo:

        inputs = json.load(arquivo)

    resultados = []

    for tarefa in tarefas:

        nome_tarefa = tarefa["nome"]

        print(f"\nExecutando tarefa: {nome_tarefa}")

        dados_tarefa = inputs[nome_tarefa]

        for item in dados_tarefa:

            input_texto = item["input"]

            esperado = item["esperado"]

            tecnicas = {

                "zero_shot":
                    zero_shot(
                        tarefa,
                        input_texto
                    ),

                "few_shot":
                    few_shot(
                        tarefa,
                        input_texto,
                        tarefa["exemplos_fewshot"]
                    ),

                "chain_of_thought":
                    chain_of_thought(
                        tarefa,
                        input_texto,
                        tarefa["passos_cot"]
                    )
            }
            # Role Prompting
            system_role, prompt_role = role_prompting(
                tarefa,
                input_texto,
                tarefa["persona"]
            )

            tecnicas["role_prompting"] = (
                system_role,
                prompt_role
            )

            for nome_tecnica, prompt in tecnicas.items():
                try:

                    print(
                        f"  Técnica: {nome_tecnica}"
                    )

                    if nome_tecnica == "role_prompting":

                        system = prompt[0]
                        user_prompt = prompt[1]

                    else:

                        system = ""
                        user_prompt = prompt

                    resultado = client.chat(
                        prompt=user_prompt,
                        system=system,
                        temp=0.5
                    )

                    acuracia = medir_acuracia(
                        resultado["resposta"],
                        esperado
                    )

                    tokens_totais = (
                            resultado["tokens_prompt"] +
                            resultado["tokens_resposta"]
                    )

                    resultados.append({

                        "tarefa": nome_tarefa,

                        "tecnica": nome_tecnica,

                        "input": input_texto,

                        "esperado": esperado,

                        "resposta":
                            resultado["resposta"],

                        "acuracia": acuracia,

                        "tokens_prompt":
                            resultado["tokens_prompt"],

                        "tokens_resposta":
                            resultado["tokens_resposta"],

                        "tokens_totais":
                            tokens_totais,

                        "tempo_ms":
                            resultado["tempo_ms"]
                    })

                except Exception as erro:

                    print(
                        f"Erro na técnica "
                        f"{nome_tecnica}: {erro}"
                    )

                # Geração de relatórios
            df = gerar_tabela(resultados)

            grafico_acuracia(df)

            grafico_custo(df)

            recomendacao = recomendar(df)

            # Teste de temperatura
            exemplo_prompt = (
                "Classifique o sentimento: "
                "Produto excelente!"
            )

            resultados_temp = testar_temperatura(
                client,
                exemplo_prompt
            )

            grafico_temperatura(resultados_temp)

            print("\nProcesso finalizado!")
            print(recomendacao)

if __name__ == "__main__":
    main()
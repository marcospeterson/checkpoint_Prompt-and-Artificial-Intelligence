import json

from src.prompt_builder import (
    montar_prompt,
    adicionar_exemplos,
    adicionar_cot
)
def zero_shot(tarefa, input_texto):
    """
    Técnica Zero-Shot.
    Não utiliza exemplos.
    """

    prompt = montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=f"Tarefa do tipo {tarefa['tipo']}",
        input_dados=input_texto,
        formato_output=tarefa["formato_output"]
    )

    return prompt

def few_shot(tarefa, input_texto, exemplos):
    """
    Técnica Few-Shot.
    Utiliza exemplos de entrada e saída.
    """

    prompt = montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=f"Tarefa do tipo {tarefa['tipo']}",
        input_dados=input_texto,
        formato_output=tarefa["formato_output"]
    )

    prompt = adicionar_exemplos(
        prompt,
        exemplos
    )

    return prompt

def chain_of_thought(tarefa, input_texto, passos):
    """
    Técnica Chain of Thought (CoT).
    Adiciona raciocínio passo a passo.
    """

    prompt = montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=f"Tarefa do tipo {tarefa['tipo']}",
        input_dados=input_texto,
        formato_output=tarefa["formato_output"]
    )

    prompt = adicionar_cot(
        prompt,
        passos
    )

    return prompt

def role_prompting(tarefa, input_texto, persona):
    """
    Técnica Role Prompting.
    Utiliza uma persona via system prompt.
    """

    with open(
        "prompts/system_prompts.json",
        "r",
        encoding="utf-8"
    ) as arquivo:

        personas = json.load(arquivo)

    system_prompt = personas[persona]

    user_prompt = montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=f"Tarefa do tipo {tarefa['tipo']}",
        input_dados=input_texto,
        formato_output=tarefa["formato_output"]
    )

    return system_prompt, user_prompt
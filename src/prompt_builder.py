def validar_campo(valor, nome_campo):
    """
    Valida se um campo obrigatório foi preenchido.
    """

    if not valor or not str(valor).strip():
        raise ValueError(
            f"O campo '{nome_campo}' não pode estar vazio."
        )

def montar_prompt(
    instrucao,
    contexto,
    input_dados,
    formato_output
):
    """
    Monta a estrutura principal do prompt.
    """

    # Validações
    validar_campo(instrucao, "instrucao")
    validar_campo(contexto, "contexto")
    validar_campo(input_dados, "input_dados")
    validar_campo(formato_output, "formato_output")

    prompt = f"""
### INSTRUÇÃO:
{instrucao}

### CONTEXTO:
{contexto}

### DADOS:
{input_dados}

### FORMATO DA RESPOSTA:
{formato_output}
"""

    return prompt.strip()

def adicionar_exemplos(prompt, exemplos):
    """
    Adiciona exemplos ao prompt para Few-Shot Prompting.
    """

    if not exemplos:
        return prompt

    bloco_exemplos = "\n\n### EXEMPLOS:\n"

    for exemplo in exemplos:

        bloco_exemplos += (
            f'\nInput: "{exemplo["input"]}"\n'
            f'Output: "{exemplo["output"]}"\n'
        )

    return prompt + bloco_exemplos


def adicionar_cot(prompt, passos):
    """
    Adiciona raciocínio passo a passo ao prompt.
    """

    if not passos:
        return prompt

    bloco_cot = "\n\n### RACIOCINE PASSO A PASSO:\n"

    for indice, passo in enumerate(passos, start=1):

        bloco_cot += f"{indice}. {passo}\n"

    return prompt + bloco_cot

if __name__ == "__main__":

    prompt = montar_prompt(
        instrucao="Classifique o sentimento do texto.",
        contexto="Avaliações de clientes de e-commerce.",
        input_dados="Produto chegou quebrado e atrasado.",
        formato_output="Responda apenas POSITIVO, NEGATIVO ou MISTO."
    )

    exemplos = [
        {
            "input": "Produto excelente!",
            "output": "POSITIVO"
        },
        {
            "input": "Muito ruim.",
            "output": "NEGATIVO"
        }
    ]

    passos = [
        "Identifique pontos positivos",
        "Identifique pontos negativos",
        "Defina a classificação final"
    ]

    prompt = adicionar_exemplos(prompt, exemplos)

    prompt = adicionar_cot(prompt, passos)

    print(prompt)

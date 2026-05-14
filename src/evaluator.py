import tiktoken

from collections import Counter

def contar_tokens(texto):
    """
    Conta quantidade aproximada de tokens.
    """

    encoding = tiktoken.get_encoding("cl100k_base")

    tokens = encoding.encode(texto)

    return len(tokens)

def medir_acuracia(resposta, esperado):
    """
    Mede se a resposta está correta.
    """

    resposta = str(resposta).strip().lower()

    esperado = str(esperado).strip().lower()

    return resposta == esperado

def medir_consistencia(respostas):
    """
    Mede consistência das respostas.
    """

    if not respostas:
        return 0

    contador = Counter(respostas)

    resposta_mais_comum = contador.most_common(1)[0][1]

    consistencia = (
        resposta_mais_comum / len(respostas)
    ) * 100

    return round(consistencia, 2)


def testar_temperatura(
    client,
    prompt,
    system="",
    temps=[0.1, 0.5, 1.0]
):
    """
    Testa diferentes temperaturas do modelo.
    """

    resultados = []

    for temp in temps:

        respostas = []

        for _ in range(3):

            resultado = client.chat(
                prompt=prompt,
                system=system,
                temp=temp
            )

            respostas.append(
                resultado["resposta"]
            )

        consistencia = medir_consistencia(
            respostas
        )

        resultados.append({
            "temperatura": temp,
            "consistencia": consistencia,
            "respostas": respostas
        })

    return resultados


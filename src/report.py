import os

import pandas as pd
import matplotlib.pyplot as plt

def gerar_tabela(resultados):
    """
    Gera tabela CSV com os resultados.
    """

    df = pd.DataFrame(resultados)

    os.makedirs("output", exist_ok=True)

    caminho = "output/resultados.csv"

    df.to_csv(
        caminho,
        index=False,
        encoding="utf-8-sig"
    )

    print("\nTabela CSV gerada com sucesso!")

    return df

def grafico_acuracia(df):
    """
    Gera gráfico de acurácia por técnica.
    """

    os.makedirs(
        "output/graficos",
        exist_ok=True
    )

    acuracia = (
        df.groupby("tecnica")["acuracia"]
        .mean() * 100
    )

    plt.figure(figsize=(8, 5))

    acuracia.plot(kind="bar")

    plt.title("Acurácia Média por Técnica")

    plt.ylabel("Acurácia (%)")

    plt.xlabel("Técnica")

    plt.tight_layout()

    plt.savefig(
        "output/graficos/grafico_acuracia.png"
    )

    plt.close()

    print("Gráfico de acurácia gerado!")

def grafico_custo(df):
    """
    Gera gráfico de custo médio por técnica.
    """

    custo = (
        df.groupby("tecnica")["tokens_totais"]
        .mean()
    )

    plt.figure(figsize=(8, 5))

    custo.plot(kind="bar")

    plt.title("Custo Médio de Tokens")

    plt.ylabel("Tokens")

    plt.xlabel("Técnica")

    plt.tight_layout()

    plt.savefig(
        "output/graficos/grafico_custo.png"
    )

    plt.close()

    print("Gráfico de custo gerado!")

def grafico_temperatura(resultados_temp):
    """
    Gera gráfico de consistência por temperatura.
    """

    temperaturas = [
        item["temperatura"]
        for item in resultados_temp
    ]

    consistencias = [
        item["consistencia"]
        for item in resultados_temp
    ]

    plt.figure(figsize=(8, 5))

    plt.plot(
        temperaturas,
        consistencias,
        marker="o"
    )

    plt.title(
        "Consistência por Temperatura"
    )

    plt.xlabel("Temperatura")

    plt.ylabel("Consistência (%)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "output/graficos/grafico_temperatura.png"
    )

    plt.close()

    print("Gráfico de temperatura gerado!")


def recomendar(df):
    """
    Recomenda a melhor técnica.
    """

    ranking = (
        df.groupby("tecnica")["acuracia"]
        .mean()
        .sort_values(ascending=False)
    )

    melhor = ranking.index[0]

    acuracia = round(
        ranking.iloc[0] * 100,
        2
    )

    recomendacao = (
        f"A melhor técnica foi "
        f"'{melhor}' com "
        f"{acuracia}% de acurácia."
    )

    print("\nRECOMENDAÇÃO FINAL:")
    print(recomendacao)

    return recomendacao


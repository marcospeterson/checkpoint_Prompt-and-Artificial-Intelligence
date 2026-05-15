from pathlib import Path
import os
import time
import tiktoken

from retry import retry
from dotenv import load_dotenv
from ollama import Client


# Carrega variáveis do .env
BASE_DIR = Path(__file__).resolve().parent.parent

print("BASE_DIR:", BASE_DIR)

print("ENV EXISTS:", (BASE_DIR / ".env").exists())

print("ENV PATH:", BASE_DIR / ".env")
load_dotenv(BASE_DIR / ".env")


class LLMClient:

    def __init__(
            self,
            model="gpt-oss:120b",
            timeout=120
    ):

        self.model = model

        self.timeout = timeout

        self.client = Client(

            host="https://ollama.com",

            headers={
                "Authorization":
                    "Bearer " +
                    os.getenv("OLLAMA_API_KEY")
            }
        )

    def contar_tokens(self, texto):
        """
        Conta quantidade aproximada de tokens.
        """

        encoding = tiktoken.get_encoding(
            "cl100k_base"
        )

        tokens = encoding.encode(texto)

        return len(tokens)

    @retry(tries=3, delay=2)
    def chat(
        self,
        prompt,
        system="",
        temp=0.5,
        max_tokens=500
    ):
        """
        Envia prompt para o modelo.
        """

        inicio = time.time()

        try:

            mensagens = []

            if system:

                mensagens.append({
                    "role": "system",
                    "content": system
                })

            mensagens.append({
                "role": "user",
                "content": prompt
            })

            response = self.client.chat(

                model=self.model,

                messages=mensagens,

                options={
                    "temperature": temp,
                    "num_predict": max_tokens
                },

                stream=False
            )

            resposta_modelo = (
                response["message"]["content"]
            )

            fim = time.time()

            tempo_ms = round(
                (fim - inicio) * 1000,
                2
            )

            return {

                "resposta": resposta_modelo,

                "tokens_prompt":
                    self.contar_tokens(prompt),

                "tokens_resposta":
                    self.contar_tokens(
                        resposta_modelo
                    ),

                "tempo_ms": tempo_ms
            }

        except Exception as erro:

            raise Exception(
                f"Erro ao acessar API: {erro}"
            )


if __name__ == "__main__":

    client = LLMClient()

    resposta = client.chat(
        prompt="Explique IA em poucas palavras.",
        system="Você é um professor."
    )

    print(resposta)
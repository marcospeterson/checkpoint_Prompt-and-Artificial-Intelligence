import time
import requests
import tiktoken

from retry import retry
from dotenv import load_dotenv


# Carrega variáveis do .env
load_dotenv()


class LLMClient:

    def __init__(
        self,
        model="mistral",
        url="http://localhost:11434/api/chat",
        timeout=120
    ):

        self.model = model
        self.url = url
        self.timeout = timeout
    def contar_tokens(self, texto):
        """
        Conta quantidade aproximada de tokens.
        """

        encoding = tiktoken.get_encoding("cl100k_base")

        tokens = encoding.encode(texto)

        return len(tokens)

    @retry(tries=3, delay=2)
    def chat(self, prompt, system="", temp=0.5, max_tokens=500):
        """
        Envia prompt para o modelo via Ollama.
        """

        inicio = time.time()

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "options": {
                "temperature": temp,
                "num_predict": max_tokens
            },
            "stream": False
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            dados = response.json()

            resposta_modelo = (
                dados["message"]["content"]
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

        except requests.exceptions.Timeout:

            raise Exception(
                "Timeout ao conectar com o Ollama."
            )

        except requests.exceptions.ConnectionError:

            raise Exception(
                "Não foi possível conectar ao Ollama."
            )

        except Exception as erro:

            raise Exception(
                f"Erro inesperado: {erro}"
            )
if __name__ == "__main__":

    client = LLMClient()

    resposta = client.chat(
        prompt="Explique o que é inteligência artificial.",
        system="Você é um professor.",
        temp=0.5
    )

    print(resposta)
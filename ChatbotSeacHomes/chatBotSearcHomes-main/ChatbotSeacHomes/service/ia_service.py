import os
from dotenv import load_dotenv   # ← Adicionado
from groq import Groq

# Carrega o arquivo .env
load_dotenv()   # ← Adicionado aqui

class IAService:
    MODELO = "llama-3.3-70b-versatile"
    MAX_TOKENS = 1024

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY não encontrada no arquivo .env")
        
        self.cliente = Groq(api_key=api_key)

    def enviar_mensagem(self, historico: list, system_prompt: str) -> str:
        try:
            mensagens = [{"role": "system", "content": system_prompt}] + historico

            resposta = self.cliente.chat.completions.create(
                model=self.MODELO,
                messages=mensagens,
                max_tokens=self.MAX_TOKENS,
            )

            return resposta.choices[0].message.content

        except Exception as e:
            mensagem = str(e).lower()
            if "401" in mensagem or "invalid_api_key" in mensagem:
                raise Exception("Erro de autenticação: verifique sua GROQ_API_KEY.")
            elif "429" in mensagem or "rate_limit" in mensagem:
                raise Exception("Limite de requisições atingido. Aguarde um momento.")
            else:
                raise Exception(f"Erro na API da Groq: {str(e)}")


if __name__ == "__main__":
    service = IAService()
    historico_teste = [
        {"role": "user", "content": "Olá! O que ocasionou o incendio em roma?"}
    ]
    system_teste = "Você é um investigador privado que responde a pergunta como se fosse uma investigação"

    print("Enviando mensagem de teste para a IA (Groq)...")
    resposta = service.enviar_mensagem(historico_teste, system_teste)
    print("\nResposta da IA:")
    print(resposta)
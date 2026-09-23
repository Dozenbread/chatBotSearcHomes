import sys
import os
from dotenv import load_dotenv   # ← Adicionado

load_dotenv()   # ← Adicionado (carrega o .env)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from Core.prompt_mestre import PromptMestre
from service.ia_service import IAService

# Inicialização do app e dos serviços
app = Flask(
    __name__,
    static_folder="frontend",
    static_url_path=""
)
CORS(app)

prompt_mestre = PromptMestre()
ia_service = IAService()

# Rota principal
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Rota do chat
@app.route("/chat", methods=["POST"])
def chat():
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"erro": "Nenhum dado recebido."}), 400

        mensagem_usuario = dados.get("mensagem", "").strip()
        historico = dados.get("historico", [])

        if not mensagem_usuario:
            return jsonify({"erro": "A mensagem não pode estar vazia."}), 400

        historico.append({
            "role": "user",
            "content": mensagem_usuario
        })

        # === PROMPT MAIS FORTE ===
        system_prompt = prompt_mestre.get_prompt()
        
        # Reforço extra para manter o personagem
        system_prompt += "\n\nIMPORTANTE: Você é um investigador forense sério e formal. NUNCA responda com receitas, piadas, ou assuntos aleatórios. Mantenha sempre o tom investigativo, formal e dentro do personagem."

        resposta_ia = ia_service.enviar_mensagem(historico, system_prompt)

        return jsonify({"resposta": resposta_ia})

    except Exception as e:
        print(f"[ERRO no chat] {e}")
        return jsonify({"erro": str(e)}), 500

@app.route("/status")
def status():
    return jsonify({"status": "online", "bot": "TutorBot"})


if __name__ == "__main__":
    print("=" * 55)
    print("          TutorBot rodando!")
    print("Acesse: http://localhost:5000")
    print("API em: http://localhost:5000/chat")
    print("Status: http://localhost:5000/status")
    print("=" * 50)
    app.run(debug=True, port=5000)
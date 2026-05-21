
# 🕵️‍♂️ ChatbotSearchHomes - Investigação Forense Digital

O **SearchHomes** (ou TutorBot) é um assistente virtual temático de investigação forense, ambientado em uma atmosfera clássica de mistério. O sistema utiliza Inteligência Artificial por meio da API da **Groq Cloud** para analisar casos, pistas e responder aos questionamentos do usuário no estilo de um perito oficial.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.13 + Flask
* **Inteligência Artificial:** Groq API (`python-dotenv` + `groq`)
* **Frontend:** HTML5, CSS3 (Estilo Vintage/Investigativo) e JavaScript (Vanilla)
* **Renderização de Texto:** Marked.js (para formatação correta de Markdown nas respostas da IA)

---

## 🚀 Como Configurar e Rodar o Projeto Localmente

Siga os passos abaixo para instalar as dependências e configurar as credenciais necessárias de forma segura.

### 1. Clonar o Repositório
Se você acabou de baixar ou clonar o projeto do GitHub, certifique-se de abrir a pasta principal no seu terminal ou VS Code.

### 2. Instalar as Dependências do Python
O projeto necessita da biblioteca `python-dotenv` para gerenciar as chaves de configuração, além do Flask e do ecossistema da Groq. Instale rodando o comando:

```bash
pip install python-dotenv flask groq

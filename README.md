# 🕵️‍♂️ ChatbotSearchHomes - Investigação Forense Digital

### 🎓 Projeto Acadêmico — Faculdade Cruzeiro do Sul

O **SearchHomes** (ou TutorBot) é um assistente virtual temático de investigação forense, ambientado em uma atmosfera clássica de mistério. O sistema utiliza Inteligência Artificial por meio da API da **Groq Cloud** para analisar casos, pistas e responder aos questionamentos do usuário no estilo de um perito oficial do século XIX.

Este software foi desenvolvido como parte das atividades acadêmicas junto à **Faculdade Cruzeiro do Sul**, aplicando conceitos de desenvolvimento web, integração de APIs de IA, segurança de credenciais e arquitetura cliente-servidor.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.13 + Flask (Estrutura de API Restful)
* **Inteligência Artificial:** Groq API (`python-dotenv` + `groq`)
* **Frontend:** HTML5, CSS3 (Estilo Vintage/Investigativo) e JavaScript (Vanilla)
* **Renderização de Texto:** Marked.js (mecanismo que traduz Markdown nas respostas da IA para HTML legível)

---

## 🚀 Como Configurar e Rodar o Projeto Localmente

Siga o passo a passo detalhado abaixo para preparar o ambiente, instalar as dependências e executar o ecossistema na sua máquina.

### 1. Clonar o Repositório
Abra o terminal do seu computador ou do VS Code e clone o projeto usando o comando Git (ou baixe o arquivo .zip direto do GitHub):

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

Em seguida, entre na pasta do projeto:

```bash
cd ChatbotSearchHomes-main
```

### 2. Criar e Ativar um Ambiente Virtual (Recomendado)
Para evitar conflitos com outras versões do Python no seu computador, crie um ambiente isolado (Venv):

* **No Windows (PowerShell/CMD):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **No Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

> 💡 *Nota: Após a ativação, você verá o prefixo `(venv)` aparecer no início da linha do seu terminal.*

### 3. Instalar as Dependências (pip install)
Com o ambiente virtual ativo, instale o microframework Flask, o cliente oficial da API da Groq e o gerenciador de variáveis de ambiente (`python-dotenv`) rodando o comando:

```bash
pip install python-dotenv flask groq
```

> 💡 *Dica Acadêmica: Se o repositório já possuir um arquivo de registros, você também pode rodar:* `pip install -r requirements.txt`

### 4. Configurar as Chaves de API de Forma Segura (Arquivo .env)
Por questões de segurança e boas práticas, o arquivo com a chave da inteligência artificial fica salvo apenas localmente e é ignorado pelo Git através do `.gitignore`.

1. Na raiz do projeto, crie um arquivo de texto e nomeie-o exatamente como: **`.env`**
2. Crie também um arquivo chamado **`.env.example`** (este serve de modelo limpo e vai para o GitHub).
3. Dentro do seu arquivo **`.env`**, cole a sua chave da Groq Cloud:
   ```env
   GROQ_API_KEY=gsk_sua_chave_real_da_groq_aqui
   ```
4. Dentro do arquivo **`.env.example`**, deixe apenas a estrutura de exemplo vazia:
   ```env
   GROQ_API_KEY=
   ```

### 5. Executar o Servidor Backend
Certifique-se de que está na pasta raiz onde se encontra o arquivo `main.py` e execute o comando:

```bash
python main.py
```

O terminal do VS Code exibirá uma mensagem personalizada informando que o **TutorBot está rodando com sucesso**.

### 6. Acessar a Interface Web (Frontend)
Com o servidor Python em execução no terminal, abra o seu navegador de internet e acesse o endereço local da aplicação:
👉 **[http://localhost:5000](http://localhost:5000)**

---

## 👥 Como Contribuir ou Testar o Modelo

Caso queira clonar este projeto para fins de estudo ou avaliação acadêmica:
1. Faça o Fork ou Clone deste repositório.
2. Certifique-se de cumprir os requisitos descritos na seção **Como Configurar**.
3. Crie o seu arquivo `.env` individual utilizando o esqueleto do `.env.example`.

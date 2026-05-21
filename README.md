<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>README - ChatbotSearchHomes</title>
</head>
<body>

    <h1>🕵️‍♂️ ChatbotSearchHomes - Investigação Forense Digital</h1>
    <h3>🎓 Projeto Acadêmico — Faculdade Cruzeiro do Sul</h3>

    <p>
        O <strong>SearchHomes</strong> (ou TutorBot) é um assistente virtual temático de investigação forense, ambientado em uma atmosfera clássica de mistério. O sistema utiliza Inteligência Artificial por meio da API da <strong>Groq Cloud</strong> para analisar casos, pistas e responder aos questionamentos do usuário no estilo de um perito oficial do século XIX.
    </p>
    <p>
        Este software foi desenvolvido como parte das atividades acadêmicas junto à <strong>Faculdade Cruzeiro do Sul</strong>, aplicando conceitos de desenvolvimento web, integração de APIs de IA, segurança de credenciais e arquitetura cliente-servidor.
    </p>

    <hr>

    <h2>🛠️ Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Backend:</strong> Python 3.13 + Flask (Estrutura de API Restful)</li>
        <li><strong>Inteligência Artificial:</strong> Groq API (<code>python-dotenv</code> + <code>groq</code>)</li>
        <li><strong>Frontend:</strong> HTML5, CSS3 (Estilo Vintage/Investigativo) e JavaScript (Vanilla)</li>
        <li><strong>Renderização de Texto:</strong> Marked.js (mecanismo que traduz Markdown nas respostas da IA para HTML legível)</li>
    </ul>

    <hr>

    <h2>🚀 Como Configurar e Rodar o Projeto Localmente</h2>
    <p>Siga o passo a passo detalhado abaixo para preparar o ambiente, instalar as dependências e executar o ecossistema na sua máquina.</p>

    <h3>1. Clonar o Repositório</h3>
    <p>Abra o terminal do seu computador ou do VS Code, clone o projeto e entre na pasta principal:</p>
    <pre><code>git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd ChatbotSearchHomes-main</code></pre>

    <h3>2. Criar e Ativar um Ambiente Virtual (Recomendado)</h3>
    <p>Para isolar as bibliotecas do projeto e evitar conflitos com o seu sistema, execute os seguintes comandos no terminal:</p>
    
    <p><strong>No Windows (PowerShell/CMD):</strong></p>
    <pre><code>python -m venv venv
.\venv\Scripts\activate</code></pre>

    <p><strong>No Linux/macOS:</strong></p>
    <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
    <p><em>*Nota: Após a ativação, o prefixo <code>(venv)</code> aparecerá no início da linha do seu terminal.</em></p>

    <h3>3. Instalar as Dependências (pip install)</h3>
    <p>Com o seu ambiente virtual ativado no terminal, instale o pacote que gerencia as variáveis de ambiente (<code>python-dotenv</code>), o Flask e a biblioteca da Groq:</p>
    <pre><code>pip install python-dotenv flask groq</code></pre>
    <p>💡 <em>Dica Acadêmica: Se preferir utilizar o arquivo de registros do projeto, você também pode rodar <code>pip install -r requirements.txt</code> caso ele esteja disponível.</em></p>

    <h3>4. Configurar as Chaves de API de Forma Segura (Arquivo .env)</h3>
    <p>Por questões de segurança cibernética e boas práticas, o arquivo com a credencial secreta da inteligência artificial fica salvo apenas localmente e é ocultado do GitHub pelo arquivo <code>.gitignore</code>.</p>
    
    <ol>
        <li>Na raiz do projeto, crie um arquivo de texto e mude o nome dele para exatamente: <strong><code>.env</code></strong></li>
        <li>Crie também um arquivo chamado <strong><code>.env.example</code></strong> (este serve de manual limpo e vai para o repositório).</li>
        <li>Abra o seu arquivo <strong><code>.env</code></strong> e adicione a sua chave gerada no painel da Groq Cloud:</li>
    </ol>
    <pre><code>GROQ_API_KEY=gsk_sua_chave_real_da_groq_aqui</code></pre>
    
    <ol start="4">
        <li>No arquivo <strong><code>.env.example</code></strong>, deixe apenas a estrutura vazia indicada para sinalizar aos próximos usuários:</li>
    </ol>
    <pre><code>GROQ_API_KEY=</code></pre>

    <h3>5. Executar o Servidor Backend</h3>
    <p>Certifique-se de que o terminal está operando na pasta raiz onde reside o arquivo <code>main.py</code> e inicie a aplicação:</p>
    <pre><code>python main.py</code></pre>
    <p>O terminal do seu VS Code exibirá os logs customizados indicando que o <strong>TutorBot está rodando com sucesso</strong>.</p>

    <h3>6. Acessar a Interface Web (Frontend)</h3>
    <p>Com o terminal ativo executando o script em segundo plano, abra o navegador de sua preferência e navegue até o endereço local:</p>
    <p>👉 <a href="http://localhost:5000" target="_blank">http://localhost:5000</a></p>

    <hr>

    <h2>👥 Como Contribuir ou Testar o Modelo</h2>
    <p>Caso queira clonar este projeto para fins de estudo ou avaliação acadêmica:</p>
    <ul>
        <li>Faça o Fork ou Clone deste repositório.</li>
        <li>Certifique-se de cumprir os requisitos descritos na seção de configuração.</li>
        <li>Crie o seu arquivo <code>.env</code> individual utilizando o esqueleto do <code>.env.example</code>.</li>
    </ul>

</body>
</html>

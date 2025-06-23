# 📄 Gerador de Resumos Inteligente de PDF e Vídeos com IA

![Demonstração do Projeto](demo/resumo-ia.gif)


Este projeto é uma aplicação web interativa construída com **Streamlit** que permite gerar resumos automáticos de documentos PDF e vídeos do YouTube usando inteligência artificial localmente, com modelos de linguagem como o Mistral via Ollama.

---

## 🚀 Funcionalidades

- Upload e extração de texto de arquivos PDF  
- Extração de transcrição de vídeos do YouTube  
- Geração de resumo automático com IA  
- Download do resumo em formato `.txt`  
- Histórico de resumos gerados durante a sessão, organizado em abas  
- Visual limpo e responsivo, com customização básica de fontes e ícones  

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+  
- Streamlit para interface web  
- Ollama + Mistral (modelo local de IA)  
- PyPDF2 para manipulação de PDFs  
- YouTube Transcript API para transcrição de vídeos  
- Bibliotecas auxiliares: `python-dotenv`, `langchain`, entre outras  

---

## 💻 Como usar

```bash

1. Clone o Repositório: 

git clone https://github.com/gabrielfelip/Resumos-IA.git
cd Resumos-IA

2. Crie e Ative um Ambiente Virtual:

python -m venv venv
 
# Windows:
venv\Scripts\activate

# Linux/MacOS:
source venv/bin/activate

3. Instale as Dependências:

pip install -r requirements.txt

4. Configuração da IA:

Ajuste as configurações para utilizar sua API key da OpenAI ou, preferencialmente, configure para usar Ollama localmente.

5. Execute a Aplicação:

 streamlit run app.py

 6. Acesse no Navegador:

Abra seu navegador e vá para o endereço indicado (geralmente http://localhost:8501).

```

## 🗂️ Estrutura do Projeto
- **app.py:** Arquivo principal com interface Streamlit e lógica de interação

- **pdf_utils.py:** Funções para extrair texto de PDFs

- **youtube_utils.py:** Funções para extrair transcrição de vídeos do YouTube

- **summarizer.py:** Módulo para gerar resumos com IA

- **.streamlit/:** Configurações visuais da aplicação

- **requirements.txt:** Dependências do projeto

###


## 🔮 Próximos Passos (Melhorias Planejadas):

💬🤖**Chatbot Interativo:** *Implementar um chatbot para perguntas e respostas baseadas no conteúdo resumido.*

🎙️🔊**Suporte a Voz:** *Adicionar reconhecimento de fala (Speech-to-Text) e síntese de voz (Text-to-Speech).*

📚📝**Mais Formatos de Arquivo:** *Estender o suporte para DOCX, EPUB, TXT e outros formatos.*



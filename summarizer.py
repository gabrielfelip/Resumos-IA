# summarizer.py
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="mistral", temperature=0.5)

resumo_prompt = PromptTemplate(
    input_variables=["conteudo"],
    template="""
Você é um assistente educacional. Resuma o conteúdo abaixo de forma clara e didática, com até 300 palavras.
Depois, destaque os 5 principais pontos em formato de bullet points.

Conteúdo:
{conteudo}
"""
)


resumo_chain = LLMChain(llm=llm, prompt=resumo_prompt)

def gerar_resumo(conteudo: str) -> str:
    result = resumo_chain.invoke({"conteudo": conteudo})
    return result["text"]


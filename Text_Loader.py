from langchain_community .document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs)
print("=" * 75)
print(type(docs))
print("=" * 75)
print(len(docs))
print("=" * 75)
print(docs[0])
print("=" * 75)


model = ChatGroq(model='openai/gpt-oss-120b')
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

chain = prompt | model | parser

result = chain.invoke({'poem' : docs[0].page_content})
print(result)
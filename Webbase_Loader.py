from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n{text}',
    input_variables=['question','text']
)

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question' : 'What is the product that we are talking about ?','text' : docs[0].page_content})

print(result)



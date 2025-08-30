from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()
print(docs)
print("=" * 100)
print(docs[0].page_content)
print(docs[0].metadata)

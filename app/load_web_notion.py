from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders import NotionDirectoryLoader

# pip install bs4

## Carregamento de uma página na Web ##
loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/README.md")

docs = loader.load()

# Vários textos com diversos campos em branco, um bom exemplo onde é necessário realizar tratamento
print(docs[0].page_content[:500])

## Carregamento de um arquivo no Notion ##

loader = NotionDirectoryLoader("docs/Notion_DB")
docs = loader.load()

print(docs[0].page_content[0:200])

print(docs[0].metadata)

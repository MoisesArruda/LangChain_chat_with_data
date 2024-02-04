"""Retorna uma lista de objetos "Document"."""

from langchain.document_loaders import PyPDFLoader

# Cria um carregador de PDF
loader = PyPDFLoader(r'C:\AI\Cursos\LangChain_Chat_Data\data')

# Carregar o documento diferenciando cada página.
pages = loader.load()

# Por padrão, carregamos uma lista de documents, neste casso temos 22 diferentes páginas no PDF.
# Cada uma é um documento próprio
print(len(pages))

# Visualizar o conteudo da primeira página.
page = pages[0]
# page_content é o texto/conteudo da página.
print(page,page.page_content[:500])
print(page.metadata)

## Carregando informações de um vídeo no Youtube ##

# Parte chave do conteúdo é o carregador de áudio


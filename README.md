# Explicação do projeto.

Este repositório tem o propósito de armazenar o conhecimento adquirido durante o curso proposto pela DeerpLearning.AI, onde sua grande proposta é
desenvolver sua própria aplicação que permite interagir com os dados usando LangChain e LLMs.

[Acesse o curso neste link.](https://www.coursera.org/learn/langchain-chat-with-your-data-project/ungradedLti/OgMwW/langchain-chat-with-your-data)

## Document Loading

Fundamentos de carregamento e descobrimento de dados com mais de 80 loaders do LangChain, providenciado para acessar diversas fontes de dados,
incluindo áudio e vídeo.

Retorna uma lista de objetos "Document". Não necessitamos da conexão da API com o LLM

# Parte chave do conteúdo é o carregador de áudio

[Acesse aqui.]()

## Document Splitting

Melhores práticas e considerações para cortes/separação de arquivos para pequenos chunks da maneira correta.

É importante realizar a separação considerando todo o contexto para que a informação faça sentido.

[Acesse aqui.]()

## Vector stores and embeddings

Entenda o conceito de embeddings e explore as integrações de Vectors stores com o LangChain.

Pegaremos nossos documentos recortados em pequenos chunks, e colocaremos estes chunks em indíces para obter retornos melhores
quando for responder a uma pergunta.

Embedding = Pegar um pedaço de texto(chunks) e criar uma representação numérica daquele texto, conteudos similares terão vetores similares.

Vector Store = Um DB onde por facilmente encontrar vetores similares, muito útil quando quisermos encontrar documentos similares
as perguntas que queremos responder, pois iremos criar embeddings da pergunta e comparar com o que temos armazenado

!(VectorStore.png)

!(process_query.png)


## Retrieval

Compreenda as técnicas avançadas para acessar e indexar arquivos na vector sotre, possibilitando recuperar as mais importantes informações
pela busca semantica.

É a parte central do nosso fluxo RAG.

!(Retrieval.png)

## Question Answering

Criar uma solução de respostas a perguntas.

1. As dúvidas são aplicadas para a Vector Store como uma query.
2. Vector Store providência *K* documentos relevantes.
3. Documentos e a dúvida são enviados para o LLM

!(Question_answering.png)

## Chat

Aprenda como acompanhar e selecionar as informações pertinentes em conversas e fontes de dados, para que construa o seu chatbot usando LangChain.

1. Configuração do recurso de memória.
2. Criação de chain conversacional com recurso de memória.

[Acesse aqui.]()
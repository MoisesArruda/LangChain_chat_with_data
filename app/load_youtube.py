"""Carregando informações de um vídeo no Youtube."""

#%%
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from yt_dlp.postprocessor import FFmpegPostProcessor
FFmpegPostProcessor._ffmpeg_location.set(R'CC:\ffmpeg-6.1.1-full_build')

#  pip install yt_dlp pydub pip install youtube-dl

# Para realizar o download utilize o seguinte link - https://www.wikihow.com/Install-FFmpeg-on-Windows

url = "https://www.youtube.com/watch?v=jGwO_UgTS7I"
# Onde armazenar os arquivos de áudio.
save_dir = "data/youtube/"
# Carregamento generico, combinação do Audio Loader com o Parser
loader = GenericLoader(
    # Parte chave do conteúdo é o carregador de áudio
    YoutubeAudioLoader([url], save_dir),
    OpenAIWhisperParser())

docs = loader.load()
# Verificar o conteudo do vídeo
print(docs[0].page_content[0:500])
# %%

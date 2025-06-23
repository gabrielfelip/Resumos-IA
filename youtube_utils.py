# youtube_utils.py
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extrair_transcricao_youtube(url: str) -> str:
    try:
        video_id = parse_qs(urlparse(url).query)["v"][0]
        transcricao = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])

        texto = " ".join([item["text"] for item in transcricao])
        return texto
    except Exception as e:
        return f"Erro ao obter transcrição: {str(e)}"

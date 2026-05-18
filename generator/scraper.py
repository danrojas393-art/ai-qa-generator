import requests

def obtener_html(url: str) -> str:
    response = requests.get(url)
    return response.text
    
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

def obtener_respuesta_claude(prompt):
     client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
     message = client.messages.create(
         model="claude-sonnet-4-20250514",
         max_tokens=2048,
         messages=[
             {"role":"user","content":prompt}
         ]
     )
     
     return message.content[0].text
 
# Generador de pruebas QA con IA

proyecto de automatizacion que combina Python y la API d Claude (Anthropic)
para generar automatizacion casos de prueba en Cypress a partir del HTML 
de una paguina wed 

## ¿Que hace?

1.Extrae el HTML de DemoBlaze con scraper.py
2.Envia ese HTML  Claude API con claude_client.py
3.El archivo generado se guarda en cypress/e2e/

## Tecnologuia 
-Python 3.12 
-Anthropic claude API
-BeautifulSoup / Requests

## Como ejecutalo
bash
# instalar dependecias 
pip install -r requirements_wripter.py

## AUTOR 
Daniel Rojas-QA Tester junior 





















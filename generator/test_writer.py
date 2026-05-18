import os
from claude_client import obtener_respuesta_claude
from scraper import obtener_html

SITIO_URL = "https://www.demoblaze.com"
ARCHIVO_SALIDA = "cypress/e2e/pruebas_generada.cy.js"

def generar_pruebas_cypress(html:str) -> str:
    prompt = f"""
    eres un experto QA  y automatizacion con Cypress.
    Analiza el siguiente HTML de un paguna wed y genera un archivo de prueba Cypress (.cy.js) en JavaScript.
    
    Requisitos:
    -Usa comandos reales de Cypress: cy.visit(), cy.get(), cy.click(), cy.type(), cy.should(), etc.
    -Crea almenos 3 casos de pruebas (it blocks) dentro de un describe block.
    -Los casos deben probar funcionalidades visibles en el HTML (botones, formularios, navegacion, etc.)
    -Usa selectores reales encontrados en el HTML (id, class, name, etc.).
    -El codigo debe estar  listo para ejecutarse sin modificaciones.
    -No agregues explicaciones, solo el codigo .cy.js.
    
    HTML dela paguina:
    {html[:6000]}
    """
    respusta = obtener_respuesta_claude(prompt)
    return respusta

def guardar_pruebas(contenido: str, ruta: str):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "W" , encoding="utf-8") as archivo:
        archivo.write(contenido)
        print(f"Pruebas generada y guardada en: {ruta}")
        
        def main():
            print("Obteniendo HTML de la pagina...")
            html = obtener_html(SITIO_URL)
            
            if not html:
                print("No se pudo odtener el HTML. Verifica la URL y tu conexion.")
                return
            
            print("enviando HTML a Claude para generar pruebas Cypress...")
            prueba = generar_pruebas_cypress(html)
            
            if not prueba:
                print("Claude no devolvio una respuesta. Verifica tu clave API key.")
                return
            
            print("guardando archivo de pruebas...")
            guardar_pruebas(pruebas,ARCHIVO_SALIDA)
            
            print("\n¡LISTO! Para ejecutar la prueba corre:")
            print(f" npx cypress run --spec \"{ARCHIVO_SALIDA}\"")
            
            if __name__ == "__main__":
                main()
            
            
            

                
                


                
    
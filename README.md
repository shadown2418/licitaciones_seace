# Licitaciones Perú App

Esta aplicación web busca licitaciones de obras públicas (simuladas) y permite descargar un archivo Excel con los datos.

## Cómo desplegar en Render

1. Crea una cuenta gratuita en [Render.com](https://render.com)
2. Sube este proyecto a tu GitHub
3. En Render, elige "New Web Service"
4. Conecta tu repositorio y configura:
   - Runtime: Python 3
   - Start command: `gunicorn app:app`
   - Build command: `pip install -r requirements.txt`
5. Haz deploy y accede a la URL generada
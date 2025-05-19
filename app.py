from flask import Flask, render_template, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route("/")
def index():
    # Simulación de scraping
    data = [
        {"Entidad": "MTC", "Objeto": "Construcción de puente", "Región": "Cusco", "Monto": 2500000},
        {"Entidad": "MVCS", "Objeto": "Agua potable rural", "Región": "Puno", "Monto": 1200000},
    ]
    df = pd.DataFrame(data)
    # Guardar archivo Excel en memoria
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return render_template("index.html", data=data)

@app.route("/descargar")
def descargar_excel():
    data = [
        {"Entidad": "MTC", "Objeto": "Construcción de puente", "Región": "Cusco", "Monto": 2500000},
        {"Entidad": "MVCS", "Objeto": "Agua potable rural", "Región": "Puno", "Monto": 1200000},
    ]
    df = pd.DataFrame(data)
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return send_file(output, download_name="licitaciones.xlsx", as_attachment=True)
from flask import Flask, render_template, request
from src.core.search import buscar_producto

app = Flask(__name__)

def parse_precio(precio_str):
    """Convierte 'S/ 1,529' → 1529.0 para poder ordenar"""
    try:
        return float(precio_str.replace("S/", "").replace(",", "").replace("\xa0", "").strip())
    except:
        return float("inf")  # Si no se puede convertir, lo ponemos al final

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = None
    query = None
    if request.method == "POST":
        query = request.form.get("query")
        resultados = buscar_producto(query)
        
        if resultados:
            # Convertimos precios a float
            for r in resultados:
                r["precio_float"] = parse_precio(r["precio"])
            
            # Ordenamos de menor a mayor
            resultados = sorted(resultados, key=lambda x: x["precio_float"])
            
            # Marcamos el producto más barato
            resultados[0]["mejor_precio"] = True

    return render_template("index.html", resultados=resultados, query=query)

if __name__ == "__main__":
    app.run(debug=True)

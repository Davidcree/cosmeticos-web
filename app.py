from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 🔹 Datos simulados (luego esto se cambia por SQL)
def get_productos():
    return [
        {"id": 1, "nombre": "Labial Mate", "precio": 25, "imagen": "/static/img/labial.jpg"},
        {"id": 2, "nombre": "Base Líquida", "precio": 40, "imagen": "/static/img/base.jpg"},
        {"id": 3, "nombre": "Perfume Floral", "precio": 80, "imagen": "/static/img/perfume.jpg"},
        {"id": 4, "nombre": "Sombra", "precio": 500, "imagen": "/static/img/sombra.jpg"}
    ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/productos")
def obtener_productos():
    return jsonify(get_productos())

#if __name__ == "__main__":
#    app.run(debug=True)
from flask import Flask, request, jsonify
app = Flask(__name__)

# endponit/characters/4
@app.route("/json")
def sereliazar_json():
    return jsonify({"clave": "valor", "clave2": "valor2", "arreglo": ['Hola', 'Geeks', 'CCS', '33']})

app.run(host='127.0.0.1', port=5000, debug=True)
from flask import Flask, request, jsonify
app = Flask(__name__)

# endponit/characters/4

@app.route("/mensaje", methods=['get','post','put'])
def hello():
    body = request.json
    if(request.method == 'GET'):
        if "mensaje" in body:
            return (f'Hello Bienvenido al API de Mensajes!, tu mensaje es { body["mensaje"] }'), 200
    else:
        if request.method == "PUT":
            if "mensaje" in body:
                print(body)
                return "La peticion tiene mensaje", 200
            else:
                print(body)
                return "peticion incorrecta, cuerpo no tiene mensaje!", 400
            return 200
        if request.method == "POST":
            return "Metodo POST no habilitado", 200


@app.route("/mensaje/<int:number>", methods=['delete'])
def specific_msj(number):
    print("numero del request", number)
    return f'Tu numero solicitado es {number} !', 200

@app.route("/mensaje/<int:number>", methods=['post'])
def cotribute(number):
    print("numero del contribucion", number)
    counter = 100 + number
    return f'Tu numero contribucion fue {number} ! y el conteo actual es {counter}', 200

@app.route("/json")
def sereliazar_json():
    return jsonify({"clave": "valor", "clave2": "valor2", "arreglo": ['Hola', 'Geeks', 'CCS', '33']})

app.run(host='127.0.0.1', port=5000, debug=True)
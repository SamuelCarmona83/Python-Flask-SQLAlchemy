from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Hello Geeks!")
    return "Hello Roberto SIUUUUUUUU!"

app.run(host='127.0.0.1', port=5000, debug=True)
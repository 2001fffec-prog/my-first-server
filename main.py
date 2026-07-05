from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Мой Flask сервер работает!"

@app.route("/greet")
def greet():
    name = request.args.get("name", "Незнакомец")
    return jsonify({"message": "Привет, " + name + "!"})

if __name__ == "__main__":
app.run()


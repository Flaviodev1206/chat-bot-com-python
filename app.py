from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem", "")
    # Simple placeholder response - replace with actual chatbot logic
    resposta = f"Obrigado pela sua mensagem: '{mensagem}'. Em breve um atendente irá ajudá-lo!"
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run()

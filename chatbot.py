from flask import Flask, request, jsonify, render_template
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

#add your sentences here
pairs = [
    ["ciao", ["Ciao!", "Come posso aiutarti?"]],
    ["come ti chiami?", ["Mi chiamo .... Bot.", "Sono un bot di.... ."]],
    ["come stai?", ["Sto bene.", "Ho la susta.", "Sto Male."]],
    ["chi è il tuo creatore?", ["Sono stato creato da Giannetto.", "Il mio creatore è...."]],
    ["cosa puoi fare?", ["..... non mi ha ancora programmato."]],
    ["uscita", ["Arrivederci!", "A presto!"]],
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["user_message"]
    response = chatbot.respond(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    nltk.download("punkt")
    app.run(debug=True)

from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
import openai
import os
from chat import Chat, load_indices, get_chat_name
from uuid import uuid4

app = Flask(__name__, template_folder="static/")
CORS(app)

# Set up OpenAI API credentials
# openai.api_key = "YOUR_API_KEY"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("static/dist", filename)


@app.route("/api/chat", methods=["POST"])
@cross_origin()
def api():
    categories = request.json.get("categories")
    message = request.json.get("message")

    _chat = Chat(load_indices(categories))
    _id = str(uuid4())
    chats[_id] = _chat
    response = _chat.engine.chat(message)
    name = get_chat_name(message)
    print(name)
    if response != None:
        reply = response
        if type(response) is not str:
            reply = response.response
        return {"answer": reply, "id": _id, "name": name}
    else:
        return "Failed to Generate response!"


@app.route("/api/chat/<chat_id>", methods=["POST"])
@cross_origin()
def chat(chat_id):
    message = request.json.get("message")

    _chat = chats[chat_id]
    response = _chat.engine.chat(message)
    if response != None:
        reply = response
        if type(response) is not str:
            reply = response.response
        return {"answer": reply}
    else:
        return "Failed to Generate response!"


if __name__ == "__main__":
    chats = {}
    app.run()

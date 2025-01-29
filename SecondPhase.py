import os
from flask import Flask, request, render_template_string, redirect, url_for
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Flask
app = Flask(__name__)
# Groq API
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

def load_knowledge(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


knowledge_base = load_knowledge("dummytext.txt")


context = f"Bu bilgileri kullanarak cevap ver: {knowledge_base}"


chat_history = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ontology SparQL Query Bot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .chat-container {
            width: 90%;
            max-width: 600px;
            background: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
        }
        .chat-header {
            background: #4a90e2;
            color: white;
            padding: 16px;
            text-align: center;
        }
        .chat-body {
            padding: 16px;
            height: 400px;
            overflow-y: auto;
            border-bottom: 1px solid #ddd;
        }
        .chat-footer {
            padding: 16px;
            display: flex;
            gap: 8px;
        }
        input[type="text"] {
            flex: 1;
            padding: 8px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background: #4a90e2;
            color: white;
            border: none;
            padding: 8px 16px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background: #357abd;
        }
    </style>    
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h2>Satılmış Kabasakal </h2>
            <h1>Ontology SparQL Query</h1>
        </div>
        <div class="chat-body" id="chat-body">
            {% for message in messages %}
                <div><strong>{{ message.role }}:</strong> {{ message.content }}</div>
            {% endfor %}
        </div>
        <div class="chat-footer">
            <form method="POST" action="/">
                <input type="text" name="user_query" placeholder="Sorunuzu yazın..." required>
                <button type="submit">Gönder</button>
            </form>
            <form method="POST" action="/clear">
                <button type="submit" style="background: #e74c3c;">Temizle</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

# Main page
@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_query = request.form.get("user_query")
        if user_query:

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": context,
                    },
                    {
                        "role": "user",
                        "content": user_query,
                    },
                ],
                model="llama-3.3-70b-versatile",
            )

            # Add Respond
            chat_history.append({"role": "user", "content": user_query})
            chat_history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})

    return render_template_string(HTML_TEMPLATE, messages=chat_history)

#Clear chat
@app.route("/clear", methods=["POST"])
def clear():
    global chat_history
    chat_history = []
    return redirect(url_for("chat"))

if __name__ == "__main__":
    app.run(debug=True, port=5050)

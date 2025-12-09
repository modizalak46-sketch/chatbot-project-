from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand."

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot_response():
    user_input = request.json["message"]
    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
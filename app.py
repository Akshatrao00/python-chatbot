from flask import Flask, request, render_template
import re
import random

app = Flask(__name__)

responses = {
    r'hello|hi|hey': ["Hello!", "Hi there!", "Hey!"],
    r'how are you': ["I'm good!", "Doing great!"],
    r'bye|goodbye': ["Goodbye!", "See you later!"]
}

default_responses = [
    "I don't understand that.",
    "Can you ask differently?",
    "Sorry, I didn't get that."
]

def get_response(user_input):
    user_input = user_input.lower().strip()
    for pattern, reply_list in responses.items():
        if re.search(pattern, user_input):
            return random.choice(reply_list)
    return random.choice(default_responses)

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        reply = get_response(user_input)
    return render_template("index.html", response=reply)

if __name__ == "__main__":
    app.run(debug=True)

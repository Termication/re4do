from flask import Flask, jsonify, render_template, request, session
from pymongo import MongoClient
import random

app = Flask(__name__)
app.secret_key = "DEFnbjxuhjgHBI12345"


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["emoji_game"]
users_collection = db["users"]

EMOJIS = ["😄", "😂", "🙃", "🥰", "😭", "😍", "😎", "🤔", "🤩", "😡",
          "😴", "😇", "🤯", "🤡", "😬", "🤓", "🥳", "😢", "🤤", "🤑",
          "🥺", "😱", "😷", "🤒", "🤕", "🧐", "😪", "🤪", "🫠", "🥶",
          "😵", "🤠", "👿", "🧛", "🧟", "👽", "👻", "💀", "🎃", "🤖",
          "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯",
          "🦁", "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🐦", "🐤", "🦆",
          "🦅", "🦉", "🐴", "🦄", "🐝", "🐛", "🦋", "🐌", "🐞", "🐜",
          "🦟", "🦗", "🕷", "🦂", "🐢", "🐍", "🦎", "🐙", "🦑", "🦀",
          "🐡", "🐠", "🐟", "🐬", "🐳", "🐋", "🦈", "🦧", "🐘", "🦏"]

@app.route('/')
def index():
    return render_template('game.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get("name")
    country = data.get("country")
    city = data.get("city")

    if not name or not country or not city:
        return jsonify({"error": "All fields are required"}), 400

    # Store user details in session and MongoDB
    session["user"] = {"name": name, "country": country, "city": city}
    users_collection.insert_one(session["user"])

    return jsonify({"message": "User registered successfully"})


@app.route('/new-round')
def new_round():
    if "user" not in session:
        return jsonify({"error": "User not registered"}), 403

    target = random.choice(EMOJIS)
    options = random.sample(EMOJIS, len(EMOJIS) - 1)
    options.append(target)
    random.shuffle(options)

    return jsonify({"target": target, "options": options})
    
if __name__ == '__main__':
    app.run(debug=True)

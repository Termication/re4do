from flask import Flask, jsonify, render_template, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session handling

EMOJIS = ["😄", "😂", "🙃", "🥰", "😭", "😍", "😎", "🤔", "🤩", "😡",
          "😴", "😇", "🤯", "🤡", "😬", "🤓", "🥳", "😢", "🤤", "🤑",
          "🥺", "😱", "😷", "🤒", "🤕", "🧐", "😪", "🤪", "🫠", "🥶",
          "😵", "🤠", "👿", "🧛", "🧟", "👽", "👻", "💀", "🎃", "🤖",
          "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯",
          "🦁", "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🐦", "🐤", "🦆"]

@app.route('/')
def index():
    session['game_started'] = False  # Ensure game is paused on first load
    return render_template('game.html')

@app.route('/start-game', methods=['POST'])
def start_game():
    session['game_started'] = True
    return jsonify({"status": "Game started"})

@app.route('/new-round')
def new_round():
    if not session.get('game_started', False):  # Don't start until play is clicked
        return jsonify({"error": "Game not started yet"}), 403

    target = random.choice(EMOJIS)
    num_options = min(80, len(EMOJIS))
    options = random.sample(EMOJIS, num_options - 1)
    options.append(target)
    random.shuffle(options)

    return jsonify({"target": target, "options": options})

if __name__ == '__main__':
    app.run(debug=True)

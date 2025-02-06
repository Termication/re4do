from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = "DEFnbjxuhjgHBI12345"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    sessions = db.relationship('GameSession', backref='user', lazy=True)

class GameSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer)
    played_at = db.Column(db.DateTime, default=db.func.current_timestamp())

EMOJIS = ["😄", "😂", "🙃", "🥰", "😭", "😍", "😎", "🤔", "🤩", "😡",
          "😴", "😇", "🤯", "🤡", "😬", "🤓", "🥳", "😢", "🤤", "🤑",
          "🥺", "😱", "😷", "🤒", "🤕", "🧐", "😪", "🤪", "🫠", "🥶",
          "😵", "🤠", "👿", "🧛", "🧟", "👽", "👻", "💀", "🎃", "🤖",
          "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯",
          "🦁", "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🐦", "🐤", "🦆",
          "🦅", "🦉", "🐴", "🦄", "🐝", "🐛", "🦋", "🐌", "🐞", "🐜",
          "🦟", "🦗", "🕷", "🦂", "🐢", "🐍", "🦎", "🐙", "🦑", "🦀",
          "🐡", "🐠", "🐟", "🐬", "🐳", "🐋", "🦈", "🦧", "🐘", "🦏"]

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('register'))
    
    user = User.query.get(session['user_id'])
    return render_template('game.html', current_score=user.score)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        
        session['user_id'] = user.id
        return redirect(url_for('index'))
    
    return render_template('register.html')

@app.route('/new-round')
def new_round():
    if 'user_id' not in session:
        return redirect(url_for('register'))
    
    target = random.choice(EMOJIS)
    options = random.sample(EMOJIS, min(80, len(EMOJIS)) - 1)
    options.append(target)
    random.shuffle(options)

    return jsonify({"target": target, "options": options})

@app.route('/save-score', methods=['POST'])
def save_score():
    if 'user_id' not in session:
        
        return jsonify({'status': 'error'}), 401
    
    user = User.query.get(session['user_id'])
    data = request.get_json()
    new_score = data.get('score', 0)
    
    # Update user's total score
    user.score = new_score
    # Create new game session
    game_session = GameSession(user_id=user.id, score=new_score)
    db.session.add(game_session)
    db.session.commit()
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
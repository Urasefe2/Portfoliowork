# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DBNAME.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    email= db.Column(db.String(100))
    def __repr__(self):
        return f'<User {self.id}>'
# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    button_unity = request.form.get('button_unity')
    texty = request.form.get("text")
    ema1l = request.form.get("email")
    card = Card(text=texty,email=ema1l)
    db.session.add(card)
    db.session.commit()
    return render_template('index.html',
                            button_python=button_python,
                            button_discord=button_discord,
                            button_html=button_html,
                            button_unity=button_unity,
                            button_db=button_db

                            )


if __name__ == "__main__":
    app.run(debug=True)

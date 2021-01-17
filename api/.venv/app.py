# Flask, SQLAlchemy imports
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tenet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model setup


class Tenet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    plot = db.Column(db.String(300))
    tagline = db.Column(db.String(20))
    rating = db.Column(db.Numeric(10, 1))
    director = db.Column(db.String(50))
    genre = db.Column(db.String(20))
    runtime = db.Column(db.String(20))
    genre = db.Column(db.String(20))

    def __repr__(self):
        return f"{self.title} - {self.plot}"


# @app.route('/')
# def index():
#     return 'Hello'


@app.route('/tenet')
def get_details():
    movie_details = Tenet.query.all()
    output = []
    for data in movie_details:
        tenet_data = data.title, data.plot, data.tagline, data.rating, data.director, data.genre, data.runtime

    output.append(tenet_data)

    return render_template('index.html',
                           title=data.title, plot=data.plot, tagline=data.tagline,
                           rating=data.rating, director=data.director, genre=data.genre, runtime=data.runtime)

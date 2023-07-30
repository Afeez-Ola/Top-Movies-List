from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import requests
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-list.db"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)
db.init_app(app)


class MovieList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Float)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


with app.app_context():
    db.create_all()


@app.route("/", methods=["POST", "GET"])
def home():
    all_movies = MovieList.query.order_by(MovieList.rating).all()
    for index, movie in enumerate(all_movies):
        movie.ranking = len(all_movies) - index
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        movie_name = request.form.get('movie_name')
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}"
        headers = {
            "accept": "application/json",
            'Authorization': "Bearer {os.getenv('API_KEY')}"
        }
        response = requests.get(url, headers=headers)
        movie_data = response.json()["results"][0]

        movie_id = movie_data["id"]
        existing_movie = MovieList.query.filter_by(title=movie_data["original_title"]).first()

        if existing_movie:
            return "Movie already exists in the database."

        year = int(movie_data["release_date"][:4])
        new_movie = MovieList(
            id=movie_id,  # Set the ID explicitly
            title=movie_data["original_title"],
            year=year,
            description=movie_data["overview"],
            rating=movie_data["vote_average"],
            ranking=8,
            review="My favourite character was Oppenheimer.",
            img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', movie_id=new_movie.id))

    return render_template("add.html")


@app.route("/edit/<int:movie_id>", methods=["POST", "GET"])
def edit(movie_id):
    movie = MovieList.query.get_or_404(movie_id)

    if request.method == "POST":
        ranking = request.form.get('ranking')
        review = request.form.get('review')

        if ranking is not None:
            movie.ranking = float(ranking)
        movie.review = review
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', movie=movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = MovieList.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=3000)

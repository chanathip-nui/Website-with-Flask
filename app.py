from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    apps_data = [
        {
            "name": "Photo Editor",
            "category": "Photography",
            "rating": "4.8",
            "icon_url": "https://img.icons8.com/fluency/48/photo-editor.png",
        },
        {
            "name": "Fitness Tracker",
            "category": "Health",
            "rating": "4.5",
            "icon_url": "https://img.icons8.com/3d-fluency/94/apple-watch.png",
        },
        # Add more...
    ]
    return render_template("main/index.html", apps=apps_data)


@app.route("/games")
def games():
    games_data = [
        {
            "name": "Super Racer",
            "category": "Racing",
            "rating": "4.6",
            "icon_url": "https://img.icons8.com/fluency/48/rocket.png",
        },
        {
            "name": "Space Adventure",
            "category": "Adventure",
            "rating": "4.9",
            "icon_url": "https://img.icons8.com/dusk/64/space.png",
        },
    ]
    return render_template("main/games.html", games=games_data)


@app.route("/movies")
def movies():
    movies_data = [
        {
            "name": "Action Flick",
            "category": "Action",
            "rating": "4.7",
            "icon_url": "https://img.icons8.com/fluency/48/action.png",
        },
        {
            "name": "Comedy Central",
            "category": "Comedy",
            "rating": "4.5",
            "icon_url": "https://img.icons8.com/fluency/48/comedy.png",
        },
    ]
    return render_template("main/movies.html", movies=movies_data)


@app.route("/books")
def books():
    books_data = [
        {
            "name": "The Great Novel",
            "category": "Fiction",
            "rating": "4.9",
            "icon_url": "https://img.icons8.com/fluency/48/book.png",
        },
        {
            "name": "Learning Python",
            "category": "Education",
            "rating": "4.8",
            "icon_url": "https://img.icons8.com/fluency/48/learning.png",
        },
    ]
    return render_template("main/books.html", books=books_data)


if __name__ == "__main__":
    app.run(debug=True)

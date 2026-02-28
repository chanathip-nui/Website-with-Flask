from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    apps_data = [
        {
            "name": "Photo Editor",
            "category": "Photography",
            "rating": "4.8",
            "icon_url": "https://via.placeholder.com/150",
        },
        {
            "name": "Fitness Tracker",
            "category": "Health",
            "rating": "4.5",
            "icon_url": "https://via.placeholder.com/150",
        },
        # Add more...
    ]
    return render_template("index.html", apps=apps_data)


if __name__ == "__main__":
    app.run(debug=True)

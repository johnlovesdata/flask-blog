from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

posts = [
    {
        "author": "John Schroeder",
        "title": "blog post 1",
        "content": "first post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "blog post 2",
        "content": "second post content",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)

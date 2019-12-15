from flask import render_template, url_for, flash, redirect

from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
    {
        "author": "Serhii Khortiuk",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Anonymous user",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.email.data == "admin@blog.com" and
                form.password.data == "password"):
            flash("You have been logged in!", "success")
            return redirect("home")
        else:
            flash(
                f"Login Unsuccessful please check username and password",
                "danger"
            )

    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect("home")

    return render_template("register.html", title="Register", form=form)

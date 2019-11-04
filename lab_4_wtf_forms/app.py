from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config["SECRET_KEY"] = "some_key"
app.config["RECAPTCHA_PUBLIC_KEY"] = "your_key_here"
app.config["RECAPTCHA_PRIVATE_KEY"] = "your_key_here"
app.config["TESTING"] = True


class LoginForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            InputRequired("A username is required!"),
            Length(min=5, max=10, message="Must be from 5 to 10 chars")
        ]
    )
    password = PasswordField(
        "password",
        validators=[
            InputRequired("Password is required!"),
            AnyOf(values=["password", "secret"])
        ]
    )
    recaptcha = RecaptchaField()


@app.route("/form", methods=["GET", "POST"])
def form():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return (
            f"<h1> username = {login_form.username.data} & password ="
            f" {login_form.password.data}</h1>"
        )
    return render_template("form.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

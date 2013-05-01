from flask import Flask, render_template, session, url_for, request, escape, redirect, g
from functools import wraps
import database

words = ["Hola","Noticias","Foto","Cosa","Buscar","Contras&#209;a"] 
#hard coded since python can't interact with the extension
answers = ["hello","news","photo","thing","search","password"]
corrects = {}

#configuration
DEBUG = True

#init
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "babble"

@app.route("/")
def index():
    user = "Login"
    if "user" in session:
        user = session["user"]
    return render_template("popup.html", user=user)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/quiz", methods=['GET','POST'])
def quiz():
    if request.method == "POST":
        corrects = {}
        responses = {}
        for i in range(len(words)):
            responses[words[i]] = request.form[words[i]]
            if(request.form[words[i]] == answers[i]):
                corrects[words[i]] = "correct"
            else:
                corrects[words[i]] = "incorrect"
        color = "blue"
        return render_template("quiz.html", words=words, color=color, corrects=corrects, responses=responses)
    else:
        corrects = {}
        responses = {}
        color = "gray"
        return render_template("quiz.html", words=words, color=color, corrects=corrects, responses=responses)

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("index"))
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if database.verify(username, password):
            session["user"] = username
            return redirect(url_for("index"))
    return render_template("login.html")
        
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("index"))

@app.route("/get_username")
def get_username():
    if "user" in session:
        return session["user"]
    else:
        return ""

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST" and request.form["username"] and request.form["password"]:
        database.register(request.form["username"], request.form["password"])
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/drop_accounts")
def drop_accounts():
    database.dropAccounts();
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()

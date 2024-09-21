from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy.sql import text

app = Flask(__name__)
app.secret_key=getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT * FROM posts"))
    posts = result.fetchall()
    return render_template("index.html", posts = posts)


@app.route("/new_post",methods =["POST","GET"])
def new_post():
    if request.method =="GET":
        return render_template("new_post.html")
    content = request.form["content"]
    query = text("INSERT INTO posts (breadtext) VALUES (:content)")
    db.session.execute(query, {"content": content})
    db.session.commit()
    return redirect("/")




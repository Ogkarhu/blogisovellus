from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy.sql import text

app = Flask(__name__)
app.secret_key=getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return redirect("/frontpage")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    pw = request.form.get("pw")
    query = text("SELECT * FROM users WHERE username = :username AND pw = :pw")
    result = db.session.execute(query, {"username": username, "pw": pw})
    user = result.fetchone()
    if user:
        session["username"] = username
        return redirect("/frontpage")
    else:
        return "Invalid username or password", 401

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/frontpage")
def frontpage():
    print(session)
    if session.get("username",0):
        result = db.session.execute(text("SELECT * FROM posts"))
        posts = result.fetchall()
        return render_template("frontpage.html", posts = posts)
    else:
        return redirect("/login")


@app.route("/new_post", methods=["POST", "GET"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    
    content = request.form["content"]
    link = request.form.get("link", "")

    youtube_url = None

    if "youtube.com/watch?v=" in link:
        index = link.find("v=") + 2
        endindex = link.find("&", index)
        unique = link[index:endindex] if endindex != -1 else link[index:]
        youtube_url = f"https://www.youtube.com/embed/{unique}"
    elif "youtu.be/" in link:
        # Extract video ID
        unique = link.split("youtu.be/")[1]
        youtube_url = f"https://www.youtube.com/embed/{unique}"
    else:
        return redirect("/frontpage")

    # Insert post (comment and YouTube link) into the database
    query = text("INSERT INTO posts (breadtext, youtube_url) VALUES (:content, :youtube_url)")
    db.session.execute(query, {"content": content, "youtube_url": youtube_url})
    db.session.commit()

    return redirect("/frontpage")


@app.route("/new_user",methods =["POST","GET"])
def new_user():
    if request.method == "GET":
        return render_template("new_user.html")
    
    if request.method == "POST":
        username = request.form["username"]
        pw = request.form["pw"]
        is_admin= request.form.get("is_admin") == "TRUE"

        query = text("INSERT INTO users (username,pw, is_admin) VALUES (:username, :pw, :is_admin)")

    try:    
        db.session.execute(query,{"username": username, "pw": pw, "is_admin": is_admin})
        db.session.commit()
        return redirect('/')
    except Exception as e:    
        db.session.rollback()
        return f"An error occurred: {str(e)}"



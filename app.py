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
        return redirect("/")

    # Insert post (comment and YouTube link) into the database
    query = text("INSERT INTO posts (breadtext, youtube_url) VALUES (:content, :youtube_url)")
    db.session.execute(query, {"content": content, "youtube_url": youtube_url})
    db.session.commit()

    return redirect("/")

@app.route("/new_post",methods =["POST","GET"])
def linkhandle(link):
    unique = ""
    index = link.find("v=")
    endindex = link.find("&")
    unique = link[index:endindex]



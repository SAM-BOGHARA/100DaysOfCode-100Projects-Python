from flask import Flask,render_template
import requests
NPOINT = "https://api.npoint.io/4cedc647e52fc72c2543"

posts = requests.get(NPOINT).json()
# print(posts)
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",all_posts = posts)

@app.route("/index.html")
def index():
    return render_template("index.html",all_posts = posts)

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/about.html")
def about():
    return render_template("about.html")



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html",post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request
import requests
import smtplib

EMAIL = "shubhamboghara444@gmail.com"
PASSWORD = ""

posts = requests.get("https://api.npoint.io/4cedc647e52fc72c2543").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        # print(data["name"] ,data["email"] ,data["phone"] ,data["message"])
        send_mail(data["name"] ,data["email"] ,data["phone"] ,data["message"])
        return render_template("contact.html" ,msg_sent = True)
    return render_template("contact.html",msg_sent = False)


def send_mail(name,email,phone,message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(EMAIL,EMAIL,email_message)

if __name__ == "__main__":
    app.run(debug=True)

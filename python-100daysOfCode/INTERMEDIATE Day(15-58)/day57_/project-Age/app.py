from flask import Flask,render_template
import requests
# GENDERIZE = "https://api.genderize.io?name=peter"

# AGIFY = "https://api.agify.io?name=michael"


app = Flask(__name__)


@app.route("/")
def hello():
    return "hello , go to /yourname"

@app.route("/<name>")
def guess(name):
    gender_response = requests.get(url = f"https://api.genderize.io?name={name}")
    data = gender_response.json()
    gender = data["gender"]

    age_response = requests.get(url = f"https://api.agify.io?name={name}")
    data = age_response.json()
    age = data["age"]
    
    return render_template("index.html",person_name = name,gender = gender,age = age)

@app.route("/blog")
def blog():
    response = requests.get(url = " https://api.npoint.io/c8e14db8b4c9f9d30897")
    data_response = response.json()
    print(data_response)

    return render_template("blog.html",all_data = data_response)

if __name__ == "__main__":
    app.run(debug=True)


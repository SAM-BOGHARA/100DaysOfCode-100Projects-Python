from flask import Flask,render_template
import random
import requests
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1,10)
    return render_template("index.html",num = random_number,year = current_year)


@app.route("/blog")
def blog():
    response = requests.get(url = " https://api.npoint.io/c8e14db8b4c9f9d30897")
    data_response = response.json()
    print(data_response)

    return render_template("blog.html",all_data = data_response)

if __name__ == "__main__":
    app.run(debug=True)


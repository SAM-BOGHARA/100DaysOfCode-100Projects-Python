from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Guess the number between 0 to 9</p>" \
        # "img src=''"


@app.route("/<int:number>")
def guess_number(number):
    if number > random_number:
        return "<h1 style='color : blue'>Too High,try Again."  \
               '<img src = https://media3.giphy.com/media/qs4ll1FSxKnNHeSmom/giphy.gif?cid=ecf05e47kciuelirhaq5rgrue9t7lkkizqhkvys9kkftzo6x&rid=giphy.gif&ct=g>'
    elif number < random_number:
        return "<h1 style='color : red'>Too Low,try Again." \
               '<img src = https://media3.giphy.com/media/qs4ll1FSxKnNHeSmom/giphy.gif?cid=ecf05e47kciuelirhaq5rgrue9t7lkkizqhkvys9kkftzo6x&rid=giphy.gif&ct=g>'
            
    else:
        return "<h1 style='color : green'>Correct." \
              '<img src = https://media2.giphy.com/media/8mONYL3lq2RtUf2V7C/giphy.gif?cid=ecf05e47akhpso4bce1qpccd5l2m0eb5ije14ib2ds2a1yt9&rid=giphy.gif&ct=g>'

if __name__ == "__main__":
    app.run(debug=True)

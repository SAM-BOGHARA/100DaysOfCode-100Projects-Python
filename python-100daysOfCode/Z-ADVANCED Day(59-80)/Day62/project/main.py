from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BnzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on Google maps (URL)', validators=[
                           DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8 AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 8 PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating', choices=[
                                "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"], validators=[DataRequired()])
    wifi_rating = SelectField('Strength rating', choices=[
                              "✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability', choices=[
                               "✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# # Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(f"{form.location.data}")
        with open("Z-ADVANCED\Day62\coffee-and-wifi\cafe-data.csv", mode="a",encoding="utf-8") as csv_file:
            csv_file.write(
                f"\n{form.cafe.data}|"f"{form.location.data}|"f"{form.open.data}|"f"{form.close.data}|"f"{form.coffee_rating.data}|"f"{form.wifi_rating.data}|"f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Z-ADVANCED\Day62\coffee-and-wifi\cafe-data.csv', newline='' , encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter='|')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

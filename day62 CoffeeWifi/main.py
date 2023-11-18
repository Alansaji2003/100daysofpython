import csv

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
# Import writer class from csv module
from csv import writer

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
# to load local css
app.static_folder = 'static'


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location_URL = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('open time', validators=[DataRequired()])
    close_time = StringField('close time', validators=[DataRequired()])
    my_choices = [('✘', '✘'), ('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                  ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')]
    coffee_rating = SelectField("Coffee Rating", choices=my_choices, validators=[DataRequired()])

    my_choices = [('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪️', '💪💪💪💪💪️')]
    wifi_rating = SelectField('Wifi rating', choices=my_choices, validators=[DataRequired()])

    my_choices = [('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')]
    power_outlet_rating = SelectField('Power outlet rating', choices=my_choices, validators=[DataRequired()])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit() and request.method == "POST":
        print("Valdation Success")

        # List that we want to add as a new row
        list_of_added_row = [form.cafe.data, form.Location_URL.data, form.open_time.data, form.close_time.data,
                             form.coffee_rating.data,
                             form.wifi_rating.data, form.power_outlet_rating.data]

        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open('cafe-data.csv', newline='', encoding="utf-8", mode='a') as f_object:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(list_of_added_row)

            # Close the file object
            f_object.close()
        msg = "Database successfully updated!."
        print(msg)
        return render_template('add.html', msg=msg, form=form)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            if len(row) != 0:
                list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

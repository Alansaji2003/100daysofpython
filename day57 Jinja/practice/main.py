# we use jinja for templating , we can use {{ }} to show that  it is python code in a html file
import datetime
import requests
from flask import Flask
from flask import render_template
import pandas as pd

df = pd.read_csv('static/country.csv')

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route('/guess/<name>')
def guess(name):
    agify_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = agify_response.json()
    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = genderize_response.json()
    nationalize_response = requests.get(f"https://api.nationalize.io?name={name}")
    nation_data = nationalize_response.json()
    code_nation = nation_data["country"][0]["country_id"]
    for code in df.code:
        if code_nation == code:
            country_name = df.loc[df['code'] == code_nation, 'country'].values[0]

    return render_template("guess.html", name=name, gender=gender_data["gender"], age=age_data["age"],
                           nation=country_name)


@app.route('/blog/<test>')
def get_blog(test):
    print(test)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_data = requests.get(blog_url).json()

    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)

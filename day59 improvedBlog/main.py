from flask import Flask, request
from flask import render_template
import requests
import smtplib

my_email = "mailalantest@gmail.com"
password = "xxxxx"

blog_data = requests.get("https://api.npoint.io/bab9e35579ca37b414d2").json()

app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template('index.html', blogs=blog_data)


@app.route('/<int:index>')
def show_post(index):
    requested_blog = None
    for blog in blog_data:
        if blog["id"] == index:
            requested_blog = blog
            return render_template('post.html', post=requested_blog)


@app.route('/about')
def show_about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def show_contact():
    if request.method == "POST":
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        connection.login(user=my_email, password=password)
        try:
            connection.sendmail(from_addr=my_email, to_addrs="rockstaralansaji@gmail.com",
                                msg=f"Subject:Someone said hi on your blog!\n\n "
                                    f"Name:{request.form['clientname']}\n"
                                    f"email:{request.form['clientemail']}\n"
                                    f"Phone:{request.form['clientph']}\n"
                                    f"Message:{request.form['clientmsg']}\n")
            connection.close()
        except:
            return '<div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3"><h1>Error ' \
                   'sending message!<h1/></div></div>'

        return '<div class="d-none" id="submitSuccessMessage"><div class="text-center mb-3"><div ' \
               'class="fw-bolder"><h1>Form submission successful!<h1/></div></div></div>'
    else:
        return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)

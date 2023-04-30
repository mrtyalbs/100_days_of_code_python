from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = 'YOUR OWN EMAIL ADDRESS'
OWN_PASSWORD = 'YOUR EMAIL ADDRESS PASSWORD'

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
posts_data = response.json()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', posts=posts_data)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        heading = "Contact Me"
        return render_template('contact.html', heading=heading)
    if request.method == 'POST':
        heading = "Successfully Sent Your Message"
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', heading=heading)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts_data:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)

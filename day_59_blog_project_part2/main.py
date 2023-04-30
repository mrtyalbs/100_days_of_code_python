from flask import Flask, render_template
import requests
import datetime

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
posts_data = response.json()

date_time = datetime.datetime.now().date()
print(date_time)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', posts=posts_data)


@app.route('/contact')
def contact():
    return render_template('contact.html')


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


if __name__ == '__main__':
    app.run(debug=True)

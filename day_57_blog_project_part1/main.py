from flask import Flask, render_template
import requests
from post import Post


response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts_data = response.json()

posts_list = []

for post in posts_data:
    post_object = Post(post["id"], post["title"],
                       post["subtitle"], post["body"])
    posts_list.append(post_object)


print(posts_list)
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts_list)


@app.route("/post/<int:blog_id>")
def read_post(blog_id):
    requested_post = None
    for blog_post in posts_list:
        if blog_id == blog_post.post_id:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

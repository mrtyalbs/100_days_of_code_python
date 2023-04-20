from flask import Flask, render_template
import random

app = Flask(__name__)

# Generate a number between 0-9
random_number = random.randint(0, 9)
print(random_number)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:guess>")
def guess_number(guess):
    if random_number > guess:
        return render_template("high.html")
    elif random_number < guess:
        return render_template("low.html")
    else:
        return render_template("found.html")


if __name__ == "__main__":
    app.run(debug=True)




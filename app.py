from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", current_year=2025)

@app.route("/about")
def about():
    return render_template("about.html", current_year=2025)

@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=2025)

if __name__ == "__main__":
    app.run(debug=True)

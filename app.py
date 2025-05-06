from flask import Flask, render_template, redirect, url_for,request

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def base():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/hebergement")
def hebergement():
    return render_template("hebergements.html")


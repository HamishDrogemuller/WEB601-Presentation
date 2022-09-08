from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World! <h1> Welcome! </h1>"

@app.route('/about')
def about():
    return "I am a basic flask App!"

@app.route('/<name>')
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
    

if __name__ == "__main__":
    app.run(debug=True)
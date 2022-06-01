from re import template
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return "coba flask"

# membuat halaman lain 
@app.route("/profil")
def profil():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()



from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def profil():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

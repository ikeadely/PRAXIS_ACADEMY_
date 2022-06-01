from flask import Flask
from flask_mongoengine import Mongoengine

app = Flask_(__name__)
db = Mongoengine()
db.init_app(app)

if __name__ == '__main__':
    app.run()
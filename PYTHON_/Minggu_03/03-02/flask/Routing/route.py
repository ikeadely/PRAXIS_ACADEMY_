from flask import Flask
app = Flask(__name__)

@app.route('/Hello')
def hello_world():
    return 'Hello ADel'

def hello_world():
    return 'Hello ADel, apakabar hari ini'
app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
    app.run()


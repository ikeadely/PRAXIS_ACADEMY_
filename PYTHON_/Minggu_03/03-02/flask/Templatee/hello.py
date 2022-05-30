from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#    return '<html><body><h1>Hello World</h1></body></html>'

# if __name__ == '__main__':
#    app.run(debug = True)

# result
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def calculate():
    text = request.form['text']
    counter = len(text.split())
    return render_template('calculate.html', counter=counter)


if __name__ == '__main__':
    app.run(debug=True)

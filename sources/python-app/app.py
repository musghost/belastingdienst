from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    age = request.form['age']
    return render_template('greeting.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

FlaskInstrumentor().instrument_app(app)


# Configure MySQL
app.config['MYSQL_HOST'] =os.environ.get("MYSQL_HOST", "mysql-service")
app.config['MYSQL_USER'] = os.environ.get("MYSQL_USER", "user")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_PASSWORD", "")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_DB", "flask_example")
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

country_map = {
    'Amsterdam': 'The Netherlands',
    'New York': 'United States',
    'Berlin': 'Germany',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']

    country = country_map[city]

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user (name, age, country) VALUES (%s, %s, %s)', (name, age, country))
    mysql.connection.commit()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    cur.close()
    return render_template('greeting.html', data=data)

    


if __name__ == '__main__':
    app.run(host="0.0.0.0")
from flask import Flask
from flask_mysql import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'eunice'
app.config['MYSQL_DATABASE_PASSWORD'] = 'example'
app.config['MYSQL_DATABASE_DB'] = 'flaskdb'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def main():
    return "Welcome!"


@app.route('/how are you')
def hello():
    return 'I am good, how about you?'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

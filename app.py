"""
simple flask app
"""

import os
from flask import Flask, render_template
from flask_mysqldb import MySQL

# App Configurations
app = Flask(__name__)
filedir = os.path.dirname(__file__)
mysql = MySQL()

# MySQL configurations
app.config['CLOUDSQL_CONNECTION_NAME'] = os.environ.get('CLOUDSQL_CONNECTION_NAME')
app.config['CLOUDSQL_USER'] = os.environ.get('CLOUDSQL_USER')
app.config['CLOUDSQL_PASSWORD'] = os.environ.get('CLOUDSQL_PASSWORD')
app.config['CLOUDSQL_DATABASE'] = os.environ.get('CLOUDSQL_DATABASE')
mysql.init_app(app)


def connect_to_cloudsql():
    """connect_to_cloudsql"""
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        return True
    else:
        return False

@app.route("/")
def main():
    """here"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=8080)


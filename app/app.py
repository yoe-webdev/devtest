from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def elevators_tbl() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'elevators_db'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM elevators_tbl')
    results = [k for k in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def indexk() -> str:
    return json.dumps({'elevators_tbl': elevators_tbl()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

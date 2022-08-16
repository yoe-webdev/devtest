from typing import List, Dict
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector



app = Flask(__name__)
app.secret_key = 'many random bytes'


config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'crud'
    }

@app.route('/')
def Index():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM records')
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return render_template('index2.html', records = records)



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        elevator_id = request.form['elevator_id']
        number_of_floors = request.form['number_of_floors']
        current_floor = request.form['current_floor']
        capacity = request.form['capacity']
        occupancy = request.form['occupancy']
        is_moving = request.form['is_moving']
        next_stop_floor = request.form['next_stop_floor']
        resting_floor = request.form['resting_floor']
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO records (elevator_id, number_of_floors, current_floor, capacity, occupancy, is_moving, next_stop_floor, resting_floor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (elevator_id, number_of_floors, current_floor, capacity, occupancy, is_moving, next_stop_floor, resting_floor))
        connection.commit()

        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM records WHERE id=%s", (id_data,))
    connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        elevator_id = request.form['elevator_id']
        number_of_floors = request.form['number_of_floors']
        current_floor = request.form['current_floor']
        capacity = request.form['capacity']
        occupancy = request.form['occupancy']
        is_moving = request.form['is_moving']
        next_stop_floor = request.form['next_stop_floor']
        resting_floor = request.form['resting_floor']
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("""
               UPDATE records
               SET elevator_id = %s, number_of_floors=%s, current_floor=%s, capacity=%s, occupancy=%s, is_moving=%s, next_stop_floor=%s, resting_floor=%s
               WHERE id=%s
            """, (elevator_id, number_of_floors, current_floor, capacity, occupancy, is_moving, next_stop_floor, resting_floor, id_data))
        flash("Data Updated Successfully")
        connection.commit()
        return redirect(url_for('Index'))



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

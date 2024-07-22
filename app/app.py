import os 
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
             host='localhost',
             database='factory', 
             user='postgres',
             password='postgres'
    )
    return conn 

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    employees = cur.fetchall() 
    cur.close()
    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        emp_id = int(request.form['emp_id'])
        emp_fname = request.form['emp_fname']
        emp_lname = request.form['emp_lname']
        emp_dob = request.form['emp_dob']
        emp_doj = request.form['emp_doj']
        salary = request.form['salary']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO employees (emp_id, emp_fname, emp_lname, emp_dob, emp_doj, salary)'
                    'VALUES(%s, %s, %s, %s, %s, %s)',
                    (emp_id, emp_fname, emp_lname, emp_dob, emp_doj, salary))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')


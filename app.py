from flask import Flask, request
import psycopg2

app = Flask("__name_")

@app.route('/', methods=['POST'])
def insertUser():
    empId = request.json['emp_id']
    time = request.json['time']
    conn = psycopg2.connect(
        host = 'bvqqudtar2kprjtlsiwj-postgresql.services.clever-cloud.com',
        dbname = 'bvqqudtar2kprjtlsiwj',
        user = 'u2ruldyvqwaw62qxkyv8',
        password = 'vDCByOlfYRCKl2XcBrNb',
        port = 5432)
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM charts WHERE emp_id = '" + empId + "' AND end_work IS NULL;")
    isLogged = cur.fetchone()
    if isLogged is not None: #zalogowany
        cur.execute("UPDATE charts SET end_work = '" + time + "' WHERE end_work IS NULL AND emp_id = '" + empId + "';")
    else:                    #wylogowany
        cur.execute("INSERT INTO charts(emp_id, start_work) VALUES('" + empId + "', '" + time + "');")
    conn.commit()
    cur.close()
    conn.close()
    return "<p>Data is updated</p>"
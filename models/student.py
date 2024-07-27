from flask import current_app
from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

class Student:
    @staticmethod
    def get_all_students():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        cur.close()
        return students

    @staticmethod
    def get_student_by_id(student_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = cur.fetchone()
        cur.close()
        return student

    @staticmethod
    def add_student(name, email):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def update_student(student_id, name, email):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE students SET name = %s, email = %s WHERE id = %s", (name, email, student_id))
        mysql.connection.commit()
        cur.close()

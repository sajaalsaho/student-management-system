import sqlite3
from .db import get_db


def add_student(name, number):
    name = (name or "").strip()
    number = (number or "").strip()
    if not name or not number:
        raise ValueError("Ad ve öğrenci numarası boş olamaz.")
    db = get_db()
    try:
        db.execute("INSERT INTO students (name, number) VALUES (?, ?)", (name, number))
        db.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Bu öğrenci numarası zaten kayıtlı.")


def list_students():
    return get_db().execute("SELECT * FROM students ORDER BY name").fetchall()


def delete_student(student_id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id = ?", (student_id,))
    db.commit()
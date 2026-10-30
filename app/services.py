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
def add_course(code, name):
    code = (code or "").strip().upper()
    name = (name or "").strip()
    if not code or not name:
        raise ValueError("Ders kodu ve adı boş olamaz.")
    db = get_db()
    try:
        db.execute("INSERT INTO courses (code, name) VALUES (?, ?)", (code, name))
        db.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Bu ders kodu zaten kayıtlı.")


def list_courses():
    return get_db().execute("SELECT * FROM courses ORDER BY code").fetchall()


def set_grade(student_id, course_id, grade):
    try:
        grade = float(grade)
    except (TypeError, ValueError):
        raise ValueError("Not bir sayı olmalı.")
    if not 0 <= grade <= 100:
        raise ValueError("Not 0 ile 100 arasında olmalı.")
    db = get_db()
    try:
        db.execute(
            """INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)
               ON CONFLICT(student_id, course_id) DO UPDATE SET grade = excluded.grade""",
            (student_id, course_id, grade),
        )
        db.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Öğrenci veya ders bulunamadı.")


def list_grades():
    return get_db().execute(
        """SELECT s.name AS student, c.name AS course, g.grade
           FROM grades g
           JOIN students s ON s.id = g.student_id
           JOIN courses c ON c.id = g.course_id
           ORDER BY s.name, c.name"""
    ).fetchall()


def calculate_average(student_id):
    row = get_db().execute(
        "SELECT AVG(grade) AS avg FROM grades WHERE student_id = ?", (student_id,)
    ).fetchone()
    return round(row["avg"], 2) if row["avg"] is not None else None
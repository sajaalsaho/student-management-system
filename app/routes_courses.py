from flask import Blueprint, flash, redirect, render_template, request, url_for
from . import services

bp = Blueprint("courses", __name__)


@bp.route("/courses", methods=["GET", "POST"])
def courses():
    if request.method == "POST":
        try:
            services.add_course(request.form.get("code"), request.form.get("name"))
            flash("Ders eklendi.")
        except ValueError as e:
            flash(str(e))
        return redirect(url_for("courses.courses"))
    return render_template("courses.html", courses=services.list_courses())


@bp.route("/grades", methods=["GET", "POST"])
def grades():
    if request.method == "POST":
        try:
            services.set_grade(
                request.form.get("student_id", type=int),
                request.form.get("course_id", type=int),
                request.form.get("grade"),
            )
            flash("Not kaydedildi.")
        except ValueError as e:
            flash(str(e))
        return redirect(url_for("courses.grades"))
    students = services.list_students()
    averages = [
        {"name": s["name"], "average": services.calculate_average(s["id"])}
        for s in students
    ]
    return render_template(
        "grades.html",
        students=students,
        courses=services.list_courses(),
        grades=services.list_grades(),
        averages=averages,
    )
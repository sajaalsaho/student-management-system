from flask import current_app
from flask import Blueprint, flash, redirect, render_template, request, url_for
from . import services

bp = Blueprint("students", __name__)


@bp.route("/")
def index():
    return redirect(url_for("students.students"))


@bp.route("/students", methods=["GET", "POST"])
def students():
    if request.method == "POST":
        try:
            services.add_student(request.form.get("name"), request.form.get("number"))
            flash("Öğrenci eklendi.")
            current_app.logger.info("Ogrenci eklendi")            
        except ValueError as e:
            flash(str(e))
        return redirect(url_for("students.students"))
    return render_template("students.html", students=services.list_students())


@bp.route("/students/<int:student_id>/delete", methods=["POST"])
def delete(student_id):
    services.delete_student(student_id)
    flash("Öğrenci silindi.")
    current_app.logger.info("Ogrenci silindi: id=%s", student_id)    
    return redirect(url_for("students.students"))

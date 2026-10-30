from flask import Blueprint, render_template
from . import services

bp = Blueprint("report", __name__)


@bp.route("/report")
def report():
    return render_template("report.html", report=services.get_report())
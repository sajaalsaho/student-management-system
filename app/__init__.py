import logging
import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)

    app.config["DATABASE"] = os.environ.get(
        "DATABASE_PATH",
        os.path.normpath(os.path.join(app.root_path, "..", "students.db")),
    )

    secret = os.environ.get("SECRET_KEY")
    if not secret:
        app.logger.warning("SECRET_KEY tanimli degil, gelistirme anahtari kullaniliyor.")
        secret = "dev-secret"
    app.config["SECRET_KEY"] = secret

    if test_config:
        app.config.update(test_config)

    from . import db
    db.init_app(app)

    from .routes_students import bp as students_bp
    app.register_blueprint(students_bp)

    from .routes_courses import bp as courses_bp
    app.register_blueprint(courses_bp)

    from .routes_report import bp as report_bp
    app.register_blueprint(report_bp)

    from .routes_health import bp as health_bp
    app.register_blueprint(health_bp)

    with app.app_context():
        db.init_db()

    app.logger.info("Uygulama baslatildi")
    return app
from flask import Blueprint, current_app, jsonify
from .db import get_db

bp = Blueprint("health", __name__)


@bp.route("/health")
def health():
    try:
        get_db().execute("SELECT 1")
        current_app.logger.info("Health check basarili")
        return jsonify(status="ok"), 200
    except Exception:
        current_app.logger.exception("Health check basarisiz")
        return jsonify(status="error"), 503
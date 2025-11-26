from flask import Blueprint, render_template
from .storage import storage


audit_bp = Blueprint("audit", __name__, url_prefix="/audit")


@audit_bp.route("/")
def dashboard():
    return render_template("audit.html", logs=storage.audit_logs)

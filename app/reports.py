from flask import Blueprint, redirect, render_template, request, url_for
from .storage import storage


reports_bp = Blueprint("reports", __name__, url_prefix="/reports")


@reports_bp.route("/")
def dashboard():
    return render_template("reports.html", reports=storage.reports.values())


@reports_bp.route("/generate", methods=["POST"])
def generate():
    title = request.form["title"]
    version = request.form["version"]
    content = request.form["content"]
    storage.create_report(title, content, version)
    return redirect(url_for("reports.dashboard"))


@reports_bp.route("/approve", methods=["POST"])
def approve():
    title = request.form["title"]
    storage.approve_report(title)
    return redirect(url_for("reports.dashboard"))

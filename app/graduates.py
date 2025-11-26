from flask import Blueprint, redirect, render_template, request, url_for
from .storage import storage


graduates_bp = Blueprint("graduates", __name__, url_prefix="/graduates")


@graduates_bp.route("/")
def dashboard():
    return render_template("graduates.html", graduates=storage.graduates.values())


@graduates_bp.route("/add", methods=["POST"])
def add_graduate():
    name = request.form["name"]
    year = int(request.form["year"])
    employment_status = request.form["employment_status"]
    employer = request.form["employer"]
    storage.add_graduate(name, year, employment_status, employer)
    return redirect(url_for("graduates.dashboard"))

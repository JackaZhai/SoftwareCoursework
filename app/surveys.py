from flask import Blueprint, redirect, render_template, request, url_for
from .storage import storage


surveys_bp = Blueprint("surveys", __name__, url_prefix="/surveys")


@surveys_bp.route("/")
def dashboard():
    return render_template("surveys.html", surveys=storage.surveys.values())


@surveys_bp.route("/add", methods=["POST"])
def add_survey():
    title = request.form["title"]
    edition = request.form["edition"]
    questions = [q.strip() for q in request.form["questions"].split("\n") if q.strip()]
    storage.add_survey(title, edition, questions)
    return redirect(url_for("surveys.dashboard"))


@surveys_bp.route("/respond", methods=["POST"])
def respond():
    survey_title = request.form["survey_title"]
    name = request.form["name"]
    status = request.form["status"]
    storage.collect_response(survey_title, {"name": name, "status": status})
    return redirect(url_for("surveys.dashboard"))

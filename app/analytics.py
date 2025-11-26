from flask import Blueprint, render_template
from .storage import storage
from .metrics import compute_employment_metrics


analytics_bp = Blueprint("analytics", __name__, url_prefix="/analytics")


@analytics_bp.route("/")
def dashboard():
    metrics = compute_employment_metrics()
    survey_participation = {
        survey.title: len(survey.responses) for survey in storage.surveys.values()
    }
    return render_template(
        "analytics.html",
        metrics=metrics,
        survey_participation=survey_participation,
    )

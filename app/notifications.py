from flask import Blueprint, redirect, render_template, request, url_for
from .storage import storage


notifications_bp = Blueprint("notifications", __name__, url_prefix="/notifications")


@notifications_bp.route("/")
def dashboard():
    return render_template("notifications.html", notifications=storage.notifications)


@notifications_bp.route("/send", methods=["POST"])
def send():
    channel = request.form["channel"]
    recipient = request.form["recipient"]
    content = request.form["content"]
    storage.send_notification(channel, recipient, content)
    return redirect(url_for("notifications.dashboard"))

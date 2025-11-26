from flask import Blueprint, redirect, render_template, request, url_for
from .storage import storage


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/")
def dashboard():
    return render_template("auth.html", users=storage.users.values())


@auth_bp.route("/add", methods=["POST"])
def add_user():
    username = request.form["username"]
    role = request.form["role"]
    mfa_enabled = bool(request.form.get("mfa"))
    storage.add_user(username, role, mfa_enabled)
    return redirect(url_for("auth.dashboard"))

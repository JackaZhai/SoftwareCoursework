from .storage import storage


def create_app():
    from flask import Flask, render_template

    from .audit import audit_bp
    from .auth import auth_bp
    from .graduates import graduates_bp
    from .notifications import notifications_bp
    from .reports import reports_bp
    from .surveys import surveys_bp
    from .analytics import analytics_bp

    app = Flask(__name__)
    app.secret_key = "graduatetracker-demo-key"

    @app.route("/")
    def index():
        return render_template(
            "index.html",
            users=storage.users,
            graduates=storage.graduates,
            surveys=storage.surveys,
            notifications=storage.notifications,
            logs=storage.audit_logs,
        )

    app.register_blueprint(auth_bp)
    app.register_blueprint(graduates_bp)
    app.register_blueprint(surveys_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(audit_bp)

    return app

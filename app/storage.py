from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass
class User:
    username: str
    role: str
    mfa_enabled: bool = False


@dataclass
class Graduate:
    name: str
    year: int
    employment_status: str
    employer: str
    history: List[str] = field(default_factory=list)
    attachments: List[str] = field(default_factory=list)


@dataclass
class Survey:
    title: str
    edition: str
    questions: List[str]
    responses: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class Notification:
    channel: str
    recipient: str
    content: str
    status: str
    timestamp: datetime


@dataclass
class Report:
    title: str
    content: str
    version: str
    approved: bool = False


class InMemoryStorage:
    def __init__(self) -> None:
        self.users: Dict[str, User] = {
            "admin": User(username="admin", role="Administrator", mfa_enabled=True),
            "auditor": User(username="auditor", role="Auditor", mfa_enabled=False),
        }
        self.graduates: Dict[str, Graduate] = {
            "Alice": Graduate(
                name="Alice",
                year=2022,
                employment_status="Employed",
                employer="TechCorp",
                history=["2023-01-02 Joined TechCorp"],
                attachments=["offer_letter.pdf"],
            )
        }
        self.surveys: Dict[str, Survey] = {
            "就业跟踪2024Q1": Survey(
                title="就业跟踪2024Q1",
                edition="2024Q1",
                questions=["目前就业状态?", "年薪范围?"],
                responses=[{"name": "Alice", "status": "Employed"}],
            )
        }
        self.notifications: List[Notification] = []
        self.audit_logs: List[str] = []
        self.reports: Dict[str, Report] = {}

    def log(self, message: str) -> None:
        entry = f"{datetime.utcnow().isoformat()}Z - {message}"
        self.audit_logs.append(entry)

    def add_user(self, username: str, role: str, mfa_enabled: bool) -> User:
        user = User(username=username, role=role, mfa_enabled=mfa_enabled)
        self.users[username] = user
        self.log(f"User created: {username} with role {role}")
        return user

    def add_graduate(
        self, name: str, year: int, employment_status: str, employer: str
    ) -> Graduate:
        grad = Graduate(
            name=name,
            year=year,
            employment_status=employment_status,
            employer=employer,
            history=[f"{datetime.utcnow().date()} status recorded"],
        )
        self.graduates[name] = grad
        self.log(f"Graduate added: {name} ({year})")
        return grad

    def add_survey(self, title: str, edition: str, questions: List[str]) -> Survey:
        survey = Survey(title=title, edition=edition, questions=questions)
        self.surveys[title] = survey
        self.log(f"Survey created: {title} / {edition}")
        return survey

    def collect_response(self, survey_title: str, response: Dict[str, str]) -> None:
        survey = self.surveys[survey_title]
        survey.responses.append(response)
        self.log(f"Survey response collected for {survey_title}")

    def send_notification(self, channel: str, recipient: str, content: str) -> Notification:
        notification = Notification(
            channel=channel,
            recipient=recipient,
            content=content,
            status="SENT",
            timestamp=datetime.utcnow(),
        )
        self.notifications.append(notification)
        self.log(f"Notification sent to {recipient} via {channel}")
        return notification

    def create_report(self, title: str, content: str, version: str) -> Report:
        report = Report(title=title, content=content, version=version)
        self.reports[title] = report
        self.log(f"Report draft created: {title} v{version}")
        return report

    def approve_report(self, title: str) -> None:
        if title in self.reports:
            self.reports[title].approved = True
            self.log(f"Report approved: {title}")


storage = InMemoryStorage()

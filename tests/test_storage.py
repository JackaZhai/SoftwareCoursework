import os
import sys

sys.path.append(os.path.abspath("."))

from app.storage import InMemoryStorage, storage
from app.metrics import compute_employment_metrics


def test_add_user_and_log():
    store = InMemoryStorage()
    store.add_user("tester", "QA", True)
    assert "tester" in store.users
    assert any("tester" in log for log in store.audit_logs)


def test_add_graduate_updates_metrics():
    store = InMemoryStorage()
    store.add_graduate("Bob", 2023, "待就业", "-")
    metrics = {
        "counts": {},
        "distribution": {},
        "total_graduates": 0,
    }
    # monkey patch storage used by analytics function
    original_graduates = storage.graduates
    storage.graduates = store.graduates
    try:
        metrics = compute_employment_metrics()
    finally:
        storage.graduates = original_graduates
    assert metrics["counts"]["待就业"] == 1
    assert metrics["total_graduates"] >= 1


def test_survey_response_flow():
    store = InMemoryStorage()
    store.add_survey("测试问卷", "v1", ["Q1"])
    store.collect_response("测试问卷", {"name": "张三", "status": "Employed"})
    assert len(store.surveys["测试问卷"].responses) == 1


def test_report_approval():
    store = InMemoryStorage()
    store.create_report("年度报告", "摘要", "1.0")
    store.approve_report("年度报告")
    assert store.reports["年度报告"].approved is True

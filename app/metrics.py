from collections import Counter
from .storage import storage


def compute_employment_metrics():
    status_counts = Counter([g.employment_status for g in storage.graduates.values()])
    total = sum(status_counts.values()) or 1
    distribution = {k: round(v / total, 2) for k, v in status_counts.items()}
    return {
        "counts": status_counts,
        "distribution": distribution,
        "total_graduates": total,
    }

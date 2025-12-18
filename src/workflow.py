from __future__ import annotations
from datetime import datetime
from typing import Dict, Any


def build_task_title(req: Dict[str, Any]) -> str:
    return f"Leave Request: {req['employee_name']} ({req['leave_type']})"


def build_task_description(req: Dict[str, Any]) -> str:
    return (
        f"🧾 **Leave Request Details**\n\n"
        f"- Employee: {req['employee_name']} ({req['employee_email']})\n"
        f"- Department: {req['employee_department']}\n"
        f"- Manager: {req['manager_name']}\n"
        f"- Leave Type: {req['leave_type']}\n"
        f"- Dates: {req['start_date']} to {req['end_date']}\n"
        f"- Reason: {req.get('reason','')}\n"
        f"- Notes: {req.get('notes','')}\n\n"
        f"📌 Status: **{req.get('status','Pending')}**\n\n"
        f"✅ Approval Action:\n"
        f"- Approve or Reject this request in ClickUp.\n"
        f"- If more info is needed, set status to **Needs Info**.\n"
    )


def validate_request(req: Dict[str, Any]) -> None:
    required = [
        "employee_name", "employee_email", "employee_department",
        "manager_name", "leave_type", "start_date", "end_date"
    ]
    missing = [k for k in required if k not in req or not str(req[k]).strip()]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    # Basic date validation
    start = datetime.strptime(req["start_date"], "%Y-%m-%d").date()
    end = datetime.strptime(req["end_date"], "%Y-%m-%d").date()
    if end < start:
        raise ValueError("end_date must be the same as or after start_date")


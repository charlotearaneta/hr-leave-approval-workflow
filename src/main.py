from __future__ import annotations

import argparse
import os
import json
from pathlib import Path
from dotenv import load_dotenv

from clickup_client import ClickUpClient
from workflow import build_task_title, build_task_description, validate_request

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"


def main():
    parser = argparse.ArgumentParser(description="HR Leave Approval Workflow (MVP)")
    parser.add_argument("--request", required=True, help="Path to leave request JSON (e.g., data/leave_request.json)")
    args = parser.parse_args()

    api_token = os.getenv("CLICKUP_API_TOKEN")
    list_id = os.getenv("CLICKUP_LIST_ID")
    manager_assignee_id = os.getenv("MANAGER_ASSIGNEE_ID") or None
    default_priority = os.getenv("DEFAULT_PRIORITY")

    if not api_token:
        raise RuntimeError("Missing CLICKUP_API_TOKEN in .env")
    if not list_id:
        raise RuntimeError("Missing CLICKUP_LIST_ID in .env")

    priority = int(default_priority) if default_priority and default_priority.isdigit() else None

    req_path = Path(args.request)
    if not req_path.exists():
        raise FileNotFoundError(f"Request file not found: {req_path}")

    req = json.loads(req_path.read_text(encoding="utf-8"))
    validate_request(req)

    title = build_task_title(req)
    description = build_task_description(req)

    client = ClickUpClient(api_token)
    task = client.create_task(
        list_id=list_id,
        name=title,
        description=description,
        assignee_id=manager_assignee_id,
        priority=priority,
        tags=["leave", "hr-workflow"]
    )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = {
        "created_task": {
            "id": task.get("id"),
            "name": task.get("name"),
            "url": task.get("url")
        },
        "request": req
    }

    out_path = RESULTS_DIR / f"leave_request_{req['employee_name'].replace(' ', '_').lower()}.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("✅ Leave request created in ClickUp!")
    print(f"🔗 Task: {task.get('url')}")
    print(f"📦 Log saved: {out_path}")


if __name__ == "__main__":
    main()


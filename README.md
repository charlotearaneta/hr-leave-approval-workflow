# ✅ HR Leave Approval Workflow (Python + ClickUp API)

A lightweight HR-Tech automation workflow that creates and routes leave requests in ClickUp using Python.  
This project demonstrates how HR processes can be converted into scalable automation systems to improve efficiency, consistency, and accountability.

## 🚀 Features
- Create leave requests from structured JSON input  
- Auto-generate a ClickUp task with complete leave details  
- Assign requests to a manager (optional)  
- Save execution logs to `results/`  

## ⚙️ Quick Start (MVP)

1. Clone the repo  
2. Install dependencies:
```bash
pip install -r requirements.txt

```
3. Create .env from .env.example and add:

```env

CLICKUP_API_TOKEN=your_clickup_token
CLICKUP_LIST_ID=your_clickup_list_id

```

4. Run

```bash

python src/main.py --request data/leave_request.sample.json


```

✅ The script creates a ClickUp task and saves a run log in results/.

---

## 🗺 Roadmap

Phase 1: MVP leave request routing ✅

Phase 2: Approve/Reject status sync + decision logging

Phase 3: Leave balance checks + policy validation

Phase 4: Calendar integration + email notifications

---


## 📬� Contact
👩‍💻 Created by: **Charlote Araneta**

🔗 LinkedIn: https://www.linkedin.com/in/charlotearaneta

🌐 Portfolio: https://charlotearaneta.github.io

---

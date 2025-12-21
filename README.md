# ✅ HR Leave Approval Workflow 

### *HR leave request and approval automation using Python and ClickUp*


The **HR Leave Approval Workflow** is a Python-based HR Tech automation project that streamlines employee leave requests and approval processes by converting structured leave data into actionable approval tasks in ClickUp.

This project demonstrates how **HR processes** can be combined with **Python automation and API integration** to reduce administrative workload, improve consistency, and preserve human decision-making in people management.

---

## 🌟 Overview

Leave approvals are often handled through emails, chats, or spreadsheets—leading to delays, poor visibility, and inconsistent documentation. This system automates the operational side of leave management while keeping approval decisions firmly in the hands of managers.

The workflow focuses on:
- Standardized leave request submission
- Clear approval routing
- Audit-friendly documentation
- Scalable HR operations

---

## 📂 Project Structure

```text
hr-leave-approval-workflow/
│
├─ src/
│ ├─ main.py # Main workflow entry point
│ ├─ clickup_client.py # ClickUp API client
│ └─ workflow.py # Validation and business logic
│
├─ data/
│ ├─ leave_request.sample.json # Sample leave request input
│ └─ policy.json # Basic leave policy rules
│
├─ results/
│ └─ .gitkeep # Stores execution logs
│
├─ .env.example # Environment variable template
├─ requirements.txt # Python dependencies
└─ README.md

```

---


## 🚀 Features
### ✔ Structured Leave Request Automation
Converts JSON-based leave requests into approval tasks in ClickUp.

### ✔ Manager Routing
Routes requests to the appropriate approver while keeping decision-making human-led.

### ✔ Validation & Business Rules
Validates required fields and leave dates before submission.

### ✔ Execution Logging
Stores request and task metadata in local logs for traceability.

### ✔ Modular & Extendable
Designed to support future enhancements such as policy enforcement and notifications.

---

## 🧠 How It Works

### 1. Leave Request Input
HR or employees submit leave requests using a structured JSON file.

### 2. Validation
The system checks required fields and validates date ranges.

### 3. Task Creation
A ClickUp task is created with complete leave details and approval instructions.

### 4. Logging
Each execution is saved as a JSON log file in the `results/` directory.

---

## 📥 Input Example (`leave_request.sample.json`)

```json
{
  "employee_name": "James Walker",
  "employee_email": "james.walker@email.com",
  "employee_department": "IT",
  "manager_name": "Sarah Lee",
  "leave_type": "Annual Leave",
  "start_date": "2026-02-10",
  "end_date": "2026-02-12",
  "reason": "Family commitment",
  "notes": "I will hand over tasks before leave.",
  "status": "Pending"
}


 ```

---


## 🛠 Tech Stack

- **Python**

- **ClickUp API**

- **Requests**

- **python-dotenv**

- **JSON-based configuration**

- **VS Code & GitHub**

---

## ⚙️ Setup Instructions

1. Clone the repo
```bash
git clone https://github.com/yourusername/hr-leave-approval-workflow.git
cd hr-leave-approval-workflow

```

2. Install dependencies:
```bash
pip install -r requirements.txt

```
3. Create .env from .env.example and add:

```env

CLICKUP_API_TOKEN=your_clickup_token
CLICKUP_LIST_ID=your_clickup_list_id

```

4. Run the workflow

```bash

python src/main.py --request data/leave_request.sample.json


```

✅ The script creates a ClickUp task and saves a run log in results/.

---

## 🖼 Demo

This project runs locally using authenticated API connections.
Sample outputs and execution logs are stored in the results/ folder.

---


## 🗺 Roadmap

Phase 1: MVP leave request routing 

Phase 2: Approve/Reject status sync + decision logging

Phase 3: Leave balance checks + policy validation

Phase 4: Calendar integration + email notifications

---

## 🎯 What I Learned

Building this system reinforced key HR-Tech principles:

- Translating HR processes into executable workflows

- Designing automation that supports—not replaces—human decisions

- Working with external APIs securely and responsibly

- Creating scalable, modular automation systems

- Applying technology to solve real operational HR challenges
  

---

## 🌍 Long-Term Vision

This project serves as a foundation for a broader HR operations automation platform that could support:

- Approval status synchronization  
- Leave balance validation  
- Calendar and email notifications  
- Integration with HRIS and ATS systems  
- End-to-end employee lifecycle automation  

The long-term goal is to empower HR teams to focus on people not paperwork.

---


## 📬 Contact
👩‍💻 Created by: **Charlote Araneta**

🔗 LinkedIn: https://www.linkedin.com/in/charlotearaneta

🌐 Portfolio: https://charlotearaneta.github.io

---

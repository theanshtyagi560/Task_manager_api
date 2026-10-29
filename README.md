# 📋 Task Manager REST API — Week 3 Internship Project

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14+-red.svg?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Tests](https://img.shields.io/badge/Tests-10%20Passed%20%E2%9C%94-success.svg)](https://github.com/)
[![Postman](https://img.shields.io/badge/Postman-Collection%20v2.1-orange.svg?logo=postman&logoColor=white)](postman_collection.json)

A production-ready **Task Manager RESTful API** developed with **Django** and **Django REST Framework (DRF)**. Built as part of the Backend Development Internship (Week 3), advancing from Week 1 (CLI OOP) and Week 2 (Flask Web App with Auth).

---

## 🌟 Key Features

- **🔐 Token Authentication:** Stateless token-based auth (`rest_framework.authtoken`) for secure API client communication.
- **🛡️ Strict User Isolation:** Users can strictly query, modify, or delete only their own tasks. Cross-user access attempts safely return `404 Not Found`.
- **⚡ Full CRUD Operations:** Complete task management lifecycle across standard HTTP verbs (`GET`, `POST`, `PATCH`, `DELETE`).
- **🔍 Query Parameter Filtering:** Filter tasks effortlessly using query params (e.g. `GET /api/tasks/?status=done`).
- **🧪 Automated Test Suite:** 10 comprehensive tests covering registration, login, authorization headers, data isolation, and validation.
- **📦 Ready-to-Use Postman Collection:** Includes environment variables (`{{base_url}}`, `{{token}}`, `{{task_id}}`) and auto-token extraction scripts.
- **🚀 One-Step Verification:** Built-in `demo_api.py` script to test every endpoint with colorful terminal status output.

---

## 📡 API Endpoints Reference

| Method | Endpoint | Auth | Request Body | Status Code | Purpose |
|---|---|:---:|---|:---:|---|
| `POST` | `/api/register/` | ❌ None | `{"username", "email", "password"}` | `201 Created` | Create new account & receive auth token |
| `POST` | `/api/login/` | ❌ None | `{"username", "password"}` | `200 OK` | Authenticate user & return token |
| `GET` | `/api/tasks/` | 🔒 Token | None | `200 OK` | List authenticated user's tasks |
| `GET` | `/api/tasks/?status=<val>` | 🔒 Token | None | `200 OK` | Filter user tasks (`todo`, `in_progress`, `done`) |
| `POST` | `/api/tasks/` | 🔒 Token | `{"title", "description", "status", "due_date"}` | `201 Created` | Create a new task linked to current user |
| `GET` | `/api/tasks/<id>/` | 🔒 Token | None | `200 OK` | Retrieve single task (404 if not yours) |
| `PATCH` / `PUT` | `/api/tasks/<id>/` | 🔒 Token | Partial or full task JSON | `200 OK` | Update task details |
| `DELETE` | `/api/tasks/<id>/` | 🔒 Token | None | `204 No Content` | Delete a task |

> 🔒 **Authorization Header Format:**  
> `Authorization: Token <your_token_key>`

---

## 📂 Project Directory Structure

```text
task-manager-api/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # DRF & TokenAuthentication settings
│   ├── urls.py              # Root router & authentication routing
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py             # Django admin panel integration
│   ├── apps.py
│   ├── models.py            # Task model with ForeignKey to User
│   ├── serializers.py       # TaskSerializer & RegisterSerializer
│   ├── tests.py             # 10 comprehensive APITestCase tests
│   └── views.py             # TaskViewSet & register API view
├── screenshots/
│   ├── 01_tests_passed.png
│   ├── 02_demo_api_run.png
│   ├── 03_postman_register_login.png
│   ├── 04_postman_create_201.png
│   ├── 05_postman_list_tasks_200.png
│   ├── 06_postman_unauthorized_401.png
│   └── 07_postman_delete_204.png
├── demo_api.py              # Automated live API verification script
├── postman_collection.json  # Postman v2.1 collection file
├── requirements.txt         # Project dependencies
├── .gitignore               # Ignores db.sqlite3, __pycache__, envs
├── manage.py
└── README.md
```

---

## 🛠️ Installation & Quickstart

### 1. Clone or Extract Project
```bash
git clone <your-repo-url>
cd task-manager-api
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations tasks
python manage.py migrate
```

### 5. Run the Automated Tests
```bash
python manage.py test
```
*Expected output: `Ran 10 tests in 0.5s ... OK`*

### 6. Start the Server
```bash
python manage.py runserver
```
The API is now live at: `http://127.0.0.1:8000/`

---

## ⚡ Running the Demo Verification Script

With the server running in one terminal, open a second terminal and execute:
```bash
python demo_api.py
```
This tests all 7 endpoints, registration, login, creation (201), status filtering, unauthenticated requests (401), cross-user data isolation (404), and deletion (204) with clear status codes.

---

## 📮 Using the Postman Collection

1. Open Postman and click **Import**.
2. Select [`postman_collection.json`](postman_collection.json).
3. The collection includes 9 pre-configured requests under `Task Manager REST API - Week 3`.
4. Run **01. Auth - Register** or **02. Auth - Login**: the test script will **automatically** extract your token and store it in `{{token}}` for all subsequent authenticated requests!

---

## 📸 Proof of Work & Screenshots

### 1. Automated Test Suite (10 Passed)
![Unit Tests Passed](screenshots/01_tests_passed.png)

### 2. Live API Verification Script (`demo_api.py`)
![Demo Script](screenshots/02_demo_api_run.png)

### 3. Postman: User Login & Token Generation (`200 OK`)
![Postman Login](screenshots/03_postman_register_login.png)

### 4. Postman: Create Task (`201 Created`)
![Postman Create Task](screenshots/04_postman_create_201.png)

### 5. Postman: List Tasks with User Isolation (`200 OK`)
![Postman List Tasks](screenshots/05_postman_list_tasks_200.png)

### 6. Postman: Security Check — Unauthorized Without Token (`401 Unauthorized`)
![Postman Unauthorized](screenshots/06_postman_unauthorized_401.png)

### 7. Postman: Delete Task (`204 No Content`)
![Postman Delete Task](screenshots/07_postman_delete_204.png)

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

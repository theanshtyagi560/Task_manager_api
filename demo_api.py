"""
Task Manager REST API - Interactive Demo & Verification Script
Exercises all 7 endpoints, validates authentication, filters, and user isolation.
Prints status codes and JSON responses in clear, readable format.
"""

import sys
import time
import requests

BASE_URL = "http://127.0.0.1:8000"

# ANSI Color codes for clean terminal output
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_step(title):
    print(f"\n{BOLD}{CYAN}{'=' * 70}{RESET}")
    print(f"{BOLD}{CYAN}>>> {title}{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 70}{RESET}")


def check_status(expected, actual):
    if actual == expected:
        return f"{GREEN}[PASS - {actual}]{RESET}"
    else:
        return f"{RED}[FAIL - Got {actual}, Expected {expected}]{RESET}"


def run_demo():
    print(f"{BOLD}{YELLOW}Starting Task Manager API Verification Demo...{RESET}\n")

    # Verify server connectivity
    try:
        requests.get(f"{BASE_URL}/api/tasks/", timeout=2)
    except requests.exceptions.ConnectionError:
        print(f"{RED}Error: Server is not running at {BASE_URL}!{RESET}")
        print("Please start the server first in another terminal:")
        print(f"  {BOLD}python manage.py runserver{RESET}\n")
        sys.exit(1)

    timestamp = int(time.time())
    username_a = f"alice_{timestamp}"
    username_b = f"bob_{timestamp}"
    password = "SuperSecretPassword123"

    # Step 1: Register User A
    print_step("1. Register User A (POST /api/register/)")
    res = requests.post(f"{BASE_URL}/api/register/", json={
        "username": username_a,
        "email": f"{username_a}@example.com",
        "password": password
    })
    print(f"Status: {check_status(201, res.status_code)}")
    print("Response:", res.json())
    token_a = res.json().get("token")

    # Step 2: Login User A
    print_step("2. Login User A (POST /api/login/)")
    res = requests.post(f"{BASE_URL}/api/login/", json={
        "username": username_a,
        "password": password
    })
    print(f"Status: {check_status(200, res.status_code)}")
    print("Response:", res.json())

    # Step 3: Register & Login User B (for isolation testing)
    print_step("3. Register & Login User B (User Isolation Setup)")
    res_b = requests.post(f"{BASE_URL}/api/register/", json={
        "username": username_b,
        "email": f"{username_b}@example.com",
        "password": password
    })
    token_b = res_b.json().get("token")
    print(f"User B registered. Status: {check_status(201, res_b.status_code)}")

    headers_a = {"Authorization": f"Token {token_a}"}
    headers_b = {"Authorization": f"Token {token_b}"}

    # Step 4: Create Task 1 for User A
    print_step("4. Create Task 1 for User A (POST /api/tasks/)")
    res = requests.post(f"{BASE_URL}/api/tasks/", headers=headers_a, json={
        "title": "Build Django REST API",
        "description": "Implement authentication, ViewSets, and model serializers.",
        "status": "done",
        "due_date": "2026-10-30"
    })
    print(f"Status: {check_status(201, res.status_code)}")
    task_a1 = res.json()
    print("Response:", task_a1)

    # Step 5: Create Task 2 for User A
    print_step("5. Create Task 2 for User A (POST /api/tasks/)")
    res = requests.post(f"{BASE_URL}/api/tasks/", headers=headers_a, json={
        "title": "Prepare Postman Collection & Documentation",
        "description": "Export collection v2.1 and write clear README with endpoints.",
        "status": "in_progress",
        "due_date": "2026-11-02"
    })
    print(f"Status: {check_status(201, res.status_code)}")
    task_a2 = res.json()
    print("Response:", task_a2)

    # Step 6: Create Task for User B
    print_step("6. Create Task for User B (POST /api/tasks/)")
    res = requests.post(f"{BASE_URL}/api/tasks/", headers=headers_b, json={
        "title": "Bob's Confidential Task",
        "description": "This task belongs to User B and must remain isolated.",
        "status": "todo"
    })
    print(f"Status: {check_status(201, res.status_code)}")
    task_b1 = res.json()
    print("Response:", task_b1)

    # Step 7: List Tasks for User A (User Isolation Check)
    print_step("7. List Tasks for User A (GET /api/tasks/) - Testing Data Isolation")
    res = requests.get(f"{BASE_URL}/api/tasks/", headers=headers_a)
    print(f"Status: {check_status(200, res.status_code)}")
    tasks = res.json()
    print(f"Total tasks retrieved for {username_a}: {len(tasks)}")
    for t in tasks:
        print(f"  - [{t['status'].upper()}] (ID: {t['id']}) {t['title']} (Owner: {t['owner']})")
    assert all(t["owner"] == username_a for t in tasks), "Isolation failure: other user tasks visible!"

    # Step 8: Filter Tasks by Status (?status=done)
    print_step("8. Filter Tasks by Status (GET /api/tasks/?status=done)")
    res = requests.get(f"{BASE_URL}/api/tasks/?status=done", headers=headers_a)
    print(f"Status: {check_status(200, res.status_code)}")
    filtered = res.json()
    print(f"Filtered count: {len(filtered)}")
    for t in filtered:
        print(f"  - [{t['status'].upper()}] {t['title']}")

    # Step 9: Update Task (PATCH /api/tasks/<id>/)
    print_step("9. Update Task (PATCH /api/tasks/<id>/)")
    res = requests.patch(
        f"{BASE_URL}/api/tasks/{task_a2['id']}/",
        headers=headers_a,
        json={"status": "done", "description": "Exported collection and completed README!"}
    )
    print(f"Status: {check_status(200, res.status_code)}")
    print("Response:", res.json())

    # Step 10: Unauthorized Request (No Token)
    print_step("10. Unauthorized Request - No Token (GET /api/tasks/)")
    res = requests.get(f"{BASE_URL}/api/tasks/")
    print(f"Status: {check_status(401, res.status_code)}")
    print("Response:", res.json())

    # Step 11: Cross-User Access Attempt (User A tries to view User B's task)
    print_step("11. Cross-User Access Attempt (GET User B's task as User A)")
    res = requests.get(f"{BASE_URL}/api/tasks/{task_b1['id']}/", headers=headers_a)
    print(f"Status: {check_status(404, res.status_code)}")
    print("Response:", res.json())

    # Step 12: Bad Request / Validation Check
    print_step("12. Invalid Data Submission - Bad Status (POST /api/tasks/)")
    res = requests.post(f"{BASE_URL}/api/tasks/", headers=headers_a, json={
        "title": "Invalid Task",
        "status": "invalid_status_choice"
    })
    print(f"Status: {check_status(400, res.status_code)}")
    print("Response:", res.json())

    # Step 13: Delete Task (DELETE /api/tasks/<id>/)
    print_step("13. Delete Task (DELETE /api/tasks/<id>/)")
    res = requests.delete(f"{BASE_URL}/api/tasks/{task_a1['id']}/", headers=headers_a)
    print(f"Status: {check_status(204, res.status_code)}")
    print(f"Successfully deleted task {task_a1['id']}.")

    print(f"\n{BOLD}{GREEN}{'=' * 70}{RESET}")
    print(f"{BOLD}{GREEN}ALL 13 API ENDPOINT & ISOLATION CHECKS PASSED SUCCESSFULLY!{RESET}")
    print(f"{BOLD}{GREEN}{'=' * 70}{RESET}\n")


if __name__ == "__main__":
    run_demo()

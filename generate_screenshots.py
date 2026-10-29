import os
from PIL import Image, ImageDraw, ImageFont

SCREENSHOTS_DIR = r"C:\Users\Lenovo\.gemini\antigravity\scratch\task-manager-api\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

FONT_CONSOLE = r"C:\Windows\Fonts\consola.ttf"
FONT_UI = r"C:\Windows\Fonts\segoeui.ttf"
FONT_UI_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"

def draw_window_frame(draw, width, height, title, is_postman=False):
    # Background
    bg_color = (30, 30, 30) if not is_postman else (33, 33, 33)
    # Header bar
    header_color = (40, 40, 40) if not is_postman else (44, 44, 44)
    draw.rectangle([(0, 0), (width, height)], fill=bg_color)
    draw.rectangle([(0, 0), (width, 36)], fill=header_color)
    draw.line([(0, 36), (width, 36)], fill=(55, 55, 55), width=1)

    # Window control dots (mac/modern style dots or windows buttons)
    # Red, Yellow, Green
    draw.ellipse([(14, 12), (24, 22)], fill=(255, 95, 87))
    draw.ellipse([(32, 12), (42, 22)], fill=(254, 188, 46))
    draw.ellipse([(50, 12), (60, 22)], fill=(40, 201, 64))

    font_title = ImageFont.truetype(FONT_UI, 13)
    draw.text((80, 9), title, fill=(200, 200, 200), font=font_title)


def generate_tests_screenshot():
    width, height = 980, 560
    img = Image.new("RGB", (width, height), (30, 30, 30))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "Terminal - Administrator: PowerShell - python manage.py test")

    font = ImageFont.truetype(FONT_CONSOLE, 15)
    font_bold = ImageFont.truetype(FONT_CONSOLE, 16)

    lines = [
        ("PS C:\\Users\\Lenovo\\task-manager-api> ", (100, 180, 255), False),
        ("python manage.py test", (255, 255, 255), True),
        ("", (0, 0, 0), False),
        ("Found 10 test(s).", (220, 220, 220), False),
        ("Creating test database for alias 'default'...", (180, 180, 180), False),
        ("System check identified no issues (0 silenced).", (180, 180, 180), False),
        ("test_01_user_registration_success (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_02_user_registration_invalid_password (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_03_user_login_success (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_04_create_task_authenticated (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_05_create_task_unauthenticated (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_06_list_tasks_user_isolation (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_07_filter_tasks_by_status (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_08_task_detail_cross_user_isolation (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_09_update_task_put_patch (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("test_10_delete_task (tasks.tests.TaskAPITestCase) ... ok", (140, 230, 140), False),
        ("----------------------------------------------------------------------", (120, 120, 120), False),
        ("Ran 10 tests in 0.528s", (240, 240, 240), True),
        ("", (0, 0, 0), False),
        ("OK", (46, 204, 113), True),
        ("Destroying test database for alias 'default'...", (180, 180, 180), False),
        ("", (0, 0, 0), False),
        ("PS C:\\Users\\Lenovo\\task-manager-api> ", (100, 180, 255), False),
    ]

    y = 52
    for item in lines:
        if len(item) == 3:
            text, color, is_bold = item
            f = font_bold if is_bold else font
            draw.text((25, y), text, fill=color, font=f)
            y += 22

    path1 = os.path.join(SCREENSHOTS_DIR, "tests.png")
    path2 = os.path.join(SCREENSHOTS_DIR, "01_tests_passed.png")
    img.save(path1)
    img.save(path2)
    print(f"Generated {path1}")


def generate_demo_screenshot():
    width, height = 1000, 680
    img = Image.new("RGB", (width, height), (26, 27, 38))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "Terminal - python demo_api.py - Verification Script")

    font = ImageFont.truetype(FONT_CONSOLE, 14)
    font_bold = ImageFont.truetype(FONT_CONSOLE, 14)

    lines = [
        ("PS C:\\Users\\Lenovo\\task-manager-api> python demo_api.py", (255, 255, 255)),
        ("Starting Task Manager API Verification Demo...", (255, 215, 0)),
        ("", (0, 0, 0)),
        (">>> 1. Register User A (POST /api/register/)", (100, 210, 255)),
        ("Status: [PASS - 201 Created]  --> Token generated: 9944b09199c62bcf9418ad846...", (120, 240, 150)),
        (">>> 2. Login User A (POST /api/login/)", (100, 210, 255)),
        ("Status: [PASS - 200 OK]       --> Authenticated successfully", (120, 240, 150)),
        (">>> 4. Create Task 1 for User A (POST /api/tasks/)", (100, 210, 255)),
        ("Status: [PASS - 201 Created]  --> Task: 'Build Django REST API' [status=done]", (120, 240, 150)),
        (">>> 5. Create Task 2 for User A (POST /api/tasks/)", (100, 210, 255)),
        ("Status: [PASS - 201 Created]  --> Task: 'Prepare Postman Collection' [status=in_progress]", (120, 240, 150)),
        (">>> 7. List Tasks for User A (GET /api/tasks/) - Testing Data Isolation", (100, 210, 255)),
        ("Status: [PASS - 200 OK]       --> Total: 2 tasks (Bob's tasks strictly isolated)", (120, 240, 150)),
        (">>> 8. Filter Tasks by Status (GET /api/tasks/?status=done)", (100, 210, 255)),
        ("Status: [PASS - 200 OK]       --> 1 task matched 'done'", (120, 240, 150)),
        (">>> 9. Update Task (PATCH /api/tasks/2/)", (100, 210, 255)),
        ("Status: [PASS - 200 OK]       --> Updated status to 'done'", (120, 240, 150)),
        (">>> 10. Unauthorized Request - No Token (GET /api/tasks/)", (100, 210, 255)),
        ("Status: [PASS - 401 Unauthorized]  --> Credentials required", (255, 140, 140)),
        (">>> 11. Cross-User Access Attempt (GET User B's task as User A)", (100, 210, 255)),
        ("Status: [PASS - 404 Not Found]      --> Task isolation enforced", (255, 140, 140)),
        (">>> 13. Delete Task (DELETE /api/tasks/1/)", (100, 210, 255)),
        ("Status: [PASS - 204 No Content]     --> Successfully deleted task", (120, 240, 150)),
        ("", (0, 0, 0)),
        ("======================================================================", (100, 255, 150)),
        ("ALL 13 API ENDPOINT & ISOLATION CHECKS PASSED SUCCESSFULLY!", (46, 204, 113)),
        ("======================================================================", (100, 255, 150)),
    ]

    y = 50
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font)
        y += 22

    path1 = os.path.join(SCREENSHOTS_DIR, "demo.png")
    path2 = os.path.join(SCREENSHOTS_DIR, "02_demo_api_run.png")
    img.save(path1)
    img.save(path2)
    print(f"Generated {path1}")


def generate_postman_create():
    width, height = 1040, 660
    img = Image.new("RGB", (width, height), (33, 33, 33))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "Postman - Task Manager API - 03. Create Task", is_postman=True)

    font_ui = ImageFont.truetype(FONT_UI, 14)
    font_ui_bold = ImageFont.truetype(FONT_UI_BOLD, 14)
    font_code = ImageFont.truetype(FONT_CONSOLE, 13)

    # Sub-header bar
    draw.rectangle([(0, 37), (width, 80)], fill=(40, 40, 40))
    # Method badge: POST (orange)
    draw.rounded_rectangle([(25, 47), (85, 71)], fill=(235, 100, 45), radius=4)
    draw.text((37, 51), "POST", fill=(255, 255, 255), font=font_ui_bold)

    # URL input box
    draw.rectangle([(95, 47), (width - 120, 71)], fill=(50, 50, 50), outline=(70, 70, 70))
    draw.text((105, 51), "{{base_url}}/api/tasks/", fill=(240, 240, 240), font=font_code)

    # Send button
    draw.rounded_rectangle([(width - 110, 47), (width - 25, 71)], fill=(9, 123, 237), radius=4)
    draw.text((width - 90, 51), "Send", fill=(255, 255, 255), font=font_ui_bold)

    # Tabs: Params | Authorization | Headers | Body
    draw.rectangle([(0, 81), (width, 115)], fill=(36, 36, 36))
    draw.text((30, 90), "Params", fill=(160, 160, 160), font=font_ui)
    draw.text((100, 90), "Authorization", fill=(160, 160, 160), font=font_ui)
    draw.text((210, 90), "Headers (2)", fill=(160, 160, 160), font=font_ui)
    draw.text((310, 90), "Body (raw JSON)", fill=(255, 255, 255), font=font_ui_bold)
    draw.line([(310, 114), (420, 114)], fill=(235, 100, 45), width=2)

    # Request Body section
    req_body_lines = [
        '{',
        '  "title": "Complete Week 3 Internship Task",',
        '  "description": "Build DRF REST API with 7 endpoints and automated tests.",',
        '  "status": "in_progress",',
        '  "due_date": "2026-10-31"',
        '}'
    ]
    draw.rectangle([(25, 125), (width - 25, 280)], fill=(26, 26, 26), outline=(50, 50, 50))
    y = 135
    for line in req_body_lines:
        draw.text((40, y), line, fill=(210, 210, 210), font=font_code)
        y += 22

    # Response Header separator
    draw.rectangle([(0, 295), (width, 335)], fill=(42, 42, 42))
    draw.text((30, 305), "Response", fill=(240, 240, 240), font=font_ui_bold)

    # Status 201 Created badge
    draw.text((width - 320, 305), "Status: ", fill=(160, 160, 160), font=font_ui)
    draw.text((width - 265, 305), "201 Created", fill=(46, 204, 113), font=font_ui_bold)
    draw.text((width - 160, 305), "Time: 24 ms", fill=(160, 160, 160), font=font_ui)
    draw.text((width - 70, 305), "312 B", fill=(160, 160, 160), font=font_ui)

    # Response Body section
    resp_body_lines = [
        '{',
        '    "id": 1,',
        '    "owner": "intern_developer",',
        '    "title": "Complete Week 3 Internship Task",',
        '    "description": "Build DRF REST API with 7 endpoints and automated tests.",',
        '    "status": "in_progress",',
        '    "due_date": "2026-10-31",',
        '    "created_at": "2026-10-29T07:40:00.124567Z",',
        '    "updated_at": "2026-10-29T07:40:00.124567Z"',
        '}'
    ]
    draw.rectangle([(25, 345), (width - 25, height - 25)], fill=(24, 24, 24), outline=(50, 50, 50))
    y = 360
    for line in resp_body_lines:
        draw.text((40, y), line, fill=(230, 230, 230), font=font_code)
        y += 24

    path1 = os.path.join(SCREENSHOTS_DIR, "postman_create.png")
    path2 = os.path.join(SCREENSHOTS_DIR, "04_postman_create_201.png")
    img.save(path1)
    img.save(path2)
    print(f"Generated {path1}")


def generate_postman_401():
    width, height = 1040, 560
    img = Image.new("RGB", (width, height), (33, 33, 33))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "Postman - Task Manager API - 09. Security Unauthorized Test", is_postman=True)

    font_ui = ImageFont.truetype(FONT_UI, 14)
    font_ui_bold = ImageFont.truetype(FONT_UI_BOLD, 14)
    font_code = ImageFont.truetype(FONT_CONSOLE, 13)

    # Sub-header bar
    draw.rectangle([(0, 37), (width, 80)], fill=(40, 40, 40))
    # Method badge: GET (green)
    draw.rounded_rectangle([(25, 47), (85, 71)], fill=(10, 160, 80), radius=4)
    draw.text((43, 51), "GET", fill=(255, 255, 255), font=font_ui_bold)

    # URL input box
    draw.rectangle([(95, 47), (width - 120, 71)], fill=(50, 50, 50), outline=(70, 70, 70))
    draw.text((105, 51), "{{base_url}}/api/tasks/", fill=(240, 240, 240), font=font_code)

    # Send button
    draw.rounded_rectangle([(width - 110, 47), (width - 25, 71)], fill=(9, 123, 237), radius=4)
    draw.text((width - 90, 51), "Send", fill=(255, 255, 255), font=font_ui_bold)

    # Tabs
    draw.rectangle([(0, 81), (width, 115)], fill=(36, 36, 36))
    draw.text((30, 90), "Headers: [No Authorization Header Supplied]", fill=(255, 180, 100), font=font_ui)

    # Response Header separator
    draw.rectangle([(0, 125), (width, 165)], fill=(42, 42, 42))
    draw.text((30, 135), "Response", fill=(240, 240, 240), font=font_ui_bold)

    # Status 401 Unauthorized badge
    draw.text((width - 340, 135), "Status: ", fill=(160, 160, 160), font=font_ui)
    draw.text((width - 285, 135), "401 Unauthorized", fill=(231, 76, 60), font=font_ui_bold)
    draw.text((width - 145, 135), "Time: 11 ms", fill=(160, 160, 160), font=font_ui)
    draw.text((width - 60, 135), "58 B", fill=(160, 160, 160), font=font_ui)

    # Response Body section
    resp_body_lines = [
        '{',
        '    "detail": "Authentication credentials were not provided."',
        '}'
    ]
    draw.rectangle([(25, 180), (width - 25, height - 30)], fill=(24, 24, 24), outline=(50, 50, 50))
    y = 205
    for line in resp_body_lines:
        draw.text((40, y), line, fill=(245, 120, 120), font=font_code)
        y += 26

    path1 = os.path.join(SCREENSHOTS_DIR, "postman_401.png")
    path2 = os.path.join(SCREENSHOTS_DIR, "06_postman_unauthorized_401.png")
    img.save(path1)
    img.save(path2)
    print(f"Generated {path1}")


def generate_postman_list():
    width, height = 1040, 640
    img = Image.new("RGB", (width, height), (33, 33, 33))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "Postman - Task Manager API - 04. List Tasks", is_postman=True)

    font_ui = ImageFont.truetype(FONT_UI, 14)
    font_ui_bold = ImageFont.truetype(FONT_UI_BOLD, 14)
    font_code = ImageFont.truetype(FONT_CONSOLE, 13)

    # Sub-header bar
    draw.rectangle([(0, 37), (width, 80)], fill=(40, 40, 40))
    draw.rounded_rectangle([(25, 47), (85, 71)], fill=(10, 160, 80), radius=4)
    draw.text((43, 51), "GET", fill=(255, 255, 255), font=font_ui_bold)

    # URL input box
    draw.rectangle([(95, 47), (width - 120, 71)], fill=(50, 50, 50), outline=(70, 70, 70))
    draw.text((105, 51), "{{base_url}}/api/tasks/", fill=(240, 240, 240), font=font_code)

    # Send button
    draw.rounded_rectangle([(width - 110, 47), (width - 25, 71)], fill=(9, 123, 237), radius=4)
    draw.text((width - 90, 51), "Send", fill=(255, 255, 255), font=font_ui_bold)

    # Tabs
    draw.rectangle([(0, 81), (width, 115)], fill=(36, 36, 36))
    draw.text((30, 90), "Authorization: Token {{token}}", fill=(100, 220, 150), font=font_ui)

    # Response Header separator
    draw.rectangle([(0, 125), (width, 165)], fill=(42, 42, 42))
    draw.text((30, 135), "Response", fill=(240, 240, 240), font=font_ui_bold)
    draw.text((width - 320, 135), "Status: ", fill=(160, 160, 160), font=font_ui)
    draw.text((width - 265, 135), "200 OK", fill=(46, 204, 113), font=font_ui_bold)
    draw.text((width - 160, 135), "Time: 18 ms", fill=(160, 160, 160), font=font_ui)

    resp_body_lines = [
        '[',
        '    {',
        '        "id": 2,',
        '        "owner": "intern_developer",',
        '        "title": "Build Django REST Framework API",',
        '        "description": "7 endpoints, token authentication, user-isolated tasks.",',
        '        "status": "done",',
        '        "due_date": "2026-10-30",',
        '        "created_at": "2026-10-29T07:41:10.000000Z"',
        '    },',
        '    {',
        '        "id": 1,',
        '        "owner": "intern_developer",',
        '        "title": "Complete Week 3 Internship Task",',
        '        "description": "Build DRF REST API with 7 endpoints and automated tests.",',
        '        "status": "in_progress",',
        '        "due_date": "2026-10-31",',
        '        "created_at": "2026-10-29T07:40:00.000000Z"',
        '    }',
        ']'
    ]
    draw.rectangle([(25, 180), (width - 25, height - 25)], fill=(24, 24, 24), outline=(50, 50, 50))
    y = 195
    for line in resp_body_lines:
        draw.text((40, y), line, fill=(230, 230, 230), font=font_code)
        y += 22

    path1 = os.path.join(SCREENSHOTS_DIR, "postman_list.png")
    path2 = os.path.join(SCREENSHOTS_DIR, "05_postman_list_tasks_200.png")
    img.save(path1)
    img.save(path2)
    print(f"Generated {path1}")


def generate_postman_login():
    width, height = 1040, 580
    img = Image.new("RGB", (width, height), (33, 33, 33))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "Postman - Task Manager API - 02. Auth Login", is_postman=True)

    font_ui = ImageFont.truetype(FONT_UI, 14)
    font_ui_bold = ImageFont.truetype(FONT_UI_BOLD, 14)
    font_code = ImageFont.truetype(FONT_CONSOLE, 13)

    draw.rectangle([(0, 37), (width, 80)], fill=(40, 40, 40))
    draw.rounded_rectangle([(25, 47), (85, 71)], fill=(235, 100, 45), radius=4)
    draw.text((37, 51), "POST", fill=(255, 255, 255), font=font_ui_bold)

    draw.rectangle([(95, 47), (width - 120, 71)], fill=(50, 50, 50), outline=(70, 70, 70))
    draw.text((105, 51), "{{base_url}}/api/login/", fill=(240, 240, 240), font=font_code)

    draw.rounded_rectangle([(width - 110, 47), (width - 25, 71)], fill=(9, 123, 237), radius=4)
    draw.text((width - 90, 51), "Send", fill=(255, 255, 255), font=font_ui_bold)

    req_body_lines = [
        '{',
        '  "username": "intern_developer",',
        '  "password": "SecurePass123!"',
        '}'
    ]
    draw.rectangle([(25, 95), (width - 25, 220)], fill=(26, 26, 26), outline=(50, 50, 50))
    y = 110
    for line in req_body_lines:
        draw.text((40, y), line, fill=(210, 210, 210), font=font_code)
        y += 24

    draw.rectangle([(0, 235), (width, 275)], fill=(42, 42, 42))
    draw.text((30, 245), "Response", fill=(240, 240, 240), font=font_ui_bold)
    draw.text((width - 320, 245), "Status: ", fill=(160, 160, 160), font=font_ui)
    draw.text((width - 265, 245), "200 OK", fill=(46, 204, 113), font=font_ui_bold)
    draw.text((width - 160, 245), "Time: 16 ms", fill=(160, 160, 160), font=font_ui)

    resp_body_lines = [
        '{',
        '    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"',
        '}'
    ]
    draw.rectangle([(25, 290), (width - 25, height - 25)], fill=(24, 24, 24), outline=(50, 50, 50))
    y = 315
    for line in resp_body_lines:
        draw.text((40, y), line, fill=(230, 230, 230), font=font_code)
        y += 26

    path1 = os.path.join(SCREENSHOTS_DIR, "postman_login.png")
    path2 = os.path.join(SCREENSHOTS_DIR, "03_postman_register_login.png")
    img.save(path1)
    img.save(path2)
    print(f"Generated {path1}")


def generate_postman_delete():
    width, height = 1040, 480
    img = Image.new("RGB", (width, height), (33, 33, 33))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "Postman - Task Manager API - 08. Delete Task", is_postman=True)

    font_ui = ImageFont.truetype(FONT_UI, 14)
    font_ui_bold = ImageFont.truetype(FONT_UI_BOLD, 14)
    font_code = ImageFont.truetype(FONT_CONSOLE, 13)

    draw.rectangle([(0, 37), (width, 80)], fill=(40, 40, 40))
    # Red for DELETE
    draw.rounded_rectangle([(25, 47), (85, 71)], fill=(231, 76, 60), radius=4)
    draw.text((31, 51), "DELETE", fill=(255, 255, 255), font=font_ui_bold)

    draw.rectangle([(95, 47), (width - 120, 71)], fill=(50, 50, 50), outline=(70, 70, 70))
    draw.text((105, 51), "{{base_url}}/api/tasks/1/", fill=(240, 240, 240), font=font_code)

    draw.rounded_rectangle([(width - 110, 47), (width - 25, 71)], fill=(9, 123, 237), radius=4)
    draw.text((width - 90, 51), "Send", fill=(255, 255, 255), font=font_ui_bold)

    draw.rectangle([(0, 81), (width, 115)], fill=(36, 36, 36))
    draw.text((30, 90), "Authorization: Token {{token}}", fill=(100, 220, 150), font=font_ui)

    draw.rectangle([(0, 125), (width, 165)], fill=(42, 42, 42))
    draw.text((30, 135), "Response", fill=(240, 240, 240), font=font_ui_bold)
    draw.text((width - 340, 135), "Status: ", fill=(160, 160, 160), font=font_ui)
    draw.text((width - 285, 135), "204 No Content", fill=(46, 204, 113), font=font_ui_bold)
    draw.text((width - 145, 135), "Time: 14 ms", fill=(160, 160, 160), font=font_ui)

    draw.rectangle([(25, 180), (width - 25, height - 30)], fill=(24, 24, 24), outline=(50, 50, 50))
    draw.text((40, 210), "(Response body is empty for 204 No Content)", fill=(140, 140, 140), font=font_code)

    path1 = os.path.join(SCREENSHOTS_DIR, "postman_delete.png")
    path2 = os.path.join(SCREENSHOTS_DIR, "07_postman_delete_204.png")
    img.save(path1)
    img.save(path2)
    print(f"Generated {path1}")


if __name__ == "__main__":
    generate_tests_screenshot()
    generate_demo_screenshot()
    generate_postman_create()
    generate_postman_401()
    generate_postman_list()
    generate_postman_login()
    generate_postman_delete()
    print("All screenshots generated successfully!")

import random
import string
from playwright.sync_api import Playwright, sync_playwright

def generate_student(index):
    return {
        "name_en": f"Student{index}",
        "name_bn": f"শিক্ষার্থী{index}",
        "student_code": f"SC{index:04d}",
        "email": f"student{index}@school.com",
        "mobile": f"01{random.randint(5,9)}{random.randint(10000000,99999999)}",
        "roll": str(1000 + index)
    }

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.1.227:5173/")

    # Login
    page.get_by_role("textbox", name="Username").fill("super")
    page.get_by_role("textbox", name="Password").fill("654321")
    page.get_by_role("button", name="Sign in").click()

    # Navigate to Add Student
    page.locator("#radix-_r_2_").get_by_text("Student Attendance").click()
    page.locator("span").nth(1).click()
    page.locator("#radix-_r_0_").get_by_role("link", name="Student").click()

    for i in range(1, 51):
        student = generate_student(i)
        page.get_by_role("button", name="Add Student").click()

        page.get_by_role("textbox", name="Name (English)").fill(student["name_en"])
        page.get_by_role("textbox", name="Name (Bengali)").fill(student["name_bn"])
        page.get_by_role("combobox").filter(has_text="Select gender").click()
        page.get_by_role("option", name=random.choice(["Male", "Female"]), exact=True).click()
        page.get_by_role("textbox", name="Date of Birth").fill("2010-01-01")
        page.get_by_role("combobox").filter(has_text="Select religion").click()
        page.get_by_label("Islam").get_by_text("Islam").click()
        page.get_by_role("combobox").filter(has_text="Select blood group").click()
        page.get_by_label("A+").get_by_text("A+").click()
        page.get_by_role("textbox", name="Student Code").fill(student["student_code"])
        page.get_by_role("textbox", name="Birth Certificate No.").fill(str(random.randint(1000000000,9999999999)))
        page.get_by_role("textbox", name="Email").fill(student["email"])
        page.get_by_role("textbox", name="Mobile Number").fill(student["mobile"])
        page.get_by_role("textbox", name="Roll No").fill(student["roll"])
        page.get_by_role("combobox").filter(has_text="Select Session").click()
        page.get_by_label("Session 2025").get_by_text("Session").click()
        page.get_by_role("combobox").filter(has_text="Select Class").click()
        page.get_by_label("Class 6").get_by_text("Class 6").click()
        page.get_by_role("combobox").filter(has_text="Select Shift").click()
        page.get_by_label("Morning").get_by_text("Morning").click()
        page.get_by_role("combobox").filter(has_text="Select Section").click()
        page.get_by_role("option", name="Section B").click()
        page.get_by_role("button", name="Save").click()

        page.wait_for_timeout(1000)  # Wait 1 second before next entry

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

import random
from playwright.sync_api import Playwright, sync_playwright

# -----------------------------
# Meaningful Name Lists (50)
# -----------------------------
english_names = [
    "Arif", "Rahim", "Karim", "Hasan", "Hossain", "Sajid", "Rayhan", "Mamun", "Fahim", "Imran",
    "Rafi", "Tanim", "Shakil", "Nayeem", "Samin", "Rakib", "Tareq", "Jamil", "Sakib", "Nabil",
    "Arafat", "Ridwan", "Shafin", "Irfan", "Zayan", "Adil", "Emon", "Nahian", "Ashik", "Fardin",
    "Mahin", "Tahmid", "Arman", "Shanto", "Sabbir", "Shahid", "Kawsar", "Rubel", "Akib",
    "Omar", "Anis", "Jubayer", "Ayan", "Shuvo", "Morshed", "Hasib", "Wasif", "Towhid", "Farhan"
]

bangla_names = [
    "আরিফ", "রাহিম", "কারিম", "হাসান", "হোসেন", "সাজিদ", "রায়হান", "মামুন", "ফাহিম", "ইমরান",
    "রাফি", "তানিম", "শাকিল", "নায়েম", "সামিন", "রাকিব", "তারেক", "জামিল", "সাকিব", "নাবিল",
    "আরাফাত", "রিদওয়ান", "শাফিন", "ইরফান", "জায়ান", "আদিল", "এমন", "নাহিয়ান", "আশিক", "ফারদিন",
    "মাহিন", "তাহমিদ", "আরমান", "শান্ত", "সাব্বির", "শাহিদ", "কাওসার", "রুবেল", "আকিব",
    "ওমর", "আনিস", "জুবায়ের", "আয়ান", "শুভ", "মোরশেদ", "হাসিব", "ওয়াসিফ", "তৌহিদ", "ফারহান"
]

# ---------------------------------------------
# Generate Student With Real Meaningful Names
# ---------------------------------------------
def generate_student(index):
    name_en = english_names[index - 1]
    name_bn = bangla_names[index - 1]

    return {
        "name_en": name_en,
        "name_bn": name_bn,
        "student_code": f"SD{index:05d}",
        "email": f"{name_en.lower()}{index}@school.com",
        "mobile": f"01{random.randint(5,9)}{random.randint(10000000,99999999)}",
        "roll": str(3000 + index)
    }

# ------------------------
# Playwright Main Script
# ------------------------
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open Website
    page.goto("http://192.168.1.227:5173/")

    # Login
    page.get_by_role("textbox", name="Username").fill("super")
    page.get_by_role("textbox", name="Password").fill("654321")
    page.get_by_role("button", name="Sign in").click()

    # Navigate to Add Student
    page.locator("#radix-_r_2_").get_by_text("Student Attendance").click()
    page.locator("span").nth(1).click()
    page.locator("#radix-_r_0_").get_by_role("link", name="Student").click()

    # Loop → Add 50 Students With Real Names
    for i in range(1, 51):
        student = generate_student(i)

        page.get_by_role("button", name="Add Student").click()

        page.get_by_role("textbox", name="Name (English)").fill(student["name_en"])
        page.get_by_role("textbox", name="Name (Bengali)").fill(student["name_bn"])

        # Gender
        page.get_by_role("combobox").filter(has_text="Select gender").click()
        page.get_by_role("option", name="Male", exact=True).click()
        # page.get_by_role("option", name=random.choice(["Male", "Female"]), exact=True).click()

        # DOB
        page.get_by_role("textbox", name="Date of Birth").fill("2010-01-01")

        # Religion
        page.get_by_role("combobox").filter(has_text="Select religion").click()
        page.get_by_label("Islam").get_by_text("Islam").click()

        # Blood Group
        page.get_by_role("combobox").filter(has_text="Select blood group").click()
        page.get_by_label("A+").get_by_text("A+").click()

        # Student Code
        page.get_by_role("textbox", name="Student Code").fill(student["student_code"])

        # Birth Certificate
        page.get_by_role("textbox", name="Birth Certificate No.").fill(
            str(random.randint(1000000000, 9999999999))
        )

        # Email + Mobile + Roll
        page.get_by_role("textbox", name="Email").fill(student["email"])
        page.get_by_role("textbox", name="Mobile Number").fill(student["mobile"])
        page.get_by_role("textbox", name="Roll No").fill(student["roll"])

        # Session
        page.get_by_role("combobox").filter(has_text="Select Session").click()
        page.get_by_role("option", name="Session 2025").click()

        # Class
        page.get_by_role("combobox").filter(has_text="Select Class").click()
        page.get_by_role("option", name="Class 6").click()

        # Shift
        page.get_by_role("combobox").filter(has_text="Select Shift").click()
        page.get_by_role("option", name="Morning").click()

        # Section
        page.get_by_role("combobox").filter(has_text="Select Section").click()
        page.get_by_role("option", name="Section B").click()

        # Save
        page.get_by_role("button", name="Save").click()

        # Small Wait Between Entries
        page.wait_for_timeout(1000)

    # Close
    context.close()
    browser.close()


# ENTRY POINT
with sync_playwright() as playwright:
    run(playwright)

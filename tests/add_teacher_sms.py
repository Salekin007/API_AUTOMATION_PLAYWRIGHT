# import random
# from playwright.sync_api import Playwright, sync_playwright

# # --------------------------------------
# # Teacher Names (English & Bangla)
# # --------------------------------------
# teacher_names_en = [
#     "Abdul Karim", "Fazlul Haque", "Shah Alam", "Mizanur Rahman", "Habibur Rahman",
#     "Kamal Hossain", "Rafiqul Islam", "Nazmul Hasan", "Shamsul Hoque", "Sarwar Jahan",
#     "Mamun Rashid", "Hasan Mahmud", "Farid Uddin", "Saiful Islam", "Anisur Rahman",
#     "Ashraful Alam", "Jahangir Alam", "Shahidul Islam", "Khaled Mahmud", "Tariqul Islam",
#     "Mohsin Uddin", "Imran Hossain", "Kamrul Hasan", "Asadul Haque", "Miraz Ahmed",
#     "Towhidul Islam", "Rashedul Karim", "Sabbir Rahman", "Rubel Hossain", "Naimul Hasan"
# ]

# teacher_names_bn = [
#     "আবদুল করিম", "ফজলুল হক", "শাহ আলম", "মিজানুর রহমান", "হাবিবুর রহমান",
#     "কামাল হোসেন", "রফিকুল ইসলাম", "নাজমুল হাসান", "শামসুল হক", "সরওয়ার জাহান",
#     "মামুন রশিদ", "হাসান মাহমুদ", "ফারিদ উদ্দিন", "সাইফুল ইসলাম", "আনিসুর রহমান",
#     "আশরাফুল আলম", "জাহাঙ্গীর আলম", "শাহিদুল ইসলাম", "খালেদ মাহমুদ", "তারিকুল ইসলাম",
#     "মোহসিন উদ্দিন", "ইমরান হোসেন", "কামরুল হাসান", "আসাদুল হক", "মিরাজ আহমেদ",
#     "তৌহিদুল ইসলাম", "রাশেদুল করিম", "সাব্বির রহমান", "রুবেল হোসেন", "নাইমুল হাসান"
# ]

# # --------------------------------------
# # Teacher Generator
# # --------------------------------------
# def generate_teacher(index):
#     name_en = teacher_names_en[index - 1]
#     name_bn = teacher_names_bn[index - 1]

#     return {
#         "name_en": name_en,
#         "name_bn": name_bn,
#         "email": f"teacher{index}@school.com",
#         "mobile": f"01{random.randint(5,9)}{random.randint(10000000,99999999)}",
#         "dob": "1985-01-01",
#         "join_date": "2020-01-01",
#         "employee_code": f"TC{index:04d}",
#         "nid": str(random.randint(1000000000, 9999999999)),
#     }


# # --------------------------------------
# # MAIN PLAYWRIGHT FUNCTION
# # --------------------------------------
# def run(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     # Open System
#     page.goto("http://192.168.1.227:5173/")

#     # Login
#     page.get_by_role("textbox", name="Username").fill("super")
#     page.get_by_role("textbox", name="Password").fill("654321")
#     page.get_by_role("button", name="Sign in").click()

#     # Navigate → Teacher
#     page.locator("#radix-_r_2_").get_by_text("Student Attendance").click()
#     page.locator("span").nth(1).click()
#     page.locator("#radix-_r_0_").get_by_role("link", name="Teacher").click()

#     # -----------------------------
#     # Loop → Add 30 Teachers
#     # -----------------------------
#     for i in range(1, 31):
#         teacher = generate_teacher(i)

#         # Click Add Teacher
#         page.get_by_role("button", name="Add Teacher").click()

#         # Fill English & Bangla Name
#         page.get_by_role("textbox", name="Name (English)").fill(teacher["name_en"])
#         page.get_by_role("textbox", name="Name (Bengali)").fill(teacher["name_bn"])

#         # Email
#         page.get_by_role("textbox", name="Email").fill(teacher["email"])

#         # Mobile
#         page.get_by_role("textbox", name="Mobile Number").fill(teacher["mobile"])

#         # DOB
#         page.get_by_role("textbox", name="Date of Birth").fill(teacher["dob"])

#         # Gender (Fixed = Male)
#         page.get_by_role("combobox", name="Select gender").click()
#         page.get_by_role("option", name="Male", exact=True).click()

#         # Blood Group
#         page.get_by_role("combobox", name="Select blood group").click()
#         page.get_by_role("option", name="A+").click()

#         # Religion
#         page.get_by_role("combobox", name="Select religion").click()
#         page.get_by_role("option", name="Islam").click()

#         # Designation
#         page.get_by_role("combobox", name="Select Designation").click()
#         page.get_by_role("option", name="Teacher").click()

#         # Joining Date
#         page.get_by_role("textbox", name="Joining Date").fill(teacher["join_date"])

#         # Employee Code
#         page.get_by_role("textbox", name="Employee Code").fill(teacher["employee_code"])

#         # NID
#         page.get_by_role("textbox", name="National ID No.").fill(teacher["nid"])

#         # Save
#         page.get_by_role("button", name="Save").click()

#         page.wait_for_timeout(1000)

#     # Close
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
import random
from playwright.sync_api import Playwright, sync_playwright

# ---------- Auto Name Generator ----------
english_names = [
    "Abdul", "Rahim", "Karim", "Jamil", "Fahim", "Naim", "Hasan", "Rakib",
    "Sajid", "Imran", "Ridwan", "Shahid", "Anis", "Nasim", "Taslim",
    "Hafiz", "Kamrul", "Jubair", "Adnan", "Mamun", "Sohail", "Tariq",
    "Farhan", "Tanvir", "Mahbub", "Sarwar", "Ashik", "Mizan", "Rashid",
    "Noman", "Faisal", "Shakil", "Samiul", "Kawsar", "Rayhan", "Masud",
    "Habib", "Ashraf", "Shahadat", "Jalal", "Hamid", "Amin", "Sabbir",
    "Arif", "Khalid", "Rafiq", "Ismail", "Aziz", "Zia"
]

bengali_names = [
    "রহিম", "করিম", "জামিল", "ফাহিম", "নাঈম", "হাসান", "রাকিব", "সাজিদ",
    "ইমরান", "রিদওয়ান", "শাহিদ", "আনিস", "নাসিম", "তাসলিম", "হাফিজ",
    "কামরুল", "জুবায়ের", "আদনান", "মামুন", "সোহাইল", "তারিক", "ফারহান",
    "তানভীর", "মাহবুব", "সরোয়ার", "আশিক", "মিজান", "রশিদ", "নোমান",
    "ফয়সাল", "শাকিল", "সামিউল", "কাউসার", "রায়হান", "মাসুদ", "হাবিব",
    "আশরাফ", "শাহাদাত", "জালাল", "হামিদ", "আমিন", "সাব্বির", "আরিফ",
    "খালিদ", "রফিক", "ইসমাইল", "আজিজ", "জিয়া"
]


def generate_teacher(i):
    name_en = english_names[i - 1]
    name_bn = bengali_names[i - 1]

    return {
        "name_en": f"{name_en}",
        "name_bn": f"{name_bn}",
        "email": f"{name_en.lower()}{i}@school.com",
        "mobile": f"01{random.randint(5,9)}{random.randint(10000000,99999999)}",
        "nid": str(random.randint(1000000000, 9999999999)),
        "employee_code": f"EMP{i:03d}"
    }


# ----------------------------- Main Script -----------------------------
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("http://192.168.1.227:5173/")
    page.get_by_label("Username").fill("super")
    page.get_by_label("Password").fill("654321")
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_load_state("networkidle")

    # Open Teacher Page
    page.locator("li").filter(has_text="User Management").get_by_role("button").click()
    page.get_by_role("link", name="Teacher").click()
    page.wait_for_load_state("networkidle")

    # Loop 50 teachers
    for i in range(1, 51):
        teacher = generate_teacher(i)

        page.get_by_role("button", name="Add Teacher").click()
        page.wait_for_selector('input[placeholder="Name (English)"]')

        # Fill Form
        page.get_by_placeholder("Name (English)").fill(teacher["name_en"])
        page.get_by_placeholder("Name (Bengali)").fill(teacher["name_bn"])
        page.get_by_placeholder("Email").fill(teacher["email"])
        page.get_by_placeholder("Mobile Number").fill(teacher["mobile"])
        page.get_by_label("Date of Birth").fill("1990-01-01")

        # Gender (Male)
        page.locator("button").filter(has_text="Select gender").click()
        page.get_by_label("Male", exact=True).click()

        # Blood group
        page.locator("button").filter(has_text="Select blood group").click()
        page.get_by_label("A+").click()

        # Religion
        page.locator("button").filter(has_text="Select religion").click()
        page.get_by_label("Islam").click()

        page.get_by_placeholder("Employee Code").fill(teacher["employee_code"])

        # Designation
        page.locator("button").filter(has_text="Select Designation").click()
        page.get_by_label("Assistant Teacher").click()

        page.get_by_label("Joining Date").fill("2025-01-01")
        page.get_by_placeholder("National ID No.").fill(teacher["nid"])

        # Save
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(1500)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

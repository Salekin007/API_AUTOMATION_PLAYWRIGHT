import random
import re
from playwright.sync_api import Playwright, sync_playwright


# ----------- Name Generators -----------
english_guardian_names = [
    "Korim", "Habib", "Salam", "Nazrul", "Hashem", "Bashir", "Jalal", "Arman",
    "Sattar", "Motaleb", "Jabbar", "Latif", "Samad", "Kuddus", "Harun",
    "Khalil", "Aziz", "Ahad", "Shamsu", "Soleman"
]

bengali_guardian_names = [
    "করিম", "হাবিব", "সালাম", "নজরুল", "হাশেম", "বাসির", "জালাল", "আর্মান",
    "সাত্তার", "মতলব", "জব্বার", "লতিফ", "সমাদ", "কুদ্দুস", "হারুন",
    "খলিল", "আজিজ", "আহাদ", "শামসু", "সোলেমান"
]


def generate_data(i):
    return {
        "name_en": english_guardian_names[i],
        "name_bn": bengali_guardian_names[i],
        "email": f"guardian{i+1}@gmail.com",
        "mobile": f"01{random.randint(5,9)}{random.randint(10000000,99999999)}",
        "nid": str(random.randint(1000000000, 9999999999)),
    }


# ---------------- MAIN SCRIPT ----------------
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

    # Go to guardian page
    page.locator("#root").get_by_text("User Management").click()
    page.get_by_role("link", name="Guardian").click()
    page.wait_for_load_state("networkidle")

    # Starting Student ID
    start_student_num = 10  # SD00010

    # Create 20 guardians
    for i in range(20):
        student_num = start_student_num + i
        student_id = f"SD{student_num:05d}"

        data = generate_data(i)

        page.get_by_role("button", name="Add Guardian").click()
        page.wait_for_timeout(1000)

        # ------------ SELECT STUDENT ------------
        page.locator("div").filter(has_text=re.compile(r"^Student$")).get_by_role("button").click()

        # Student row locator format EXACTLY matches your UI Example:
        # "Select row SD00010 Imran"
        row_name = f"Select row {student_id}"
        page.get_by_role("row", name=re.compile(row_name)).get_by_role("cell").first.click()

        # ------------ SELECT STUDENT ID ------------
        page.get_by_role("button", name="Student ID").click()
        page.get_by_role("row", name=re.compile(row_name)).get_by_label("Select row").click()

        # Save selected student
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(1200)

        # ------------ FILL GUARDIAN FORM ------------
        page.get_by_label("Name (English)").fill(data["name_en"])
        page.get_by_label("Name (Bengali)").fill(data["name_bn"])

        # Gender
        page.locator("button").filter(has_text="Select gender").click()
        page.get_by_label("Male", exact=True).click()

        # DOB
        page.get_by_label("Date of Birth").fill("1980-01-01")

        # Religion
        page.locator("button").filter(has_text="Select religion").click()
        page.get_by_label("Islam").click()

        # Blood Group
        page.locator("button").filter(has_text="Select blood group").click()
        page.get_by_label("A+").click()

        # Relation
        page.locator("button").filter(has_text="Select relation").click()
        page.get_by_label("Father").click()

        # NID, Email, Mobile
        page.get_by_label("National ID No.").fill(data["nid"])
        page.get_by_label("Email").fill(data["email"])
        page.get_by_label("Mobile Number").fill(data["mobile"])

        # Final Save
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(1500)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

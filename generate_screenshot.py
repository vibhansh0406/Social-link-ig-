from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    file_path = f"file://{os.path.abspath('index.html')}"
    page.goto(file_path)
    page.wait_for_timeout(2500)

    os.makedirs("verification", exist_ok=True)
    page.screenshot(path="verification/glass_nav.png")
    browser.close()

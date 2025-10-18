import os
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the local HTML file
    url = "http://localhost:8000/index.html"
    print(f"Navigating to {url}")
    page.goto(url)

    # Wait for the video to be present
    page.wait_for_selector('#hero-video')
    page.wait_for_timeout(5000) # 5 seconds

    # Take a screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
import os
from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.parametrize("pw_browser", ["chromium", "firefox", "webkit"])
def test_Login(pw_browser):
    print(f"\nRunning test on browser: {pw_browser.upper()}")

    headless = os.getenv("CI") == "true"  # CI=true is set by GitHub Actions

    with sync_playwright() as p:
        browser = getattr(p, pw_browser).launch(
            headless=headless,
            slow_mo=0
        )
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.wait_for_timeout(400)
        page.fill('input[id="user-name"]', 'standard_user')
        page.fill('input[id="password"]', 'secret_sauce')
        login_button = page.locator('input[id="login-button"]')
        expect(login_button).to_be_visible()
        expect(login_button).to_be_enabled()
        login_button.click()
        browser.close()
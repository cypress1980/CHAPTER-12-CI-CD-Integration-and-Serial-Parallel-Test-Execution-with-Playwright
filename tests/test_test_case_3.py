from playwright.sync_api import sync_playwright, expect
import pytest
@pytest.mark.parametrize("pw_browser", ["chromium", "firefox", "webkit"])
def test_Login(pw_browser):
    print(f"\n Running test on browser: {pw_browser.upper()}")
    with sync_playwright() as p:
        browser = getattr(p, pw_browser).launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', 'demo')
        login_button = page.locator('button[id="loginBtn"]')
        expect(login_button).to_be_visible()
        expect(login_button).to_be_enabled()
        login_button.click()
        browser.close()
from playwright.sync_api import sync_playwright
def test_browser_contexts_independent_sessions():
    with sync_playwright() as p:
        # Launch a single browser instance
        browser = p.chromium.launch(headless=False)  # Use headless=True in CI

        # -------- Context 1: QA Automation Labs Shop --------
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://shop.qaautomationlabs.com/index.php")
        page1.fill('input[id="email"]', 'demo@demo.com')
        page1.fill('input[id="password"]', 'demo')
        page1.click('button[id="loginBtn"]')
        page1.wait_for_load_state("networkidle")
        page1.screenshot(path="screenshot_shop_logged_in.png")

        # -------- Context 2: SauceDemo --------
        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://www.saucedemo.com/")
        page2.fill('input[id="user-name"]', 'standard_user')
        page2.fill('input[id="password"]', 'secret_sauce')
        page2.click('input[id="login-button"]')
        page2.wait_for_load_state("networkidle")
        page2.screenshot(path="screenshot_saucedemo_logged_in.png")

        # Observation wait
        page1.wait_for_timeout(5000)
        page2.wait_for_timeout(5000)

        # Cleanup
        context1.close()
        context2.close()
        browser.close()
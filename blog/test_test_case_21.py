from playwright.sync_api import sync_playwright, expect

def test_Login():
    browser_name = "CHROMIUM"
    print(f"\n🌐 Running test on browser: {browser_name}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', 'demo')
        login_button = page.locator('button[id="loginBtn"]')
        expect(login_button).to_be_visible()
        expect(login_button).to_be_enabled()
        login_button.click()
        browser.close()
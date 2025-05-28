import pytest
from playwright.sync_api import expect
EXPECTED_TITLE = "Fast and reliable end-to-end testing for modern web apps | Playwright"
LINK = "https://playwright.dev/"
@pytest.mark.parametrize("browser_type", ["chromium", "firefox"])
def test_page_title(browser_type, playwright):
    if browser_type == "chromium":
        browser = playwright.chromium.launch()
    elif browser_type == "firefox":
        browser = playwright.firefox.launch()
    else:
        pytest.fail(f"Unsupported browser type: {browser_type}")
    # Создаем контекст и страницу
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto(LINK)
        expect(page).to_have_title(EXPECTED_TITLE)        
    finally:
        context.close()
        browser.close()

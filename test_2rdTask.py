import pytest
from playwright.sync_api import expect, Playwright


EXPECTED_TITLE: str = "Fast and reliable end-to-end testing for modern web apps | Playwright"
LINK: str = "https://playwright.dev/"


@pytest.mark.parametrize("browser_type", ["chromium", "firefox"])
def test_page_title(browser_type, playwright):
    """
    Verifies that the page title matches the expected value for the specified browser type.

    Args:
        browser_type (str): The type of browser to launch ("chromium" or "firefox").
        playwright (Playwright): A Playwright instance used to launch browser instances.

    Raises:
        pytest.fail: If an unsupported browser type is provided.

    Usage Example:
        test_page_title("chromium", playwright)
    """
    if browser_type == "chromium":
        browser = playwright.chromium.launch()
    elif browser_type == "firefox":
        browser = playwright.firefox.launch()
    else:
        pytest.fail(f"Unsupported browser type: {browser_type}")
    
	# Create a new context and page
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto(LINK)
        expect(page).to_have_title(EXPECTED_TITLE)        
    finally:
        context.close()
        browser.close()
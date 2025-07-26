import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        is_ci = os.getenv("CI") == "true"
        browser = p.chromium.launch(headless=is_ci)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
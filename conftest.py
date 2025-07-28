import pytest
import base64
import os 
import pytest_html
from datetime import datetime
from pathlib import Path
from pytest_metadata.plugin import metadata_key 
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def playwright_instance():
    """Initialize Playwright once for the entire test session."""
    with sync_playwright() as p:
        yield p



@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launch the browser."""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    """Create a fresh page for each test."""
    page = browser.new_page(ignore_https_errors=True)
    yield page
    page.close()

@pytest.fixture(scope="session")
def normalize_number():
    def _normalize(value):
        return value.replace(".", "").strip() if value.replace(".", "").isdigit() else value.strip()
    
    return _normalize

def pytest_configure(config):
    config.option.htmlpath = "report.html"
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Fixture to print test case result (Pass/Fail) in the report."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        if report.failed:
            print(f"❌ Test case '{item.name}' FAILED!")
        else:
            print(f"✅ Test case '{item.name}' PASSED!")


@pytest.hookimpl(hookwrapper=True)  
def pytest_runtest_makereport(item):  
    outcome = yield  
    report = outcome.get_result()  
    extra = getattr(report, "extra", [])  

    if report.when == "call":  
        test_name = item.name
        screenshot_dir = os.getenv("SCREENSHOT_PATH", "screenshots")

        # Pastikan screenshot optional dan foldernya ada
        if not os.path.exists(screenshot_dir):
            print(f"Screenshot directory '{screenshot_dir}' not found. Skipping screenshot attachment.")
        else:
            screenshot_files = sorted([
                f for f in os.listdir(screenshot_dir) 
                if f.startswith(test_name) and f.endswith(".png")
            ])

            if screenshot_files:
                for screenshot_file in screenshot_files:
                    screenshot_path = os.path.join(screenshot_dir, screenshot_file)
                    try:
                        with open(screenshot_path, "rb") as image_file:
                            encoded_string = base64.b64encode(image_file.read()).decode()
                            extra.append(pytest_html.extras.png(encoded_string))
                        report.extra = extra
                    except Exception as e:
                        print(f"Error reading screenshot {screenshot_path}: {e}")
            else:
                print(f"No screenshot found for test: {test_name}")
            if report.failed:
                print(f"❌ Test case '{item.name}' FAILED!")
            else:
                print(f"✅ Test case '{item.name}' PASSED!")

def pytest_html_report_title(report):  
    report.title = "Bersama Loyalty Automation Report"

@pytest.fixture
def check_expectation():
    """Fixture to check element existence, visibility, text, and handle assertions."""
    def _check(page, description:str, locator, expected_text=None, check_visibility=False):
        """Perform multiple assertions based on the parameters."""
        try:
            if check_visibility:  # Check if element is visible
                assert locator.is_visible(), f"❌ {description} is NOT visible!"
                print(f"✅ {description} is visible!")
            elif expected_text:  # Check if element contains specific text
                expect(locator).to_have_text(expected_text)
                print(f"✅ {description}: Expected text '{expected_text}' is present!")
            else:  # Default check: Ensure the element exists
                assert locator.count() > 0, f"❌ {description} does NOT exist!"
                print(f"✅ {description} exists!")

        except AssertionError as e:
            print(f"❌ {description} failed! Error: {e}")

            # ✅ Capture screenshot on failure
            screenshot_path = f"screenshots/{description.replace(' ', '_')}.png"
            page.screenshot(path=screenshot_path)
            print(f"📸 Screenshot saved at {screenshot_path}")

            pytest.fail(f"Test failed: {description}")  # Fails the test case in pytest

    return _check

def pytest_configure(config):  
    config.stash[metadata_key]["Project"] = "Playwright Python - Bersama Loyalty"
    config.stash[metadata_key]["Base URL"] = "https://staging-loyalty.bersama.id"

def pytest_html_results_summary(prefix, summary, postfix):
    # Inject custom CSS to resize the div.media
    prefix.extend([
        '<style>',
        #Resize the div.media container 
        '.media {',
        '    width: 640px; /* 2x original width */',
        '    height: 480px; /* 2x original height */',
        '    overflow: hidden; /* Ensure content fits */',
        '}',

        # /* Resize images inside the div.media */
        '.media img {',
        '    max-width: 100%; /* Ensure images fit within the container */',
        '    max-height: 100%;',
        '    width: auto;',
        '    height: auto;',
        '}',
        '</style>'
    ])

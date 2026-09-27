import pytest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader
from utils.logger import get_logger


# ---------------------------------------------------------
# Global configuration and logger
# ---------------------------------------------------------

config = ConfigReader()
logger = get_logger()


# ---------------------------------------------------------
# PyTest WebDriver Fixture
# ---------------------------------------------------------

@pytest.fixture
def driver(request):

    browser = config.get(
        "application",
        "browser"
    ).lower()

    headless = config.get_boolean(
        "application",
        "headless"
    )

    # -----------------------------------------------------
    # Browser Configuration
    # -----------------------------------------------------

    if browser == "chrome":

        options = Options()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")

        driver = webdriver.Chrome(
            options=options
        )

    elif browser == "edge":

        from selenium.webdriver.edge.options import Options as EdgeOptions

        options = EdgeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

        driver = webdriver.Edge(
            options=options
        )

    else:

        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    # -----------------------------------------------------
    # Browser Settings
    # -----------------------------------------------------

    implicit_wait = config.get_int(
        "application",
        "implicit_wait"
    )

    driver.implicitly_wait(
        implicit_wait
    )

    # -----------------------------------------------------
    # Launch Application
    # -----------------------------------------------------

    base_url = config.get(
        "application",
        "base_url"
    )

    driver.get(base_url)

    logger.info(
        f"Browser started: {browser}"
    )

    logger.info(
        f"Application launched: {base_url}"
    )

    # -----------------------------------------------------
    # Execute Test
    # -----------------------------------------------------

    yield driver

    # -----------------------------------------------------
    # Screenshot Handling
    # -----------------------------------------------------

    if hasattr(request.node, "rep_call"):

        screenshot_root = Path(
            config.get(
                "report",
                "screenshot_dir"
            )
        )

        # -------------------------------------------------
        # FAILURE SCREENSHOT
        # -------------------------------------------------

        if request.node.rep_call.failed:

            failure_dir = (
                screenshot_root / "failures"
            )

            failure_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            screenshot_path = (
                failure_dir /
                f"{request.node.name}.png"
            )

            driver.save_screenshot(
                str(screenshot_path)
            )

            logger.error(
                f"Test failed. Screenshot saved: "
                f"{screenshot_path}"
            )

        # -------------------------------------------------
        # SUCCESSFUL TEST EVIDENCE
        # -------------------------------------------------

        elif request.node.rep_call.passed:

            evidence_dir = (
                screenshot_root / "evidence"
            )

            evidence_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            screenshot_path = (
                evidence_dir /
                f"{request.node.name}.png"
            )

            driver.save_screenshot(
                str(screenshot_path)
            )

            logger.info(
                f"Test passed. Evidence screenshot saved: "
                f"{screenshot_path}"
            )

    # -----------------------------------------------------
    # Browser Cleanup
    # -----------------------------------------------------

    driver.quit()

    logger.info(
        "Browser closed successfully"
    )


# ---------------------------------------------------------
# PyTest Hook
# Required to access test result inside fixture
# ---------------------------------------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )
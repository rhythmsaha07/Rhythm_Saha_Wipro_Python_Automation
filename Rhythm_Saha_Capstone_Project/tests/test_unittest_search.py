import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from utils.config_reader import ConfigReader
from utils.logger import get_logger


class TestProductSearch(unittest.TestCase):

    # -----------------------------------------------------
    # Test Setup
    # -----------------------------------------------------

    @classmethod
    def setUpClass(cls):

        cls.config = ConfigReader()
        cls.logger = get_logger()

        browser = cls.config.get(
            "application",
            "browser"
        ).lower()

        if browser != "chrome":

            raise unittest.SkipTest(
                "Unittest implementation currently uses Chrome."
            )

        # -------------------------------------------------
        # Browser Configuration
        # -------------------------------------------------

        options = Options()

        options.add_argument(
            "--start-maximized"
        )

        options.add_argument(
            "--disable-notifications"
        )

        options.add_argument(
            "--disable-popup-blocking"
        )

        # -------------------------------------------------
        # Start Browser
        # -------------------------------------------------

        cls.driver = webdriver.Chrome(
            options=options
        )

        # -------------------------------------------------
        # Browser Settings
        # -------------------------------------------------

        implicit_wait = cls.config.get_int(
            "application",
            "implicit_wait"
        )

        cls.driver.implicitly_wait(
            implicit_wait
        )

        # -------------------------------------------------
        # Launch Application
        # -------------------------------------------------

        base_url = cls.config.get(
            "application",
            "base_url"
        )

        cls.driver.get(
            base_url
        )

        cls.logger.info(
            f"Unittest browser started: {browser}"
        )

        cls.logger.info(
            f"Unittest application launched: {base_url}"
        )

    # -----------------------------------------------------
    # Product Search Test
    # -----------------------------------------------------

    def test_product_search_using_unittest(self):

        home_page = HomePage(
            self.driver
        )

        try:

            # -------------------------------------------------
            # Open Products
            # -------------------------------------------------

            home_page.open_products()

            # -------------------------------------------------
            # Search Product
            # -------------------------------------------------

            home_page.search_product(
                "dress"
            )

            # -------------------------------------------------
            # Successful Test Evidence
            # -------------------------------------------------

            screenshot_root = Path(
                self.config.get(
                    "report",
                    "screenshot_dir"
                )
            )

            evidence_dir = (
                screenshot_root / "evidence"
            )

            evidence_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            screenshot_path = (
                evidence_dir /
                "test_product_search_using_unittest.png"
            )

            self.driver.save_screenshot(
                str(screenshot_path)
            )

            self.logger.info(
                f"Unittest evidence screenshot saved: "
                f"{screenshot_path}"
            )

            # -------------------------------------------------
            # Assertions
            # -------------------------------------------------

            self.assertTrue(
                home_page.search_results_displayed(),
                "SEARCHED PRODUCTS section was not displayed."
            )

            self.assertGreater(
                home_page.product_count(),
                0,
                "No products were found for the search."
            )

        except Exception:

            # -------------------------------------------------
            # Unittest Failure Screenshot
            # -------------------------------------------------

            screenshot_root = Path(
                self.config.get(
                    "report",
                    "screenshot_dir"
                )
            )

            failure_dir = (
                screenshot_root / "failures"
            )

            failure_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            screenshot_path = (
                failure_dir /
                "test_product_search_using_unittest.png"
            )

            self.driver.save_screenshot(
                str(screenshot_path)
            )

            self.logger.error(
                f"Unittest failed. Failure screenshot saved: "
                f"{screenshot_path}"
            )

            # Re-raise the exception so unittest/PyTest
            # correctly reports the test as failed.

            raise

    # -----------------------------------------------------
    # Test Teardown
    # -----------------------------------------------------

    @classmethod
    def tearDownClass(cls):

        if hasattr(cls, "driver"):

            cls.driver.quit()

            cls.logger.info(
                "Unittest browser closed successfully"
            )


# ---------------------------------------------------------
# Direct unittest execution
# ---------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
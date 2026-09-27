from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class HomePage(BasePage):

    # -----------------------------
    # Navigation
    # -----------------------------

    PRODUCTS_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Products')]"
    )

    PRODUCTS_URL = "https://automationexercise.com/products"

    # -----------------------------
    # Google Vignette Advertisement
    # -----------------------------

    VIGNETTE_IFRAME = (
        By.CSS_SELECTOR,
        "iframe[name^='aswift_']"
    )

    # Google ads can contain another iframe
    AD_IFRAME = (
        By.CSS_SELECTOR,
        "iframe[name='ad_iframe']"
    )

    VIGNETTE_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "#dismiss-button"
    )

    # -----------------------------
    # Product Search
    # -----------------------------

    SEARCH_INPUT = (
        By.NAME,
        "search"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    SEARCH_RESULTS_HEADER = (
        By.XPATH,
        "//h2[contains("
        "translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
        "'abcdefghijklmnopqrstuvwxyz'),"
        "'searched products'"
        ")]"
    )

    PRODUCT_RESULTS = (
        By.CSS_SELECTOR,
        ".features_items .product-image-wrapper"
    )

    # -----------------------------
    # Close Google Vignette
    # -----------------------------

    def close_vignette_ad(self):

        self.driver.switch_to.default_content()

        # Find all possible Google ad iframes
        iframes = self.driver.find_elements(
            By.CSS_SELECTOR,
            "iframe[name^='aswift_']"
        )

        for iframe in iframes:

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(iframe)

                # Some Google ads contain a nested ad iframe
                nested_iframes = self.driver.find_elements(
                    By.CSS_SELECTOR,
                    "iframe[name='ad_iframe']"
                )

                if nested_iframes:

                    self.driver.switch_to.frame(
                        nested_iframes[0]
                    )

                close_buttons = self.driver.find_elements(
                    By.CSS_SELECTOR,
                    "#dismiss-button"
                )

                for button in close_buttons:

                    if button.is_displayed():

                        self.driver.execute_script(
                            "arguments[0].click();",
                            button
                        )

                        self.driver.switch_to.default_content()

                        return True

            except Exception:

                self.driver.switch_to.default_content()
                continue

        self.driver.switch_to.default_content()

        return False

    # -----------------------------
    # Open Products Page
    # -----------------------------

    def open_products(self):

        self.driver.switch_to.default_content()

        # ---------------------------------
        # STEP 1: Try to close advertisement
        # ---------------------------------

        self.close_vignette_ad()

        self.driver.switch_to.default_content()

        # ---------------------------------
        # STEP 2: Locate Products
        # ---------------------------------

        product_link = self.wait.until(
            EC.presence_of_element_located(
                self.PRODUCTS_LINK
            )
        )

        # ---------------------------------
        # STEP 3: Scroll to Products
        # ---------------------------------

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            product_link
        )

        # ---------------------------------
        # STEP 4: Normal Selenium click
        # ---------------------------------

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.PRODUCTS_LINK
                )
            )

            product_link.click()

        except Exception:

            # JavaScript fallback
            self.driver.execute_script(
                "arguments[0].click();",
                product_link
            )

        # ---------------------------------
        # STEP 5: Give navigation a short
        # opportunity to complete
        # ---------------------------------

        try:

            WebDriverWait(
                self.driver,
                5
            ).until(
                lambda driver:
                "/products" in driver.current_url.lower()
            )

        except TimeoutException:

            # ---------------------------------
            # STEP 6: Advertisement may have
            # blocked navigation
            # ---------------------------------

            self.close_vignette_ad()

            self.driver.switch_to.default_content()

            # Try the Products link once more
            try:

                product_link = self.driver.find_element(
                    *self.PRODUCTS_LINK
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    product_link
                )

                WebDriverWait(
                    self.driver,
                    5
                ).until(
                    lambda driver:
                    "/products" in driver.current_url.lower()
                )

            except Exception:

                # ---------------------------------
                # STEP 7: Controlled URL fallback
                # ---------------------------------

                self.driver.get(
                    self.PRODUCTS_URL
                )

        # ---------------------------------
        # STEP 8: Make sure main document
        # is active
        # ---------------------------------

        self.driver.switch_to.default_content()

        # ---------------------------------
        # STEP 9: Final verification
        # ---------------------------------

        self.wait.until(
            lambda driver:
            "/products" in driver.current_url.lower()
        )

        # ---------------------------------
        # STEP 10: Wait for Search box
        # ---------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

    # -----------------------------
    # Search Product
    # -----------------------------

    def search_product(self, product_name):

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        search_box.clear()

        search_box.send_keys(
            product_name
        )

        search_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        )

        search_button.click()

        # Wait for search URL
        self.wait.until(
            lambda driver:
            "search=" in driver.current_url.lower()
        )

    # -----------------------------
    # Verify Search Results
    # -----------------------------

    def search_results_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_RESULTS_HEADER
            )
        ).is_displayed()

    # -----------------------------
    # Count Products
    # -----------------------------

    def product_count(self):

        products = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_RESULTS
            )
        )

        return len(products)
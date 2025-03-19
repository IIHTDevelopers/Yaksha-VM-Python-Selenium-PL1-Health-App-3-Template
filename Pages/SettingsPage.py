from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.settings = {
            "settings_link": (By.CSS_SELECTOR, 'a[href="#/Settings"]'),
            "more_dropdown": (By.XPATH, '//a[contains(text(),"More...")]'),
            "price_category_tab": (By.CSS_SELECTOR, 'ul.dropdown-menu a[href="#/Settings/PriceCategory"]'),
            "activate_success_message": (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Activated."]'),
            "deactivate_success_message": (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Deactivated."]'),
        }

    def verify_occupied_bed_edit(self):
        """
        /**
        * @Test9
        * @description This method verifies that an error message is displayed when attempting to edit an occupied bed.
        * @expected
        * An error message should appear stating: "Cannot modify occupied beds."
        */
        """
        pass
        assert False, "TODO: Implement verify_occupied_bed_edit"
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from datetime import datetime

class DispensaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

        self.dispensaryLink = (By.CSS_SELECTOR, 'a[href="#/Dispensary"]')
        self.newPatient_modal = (By.XPATH, '//span[text()="Add New Patient"]')
        self.activateCounter = (By.XPATH, "//a[contains(text(),'Counter')]")
        self.activate_counter_link = (By.XPATH, "//h5[contains(text(),'Morning Counter')]"),
        self.counterSelection = (By.XPATH, '//div[@class="counter-item"]')
        self.counterName = (By.XPATH, '//div[@class="counter-item"]//h5')
        self.activatedCounterInfo = (By.CSS_SELECTOR, "div.mt-comment-info")
        self.deactivateCounterButton = (By.XPATH, "//button[contains(text(), 'Deactivate Counter')]")
        self.titleName = (By.XPATH, '//span[@class="caption-subject"]')
        self.name = (By.XPATH, '(//div[@class="col-sm-4 col-md-3"]//label//span)[1]')
        self.prescription = (By.XPATH, "//a[contains(text(),' Prescription ')]")
        self.reports = (By.XPATH, "//a[contains(text(), 'Reports')]")
        self.fromDate = (By.XPATH, '(//input[@id="date"])[1]')
        self.showReportButton = (By.XPATH, "//span[text()='Show Report']")
        self.userCollectionReport = (By.XPATH, "//i[text()='User Collection']")
        self.counterDropdown = (By.CSS_SELECTOR, "select#ddlCounter")
        self.counterNameFromTable = (By.CSS_SELECTOR, "div[col-id='CounterName']")

    def verify_active_counter_message_in_dispensary(self):
        """
        /**
        * @Test2
        * @description This method navigates to the Dispensary module and checks if counters are available.
        *              If counters exist, it selects one at random, activates it, and verifies that the activation
        *              message correctly displays the name of the selected counter.
        */
        """
        pass
        assert False, "TODO: Implement verify_active_counter_message_in_dispensary"

    def activate_counter_and_select_sale(self):
        """
        /**
        * @Test10
        * @description This method verifies the activation of a counter and selects the Sale tab using Alt + N.
        * @expected
        * The Sale tab should be selected after pressing Alt + N.
        */
        """
        pass
        assert False, "TODO: Implement activate_counter_and_select_sale"

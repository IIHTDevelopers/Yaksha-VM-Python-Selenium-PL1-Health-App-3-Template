import os

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PatientPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.patient = {
            "patient_link": (By.CSS_SELECTOR, 'a[href="#/Patient"]'),
            "search_bar": (By.CSS_SELECTOR, "#quickFilterInput"),
            "register_patient": (By.CSS_SELECTOR, 'ul.page-breadcrumb a[href="#/Patient/RegisterPatient"]'),
            "new_photo_button": (By.XPATH, '//button[contains(text(),"New Photo")]'),
            "upload_button": (By.CSS_SELECTOR, 'label[for="fileFromLocalDisk"]'),
            "done_button": (By.XPATH, '//button[text()="Done"]'),
            "uploaded_img": (By.CSS_SELECTOR, 'div.wrapper img'),
            "profile_picture_icon": (By.CSS_SELECTOR, 'a[title="Profile Picture"]'),
        }

    def search_and_verify_patients(self, patient_data):
        """
        /**
        * @Test6
        * @description This method navigates to the patient section, iterates over a predefined list of patients,
        *              and performs a search operation for each patient name. After each search, it verifies that the
        *              search result matches the expected patient name. Returns True if all patient searches are verified
        *              successfully; returns False if an error occurs.
        */
        """
        pass
        assert False, "TODO: Implement search_and_verify_patients"
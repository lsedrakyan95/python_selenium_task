from selenium.webdriver.common.by import By

class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_id = (By.ID, "get-in-touch-form-first_name")
        self.last_name_id = (By.ID, "get-in-touch-form-last_name")
        self.email_id = (By.ID, "get-in-touch-form-email")
        self.terms_conditions_checkbox_name = (By.NAME, "terms")
        self.subscribe_checkbox_name = (By.NAME, "subscribe[]")
        self.submit_xpath = (By.XPATH, "//input[@value='Submit']")

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name_id).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name_id).send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element(*self.email_id).send_keys(email)

    def accept_terms_conditions(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.terms_conditions_checkbox_name))

    def accept_subscribtion(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.subscribe_checkbox_name))

    def is_submit_button_disabled(self):
        return self.driver.find_element(*self.submit_xpath).get_attribute("disabled") == 'true'
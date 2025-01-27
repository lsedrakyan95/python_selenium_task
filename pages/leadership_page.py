from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeadershipPage:
    def __init__(self, driver):
        self.driver = driver
        self.about_header_link_xpath = (By.XPATH,
            "//div[contains(@class, 'team-grid__info--name')]//p[text()='{}']")
        self.person_details_xpath = (By.XPATH,
            "//div[contains(@style, 'opacity: 1') and contains(@style, 'visibility: visible')]" +
            "//div[@class='team-grid__modal-content-bio']/p")

    def open_person_details(self, person_name):
        person_locator = (self.about_header_link_xpath[0],
                          self.about_header_link_xpath[1].format(person_name))
        self.driver.find_element(*person_locator).click()

    def get_person_details(self):
        person_details = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.person_details_xpath)
        )
        return person_details.text

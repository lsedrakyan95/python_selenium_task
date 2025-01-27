
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.leadership_page import LeadershipPage
from pages.contact_page import ContactPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.accept_cookies_id = (By.ID, "onetrust-accept-btn-handler")
        self.about_header_link_xpath = (By.XPATH,
            "//a[@href='https://www.griddynamics.com/about']")
        self.leadership_header_link_xpath = (By.XPATH,
            "//a[@href='https://www.griddynamics.com/leadership']")
        self.filter_article_topics_id = (By.ID, "sub-category-list")
        self.filter_article_topic_xpath = (By.XPATH,
            "//div[@id='sub-category-list']//span[contains(text(),'{}')]")
        self.article_titles_css = (By.CSS_SELECTOR,
            ".blog-page__feed .blog-page__post-item .regular__title h3")
        self.get_in_touch_xpath = (By.XPATH,
            "//a[@href='https://www.griddynamics.com/contact']")

    def load_homepage(self):
        self.driver.get("https://blog.griddynamics.com")
        self.accept_cookies()

    def open_leadership_page(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.about_header_link_xpath)).perform()
        leadership_header_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.leadership_header_link_xpath)
        )
        leadership_header_link.click()
        return LeadershipPage(self.driver)

    def filter_articles_by_topic(self, topic):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.filter_article_topics_id)).perform()
        filter_article_topics = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.filter_article_topics_id)
        )
        filter_article_topics.click()
        filter_article_topic_xpath_formatted =(self.filter_article_topic_xpath[0],
            self.filter_article_topic_xpath[1].format(topic))
        filter_article_topic = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(filter_article_topic_xpath_formatted)
        )
        filter_article_topic.click()

    def get_article_titles(self):
        title_elements = self.driver.find_elements(*self.article_titles_css)
        return [e.get_attribute("innerHTML") for e in title_elements]

    def open_contact_page(self):
        self.driver.find_element(*self.get_in_touch_xpath).click()
        return ContactPage(self.driver)

    def accept_cookies(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.accept_cookies_id)
        )
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.accept_cookies_id)
        )

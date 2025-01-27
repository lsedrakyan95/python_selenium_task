import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.homepage import HomePage

@pytest.fixture(name="driver")
def driver_fixture():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture(name="homepage")
def homepage_fixture(driver):
    page = HomePage(driver)
    page.load_homepage()
    return page

@allure.story("Case #1")
def test_case_1(homepage):
    leadership_page = homepage.open_leadership_page()
    leadership_page.open_person_details('Leonard Livschitz')
    actual_text = leadership_page.get_person_details()

    assert 'Chief Executive Officer of Grid Dynamics, a NASDAQ-listed company' in actual_text

@allure.story("Case #2")
def test_case_2(homepage):
    homepage.filter_articles_by_topic('Cloud and DevOps')
    titles_cloud = homepage.get_article_titles()
    assert len(titles_cloud) > 1

    homepage.filter_articles_by_topic('All topics')
    titles_all = homepage.get_article_titles()
    assert titles_cloud[0] != titles_all[1]

@allure.story("Case #3")
def test_case_3(homepage):
    contact_page = homepage.open_contact_page()
    contact_page.fill_first_name('Anna')
    contact_page.fill_last_name('Smith')
    contact_page.fill_email('annasmith@griddynamics.com')
    # this field doesn't exist any more - select  How did you hear about us? = Online Ads
    contact_page.accept_terms_conditions()
    contact_page.accept_subscribtion()

    assert contact_page.is_submit_button_disabled()

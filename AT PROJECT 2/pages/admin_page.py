# pages/admin_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AdminPage(BasePage):
    # PAGE_TITLE = (By.TAG_NAME, 'title')
    ADMIN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
    EXPECTED_HEADER_OPTIONS = [
        'User Management',
        'Job',
        'Organization',
        'Qualifications',
        'Nationalities',
        'Corporate Branding',
        'Configuration'
    ]

    def get_page_title(self):
        return self.driver.title

    def get_header_items(self):
        try:
            elements = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li"))
            )
            return [element.text for element in elements]
        except Exception as e:
            print(f"An error occurred while fetching header items: {e}")
            return []

    def click_admin(self):
        self.click_element(self.ADMIN)

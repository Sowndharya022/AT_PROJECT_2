#pages/menu_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MenuPage(BasePage):
    DASHBOARD = (By.XPATH, '//span[text()="Dashboard"]')
    EXPECTED_MENU_OPTIONS = {
        'Admin',
        'PIM',
        'Leave',
        'Time',
        'Recruitment',
        'My Info',
        'Performance',
        'Dashboard',
        'Directory',
        'Maintenance',
        'Buzz'
    }

    def click_dashboard(self):
        self.click_element(self.DASHBOARD)

    def get_menu_items(self):
        try:
            elements = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li"))
            )
            return [element.text for element in elements]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

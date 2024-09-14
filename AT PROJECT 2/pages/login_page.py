#pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
    USERNAME_INPUT_FOR_PASSWORD_RESET = (By.XPATH, '//input[@name="username"]')
    RESET_PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
    SUCCESS_MESSAGE_FOR_PASSWORD_RESET = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/h6')
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password=None):
        self.enter_text(self.USERNAME_INPUT, username)
        if password:
            self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def initiate_password_reset(self, username):
        self.click_element(self.FORGOT_PASSWORD)
        self.enter_text(self.USERNAME_INPUT_FOR_PASSWORD_RESET, username)
        self.click_element(self.RESET_PASSWORD)

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE_FOR_PASSWORD_RESET).text

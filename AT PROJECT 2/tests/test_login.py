import pytest
import pandas as pd
from pages.login_page import LoginPage
from utils.result_writer import update_test_result


def get_login_data():
    df = pd.read_csv('data/login_data.csv')
    return [(row['username']) for _, row in df.iterrows()]


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("username", get_login_data())
    def test_forgot_password(self, username):
        login_page = LoginPage(self.driver)
        login_page.initiate_password_reset(username)

        try:
            success_message = login_page.get_success_message()
            expected_message = "Reset Password link sent successfully"
            success = success_message == expected_message
        except Exception as e:
            print(f"Error during password reset: {e}")
            success = False

        # Update test result based on the outcome
        if success:
            update_test_result("TC_PIM_01", "Passed", "Sowndharya")
        else:
            update_test_result("TC_PIM_01", "Failed", "Sowndharya")

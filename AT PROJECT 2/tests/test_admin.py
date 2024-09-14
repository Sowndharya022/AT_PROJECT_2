# tests/test_admin.py
import pytest
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from utils.result_writer import update_test_result


@pytest.mark.usefixtures("setup")
class TestAdminPage:

    def test_admin_page_headers(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        admin_page = AdminPage(self.driver)
        admin_page.click_admin()

        # # Get the page title
        # page_title = admin_page.get_page_title()

        # Get the actual header items
        header_texts = admin_page.get_header_items()

        # Expected header options
        expected_headers = set(admin_page.EXPECTED_HEADER_OPTIONS)

        # Check if all expected headers are present in the actual headers
        all_headers_displayed = all(option in header_texts for option in expected_headers)

        # Determine test success
        success = all_headers_displayed

        # Update test result
        if success:
            update_test_result("TC_PIM_02", "Passed", "Sowndharya")
        else:
            update_test_result("TC_PIM_02", "Failed", "Sowndharya")

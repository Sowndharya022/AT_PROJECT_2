#tests/test_menu.py
import pytest
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from utils.result_writer import update_test_result


@pytest.mark.usefixtures("setup")
class TestMenuPage:

    def test_menu_page_items(self):

        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        menu_page = MenuPage(self.driver)

        menu_page.click_dashboard()

        # Get the menu items from the page
        menu_items = menu_page.get_menu_items()

        # Check if all expected menu options are present
        all_menu_items_displayed = all(option in menu_items for option in menu_page.EXPECTED_MENU_OPTIONS)

        success = all_menu_items_displayed

        if success:
            update_test_result("TC_PIM_03", "Passed", "Sowndharya")
        else:
            update_test_result("TC_PIM_03", "Failed", "Sowndharya")

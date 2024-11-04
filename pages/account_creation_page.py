import testing_magento.pages.locators.account_creation_locators as loc
from testing_magento.pages.basepage import BasePage
from testing_magento.utils.test_data import generate_account_data
from testing_magento.pages.locators.account_creation_locators import success_message_locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CreationAccount(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = '/customer/account/create/'
        self.fields = {}

    def __get_all_fields(self):
        self.fields['firstname'] = self.find(loc.first_name_field_loc)
        self.fields['lastname'] = self.find(loc.last_name_field_loc)
        self.fields['email'] = self.find(loc.email_field_loc)
        self.fields['password'] = self.find(loc.password_field_loc)
        self.fields['password-confirmation'] = self.find(loc.password_confirmation_field_loc)

    def __get_success_text(self):
        return self.find(success_message_locator).text

    def fill_in_account_form_properly(self, first_name=True, last_name=True, email=True, password=True,
                                      password_confirmation=True):
        self.__get_all_fields()
        field_flags = {
            'firstname': first_name,
            'lastname': last_name,
            'email': email,
            'password': password,
            'password-confirmation': password_confirmation
        }

        account_data = generate_account_data(field_flags)

        for key, field in self.fields.items():
            if field_flags[key]:
                field.send_keys(account_data[key])

        self.find(loc.create_account_button_loc).click()

        for field_name, flag in field_flags.items():
            if not flag:
                error_element_id = f"{field_name}-error"
                error_message = WebDriverWait(self.browser, 10).until(
                    ec.visibility_of_element_located((By.ID, error_element_id))
                ).text
                assert error_message == "This is a required field.", f"Expected error message for {field_name} not found"

        if all(field_flags.values()):
            assert self.__get_success_text() == "Thank you for registering with Main Website Store.", \
                "Invalid answer when all fields are True"

    def fill_in_form_with_mismatching_password(self):
        self.__get_all_fields()
        account_data = generate_account_data(None)
        for key, field in self.fields.items():
                field.send_keys(account_data[key])
        self.find(loc.create_account_button_loc).click()
        error_message = WebDriverWait(self.browser, 10).until(
            ec.visibility_of_element_located((By.ID, "password-confirmation-error"))
        ).text
        assert error_message == "Please enter the same value again.", "Invalid answer"

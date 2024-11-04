from selenium.webdriver.common.by import By

first_name_field_loc = (By.ID, 'firstname')
last_name_field_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
password_field_loc = (By.ID, 'password')
password_confirmation_field_loc = (By.ID, 'password-confirmation')
create_account_button_loc = (By.CSS_SELECTOR, '.action.submit.primary')

#  opens in the separate page
success_message_locator = (By.CSS_SELECTOR, "div[data-ui-id='message-success'] div")

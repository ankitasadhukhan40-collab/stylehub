from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
  FIRSTNAME_INPUT = (By.CSS_SELECTOR, "[data-testid='register-firstname']")
  EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='register-email']")
  PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='register-password']")
  SUBMIT_BTN = (By.CSS_SELECTOR, "[data-testid='register-submit']")

  def register(self, firstname, email, password):
    self.enter_text(self.FIRSTNAME_INPUT, firstname)
    self.enter_text(self.EMAIL_INPUT, email)
    self.enter_text(self.PASSWORD_INPUT, password)
    self.click(self.SUBMIT_BTN)
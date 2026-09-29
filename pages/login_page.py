from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
  EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='login-email']")
  PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='login-password']")
  SUBMIT_BTN = (By.CSS_SELECTOR, "[data-testid='login-submit']")

  def login(self, email, password):
    self.enter_text(self.EMAIL_INPUT, email)
    self.enter_text(self.PASSWORD_INPUT, password)
    self.click(self.SUBMIT_BTN)
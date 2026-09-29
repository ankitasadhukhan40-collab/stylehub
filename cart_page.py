from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
  CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-testid='checkout-button']")

  def proceed_to_checkout(self):
    self.click(self.CHECKOUT_BTN)
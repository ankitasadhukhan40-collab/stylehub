from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
  ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-testid='add-to-cart']")

  def add_to_cart(self):
    self.click(self.ADD_TO_CART_BTN)
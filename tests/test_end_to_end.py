from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


def test_stylehub_full_journey(driver):
  # 1. Register a new user
  driver.get("http://127.0.0.1:5000/register")
  reg_page = RegistrationPage(driver)
  reg_page.register("John", "john@example.com", "Test@123")

  # 2. Login with the user
  driver.get("http://127.0.0.1:5000/login")
  login_page = LoginPage(driver)
  login_page.login("john@example.com", "Test@123")

  # 3. View product and add to cart
  driver.get("http://127.0.0.1:5000/product/1")
  prod_page = ProductPage(driver)
  prod_page.add_to_cart()

  # 4. Proceed to checkout from cart
  driver.get("http://127.0.0.1:5000/cart")
  cart_page = CartPage(driver)
  cart_page.proceed_to_checkout()

  assert "checkout" in driver.current_url.lower()
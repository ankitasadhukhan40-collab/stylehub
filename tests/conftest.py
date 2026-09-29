import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
  # Selenium 4+ automatically manages the driver using Selenium Manager (no webdriver-manager needed)
  driver = webdriver.Chrome()
  driver.maximize_window()
  yield driver
  driver.quit()
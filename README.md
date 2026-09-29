# stylehub
# 🛍️ STYLEHUB - Fancy Clothing E-Commerce & Selenium Automation Framework

> **"Fashion for Every You."**  
> A full-stack fashion e-commerce web application coupled with a professional, enterprise-grade Selenium WebDriver automation testing framework using Python.

---

## 🌟 Project Overview

**STYLEHUB** is designed as a capstone project for software testing, QA automation, and full-stack development portfolios. The project bridges the gap between development and testing by delivering two core pillars:
1. **The Web Application:** A fully functional, responsive, and stylish multi-category fashion e-commerce web app built with Python and Flask.
2. **The Automation Framework:** A robust Python-based test automation suite using **Selenium WebDriver**, **PyTest**, and the **Page Object Model (POM)** architectural design pattern.

---

## ✨ Key Features

### E-Commerce Web Application
* **Multi-Category Navigation:** Browse products tailored for Men, Women, Kids, and Pets.
* **Customer Authentication:** Secure user registration, encrypted password hashing, and session-based login/logout tracking.
* **Product Catalog & Details:** Real-time dynamic pricing, discounts, and size/color selection.
* **Shopping Cart & Checkout:** Live quantity calculation, subtotal adjustments, and multi-step order placement.
* **Automation-Friendly Design:** Embedded unique `data-testid` attributes across all interactive components for reliable web element targeting.

### Selenium Automation Framework
* **Page Object Model (POM):** Clean separation of test scripts, page locators, and action methods for high maintainability.
* **Native Selenium Manager:** Zero manual driver management required (fully compatible with modern Selenium 4+).
* **PyTest Fixtures:** Automated browser initialization, maximization, teardown, and setup configuration.
* **Executive HTML Reports:** Automated generation of detailed execution logs and pass/fail metrics via `pytest-html`.

---

## 📂 Project Architecture

```text
STYLEHUB_AUTOMATION/
├── app.py                      # Flask backend application and mock database
├── requirements.txt            # Project Python dependencies
├── pytest.ini                  # PyTest configuration and reporting rules
├── static/                     # Custom styles and assets
├── templates/                  # Frontend HTML templates (Bootstrap 5)
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── product.html
│   ├── cart.html
│   └── checkout.html
├── pages/                      # Page Object Model (POM) classes
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── registration_page.py
│   ├── product_page.py
│   └── cart_page.py
├── tests/                      # PyTest test suite
│   ├── __init__.py
│   ├── conftest.py             # PyTest fixtures and browser hooks
│   └── test_end_to_end.py      # Complete end-to-end customer journey tests
└── reports/                    # Generated HTML test execution reports

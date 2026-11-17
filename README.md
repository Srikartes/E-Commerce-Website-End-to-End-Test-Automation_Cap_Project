# E-Commerce Website End-to-End Test Automation

Automated UI and API test suite for [Automation Exercise](https://automationexercise.com) built using **Python**, **Playwright**, and **Pytest** following the **Page Object Model (POM)** design pattern.

---

## Project Structure

```text
E-Commerce-Website End-to-End Test Automation_1/
├── api/
│   └── ecommerce_api.py        # API client wrapper for all 8 endpoints
├── data/
│   └── test_data.json          # Externalized test data
├── pages/
│   ├── base_page.py            # Base page class with common actions
│   ├── home_page.py            # Home page navigation & footer subscription
│   ├── auth_page.py            # Registration, login, logout & account deletion
│   ├── products_page.py        # Product search, details, categories & brands
│   └── cart_page.py            # Shopping cart operations
├── tests/
│   ├── ui/                     # 15 end-to-end UI functional test cases
│   └── api/                    # 8 API test cases
├── reports/                    # Generated HTML test reports (report.html)
├── screenshots/                # Failure screenshots (captured automatically)
├── traces/                     # Playwright trace archives on failure (*.zip)
├── conftest.py                 # Pytest fixtures, ad-blocker & artifact hooks
├── pytest.ini                  # Pytest configuration & CLI defaults
└── README.md                   # Project documentation
```

---

## Features & Test Coverage

### 1. UI Functional Tests (`tests/ui/`)
1. Verify home page loads successfully
2. Register a new user
3. Verify successful account creation
4. Login with valid credentials
5. Verify login with invalid credentials
6. Logout from the application
7. Navigate to the Products page
8. Search for a product and verify results
9. View product details
10. Add a product to the cart
11. Verify product details and quantity in the cart
12. Remove a product from the cart
13. Navigate through product categories
14. Navigate through product brands
15. Verify footer newsletter subscription functionality

### 2. API Tests (`tests/api/`)
1. `GET /api/productsList` – Get all products
2. `GET /api/brandsList` – Get all brands
3. `POST /api/searchProduct` – Search products
4. `POST /api/verifyLogin` – Verify login credentials
5. `POST /api/createAccount` – Create user account
6. `PUT /api/updateAccount` – Update user account
7. `DELETE /api/deleteAccount` – Delete user account
8. `GET /api/getUserDetailByEmail` – Get user details by email

---
#### Negative & Edge-Case API Scenarios (Parametrized)
9. `POST /api/searchProduct` – Search product without `search_product` parameter (`400 Bad Request`)
10. `POST /api/verifyLogin` – Verify login with invalid credentials (`404 User not found!`)
11. `POST /api/verifyLogin` – Verify login with missing parameters (`400 Bad Request` – 3 parametrized cases: missing email, missing password, missing both)
12. Unsupported HTTP Methods (`405 Method Not Allowed` – 3 parametrized cases: `POST /api/productsList`, `PUT /api/brandsList`, `DELETE /api/verifyLogin`)

-----

## Prerequisites & Setup

1. **Install Python 3.10+**
2. **Install required packages:**
   ```bash
   pip install pytest pytest-playwright pytest-html pytest-xdist pytest-rerunfailures
   ```
3. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

---

## Running the Tests

* **Run the entire test suite (UI + API):**
  ```bash
  pytest
  ```
* **Run only UI tests:**
  ```bash
  pytest tests/ui
  ```
* **Run only API tests:**
  ```bash
  pytest tests/api
  ```
* **Run tests in headed mode (visible browser):**
  ```bash
  pytest tests/ui --headed
  ```
* **Run a single test file:**
  ```bash
  pytest tests/ui/test_08_search_product.py
  ```
pytest tests/ui -v --html=reports/ui_report.html --self-contained-html

pytest tests/api -v --html=reports/api_report.html --self-contained-html

pytest tests/ -v --html=reports/report.html --self-contained-html

---

## Reports & Debugging Artifacts

* **HTML Report:** Open `reports/report.html` in any browser after a test run to view detailed pass/fail results.
* **Failure Screenshots:** Automatically saved to `screenshots/<test_name>.png` whenever a UI test fails.
* **Playwright Traces:** Automatically saved to `traces/<test_name>_trace.zip` on failure. View any trace interactively with:
  ```bash
  playwright show-trace traces/<test_name>_trace.zip
  ```

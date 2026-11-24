# E-Commerce Website End-to-End Test Automation

Automated UI and API test suite for [Automation Exercise](https://automationexercise.com) built using **Python**, **Playwright**, and **Pytest** following the **Page Object Model (POM)** design pattern.

---


## Project Structure

```text
E-Commerce-Website End-to-End Test Automation/
├── data/
│   └── test_data.json                  # Centralized test data for UI and API tests
├── pages/                              # Page Object Model classes
│   ├── base_page.py                    # Base navigation & footer newsletter subscription
│   ├── home_page.py                    # Top navigation & sidebar product categories
│   ├── auth_page.py                    # Registration, login, logout & account deletion
│   ├── products_page.py                # Product search, details, cart add & brand filters
│   └── cart_page.py                    # Cart item verification & removal
├── tests/
│   ├── ui/                             # 15 End-to-End UI test requirements
│   └── api/                            # 8 Positive + 4 Negative API test scenarios (18 items)
│       ├── test_api_01_get_all_products.py
│       ├── test_api_02_get_all_brands.py
│       ├── test_api_03_search_products.py
│       ├── test_api_04_verify_login.py
│       ├── test_api_05_create_user_account.py
│       ├── test_api_06_update_user_account.py
│       ├── test_api_07_delete_user_account.py
│       └── test_api_08_get_user_details.py
├── reports/                            # Generated HTML, UI and API reports
├── screenshots/                        # Failure screenshots (auto-generated)
├── traces/                             # Playwright trace archives on failure
├── conftest.py                         # Shared fixtures, API context & failure hooks
├── pytest.ini                          # Pytest markers, parallel workers & reporting config
└── requirements.txt                    # Project dependencies
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

### UI Automation Coverage details for above (15 Scenarios)
1. **Home Page Load:** Verify that the home page loads successfully.
2. **User Registration:** Register a new user with complete profile and address details.
3. **Account Creation Verification:** Verify successful account creation message and logged-in state.
4. **Valid Login:** Login with valid registered credentials.
5. **Invalid Login:** Verify error message when logging in with invalid credentials.
6. **Logout:** Logout cleanly from the application.
7. **Products Navigation:** Navigate to the All Products page.
8. **Product Search:** Search for a product and verify matching search results.
9. **Product Details:** View detailed product information (name, category, price, availability, condition, brand).
10. **Add to Cart:** Add products to the shopping cart.
11. **Cart Verification:** Verify product details, unit prices, and quantities in the cart.
12. **Remove from Cart:** Remove a product from the cart and verify empty cart state.
13. **Category Navigation:** Filter and navigate through product categories (`Women`, `Men`, `Kids`).
14. **Brand Navigation:** Filter and navigate through product brands (`Polo`, `H&M`, etc.).
15. **Newsletter Subscription:** Verify footer email subscription functionality.


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

### API Automation Coverage for above ap's(8 Positive + 4 Negative Scenarios)

| File | Positive Scenario | Negative Scenario(s) |
| :--- | :--- | :--- |
| `test_api_01_get_all_products.py` | `GET /api/productsList` (200) | `POST /api/productsList` unsupported method (405) |
| `test_api_02_get_all_brands.py` | `GET /api/brandsList` (200) | `PUT /api/brandsList` unsupported method (405) |
| `test_api_03_search_products.py` | `POST /api/searchProduct` with keywords (200) | Missing `search_product` parameter (400) |
| `test_api_04_verify_login.py` | `POST /api/verifyLogin` with valid credentials (200) | Invalid user (404), missing email/password (400), `DELETE` unsupported method (405) |
| `test_api_05_create_user_account.py` | `POST /api/createAccount` (201) | — |
| `test_api_06_update_user_account.py` | `PUT /api/updateAccount` (200) | — |
| `test_api_07_delete_user_account.py` | `DELETE /api/deleteAccount` (200) | — |
| `test_api_08_get_user_details.py` | `GET /api/getUserDetailByEmail` (200) | — |


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
              - `reports/report.html`
              -  `reports/api_report.html`
              -   `reports/ui_report.html`

* **Failure Screenshots:** Automatically saved to `screenshots/<test_name>.png` whenever a UI test fails.
* **Playwright Traces:** Automatically saved to `traces/<test_name>_trace.zip` on failure. View any trace interactively with:
  ```bash
  playwright show-trace traces/<test_name>_trace.zip
  ```

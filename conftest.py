import json
from pathlib import Path
import sys
import time
from playwright.sync_api import Playwright
import pytest

# Ensure project root is always in Python's import path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from pages.auth_page import AuthPage
from pages.home_page import HomePage


@pytest.fixture(autouse=True)
def block_ads(request):
    # Skip launching a browser for API tests
    if "api" in request.node.nodeid:
        return

    page = request.getfixturevalue("page")
    page.route(
        "**/*",
        lambda route: (
            route.abort()
            if any(
                ad in route.request.url
                for ad in ["googlesyndication", "doubleclick", "googleads"]
            )
            else route.continue_()
        ),
    )


@pytest.fixture(scope="session")
def raw_test_data():
    data_file = ROOT_DIR / "data" / "test_data.json"
    with open(data_file, "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def test_data(raw_test_data):
    """Alias so both API tests (test_data) and UI tests (raw_test_data) work seamlessly."""
    return raw_test_data


@pytest.fixture
def user_data(raw_test_data):
    user = raw_test_data["user"].copy()
    user["email"] = f"mohan_{int(time.time() * 1000)}@test.com"
    return user


@pytest.fixture
def registered_user(page, user_data):
    """Creates a fresh UI account before a test and deletes it afterward."""
    home = HomePage(page)
    auth = AuthPage(page)

    home.open()
    home.go_to_login()
    auth.signup_initial(user_data["name"], user_data["email"])
    auth.fill_account_details(user_data)
    auth.click_continue()
    auth.logout()

    yield user_data

    # Cleanup after test finishes
    home.open()
    if page.get_by_role("link", name="Logout").is_visible():
        auth.delete_account()
    else:
        home.go_to_login()
        auth.login(user_data["email"], user_data["password"])
        auth.delete_account()


@pytest.fixture
def api_request(playwright: Playwright):
    context = playwright.request.new_context(
        base_url="https://automationexercise.com",
        extra_http_headers={"Accept": "application/json"},
        ignore_https_errors=True,
    )
    yield context
    context.dispose()


@pytest.fixture
def created_user(api_request, raw_test_data):
    """Creates a user via API before the test and deletes it afterward."""
    user = raw_test_data["user"].copy()
    unique_email = f"mohan_api_{int(time.time() * 1000)}@test.com"
    payload = {
        "name": user["name"],
        "password": user["password"],
        "email": unique_email,
        "title": user.get("title", "Mr"),
        "birth_date": user["birth_date"],
        "birth_month": "Jan",
        "birth_year": user["birth_year"],
        "firstname": user["firstname"],
        "lastname": user["lastname"],
        "company": user["company"],
        "address1": user["address1"],
        "address2": user["address2"],
        "country": user["country"],
        "zipcode": user["zipcode"],
        "state": user["state"],
        "city": user["city"],
        "mobile_number": user["mobile_number"],
    }

    res = api_request.post("/api/createAccount", form=payload)
    assert res.status == 200
    assert res.json()["responseCode"] == 201, f"Setup failed: {res.text()}"

    yield {
        "email": unique_email,
        "password": user["password"],
        "name": user["name"],
        "payload": payload,
    }

    api_request.delete(
        "/api/deleteAccount",
        form={"email": unique_email, "password": user["password"]},
    )


@pytest.fixture(autouse=True)
def manage_artifacts(request):
    # Skip browser tracing/screenshots for API tests
    if "api" in request.node.nodeid:
        yield
        return

    page = request.getfixturevalue("page")
    context = page.context

    # Start recording trace
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield

    # Check if the test failed
    failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed
    test_name = request.node.name.replace("[", "_").replace("]", "")

    if failed:
        Path("screenshots").mkdir(exist_ok=True)
        Path("traces").mkdir(exist_ok=True)

        # Save screenshot in screenshots/ folder
        page.screenshot(
            path=f"screenshots/{test_name}.png", full_page=True
        )
        # Save trace.zip in traces/ folder
        context.tracing.stop(path=f"traces/{test_name}_trace.zip")
    else:
        context.tracing.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

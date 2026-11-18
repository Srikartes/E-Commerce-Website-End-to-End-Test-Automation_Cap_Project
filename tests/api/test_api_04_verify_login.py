#import pytest
#@pytest.mark.api
#def test_api_04_verify_login(api_client, api_registered_user):
 #   response = api_client.verify_login(
  #      api_registered_user["email"], api_registered_user["password"]
#    )
   # body = response.json()

    #assert response.status == 200
    #assert body["responseCode"] == 200
    #assert body["message"] == "User exists!"

import pytest


@pytest.mark.api
def test_verify_login_valid(api_request, created_user):
    response = api_request.post(
        "/api/verifyLogin",
        form={"email": created_user["email"], "password": created_user["password"]},
    )
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"


@pytest.mark.api
def test_verify_login_invalid_credentials(api_request, test_data):
    invalid = test_data["invalid_user"]
    response = api_request.post(
        "/api/verifyLogin",
        form={"email": invalid["email"], "password": invalid["password"]},
    )
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"


@pytest.mark.api
@pytest.mark.parametrize(
    "payload",
    [
        {"password": "SomePassword123"},
        {"email": "some_user@gmail.com"},
        {},
    ],
)
def test_verify_login_missing_parameters(api_request, payload):
    response = api_request.post("/api/verifyLogin", form=payload)
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, email or password parameter is missing in POST request."


@pytest.mark.api
def test_delete_verify_login_unsupported(api_request):
    response = api_request.delete("/api/verifyLogin")
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."


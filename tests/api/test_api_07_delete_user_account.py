import time
import pytest


@pytest.mark.api
def test_delete_user_account(api_request, test_data):
    user = test_data["user"]
    unique_email = f"mohan_del_{int(time.time() * 1000)}@gmail.com"
    payload = {
        "name": user["name"],
        "email": unique_email,
        "password": user["password"],
        "title": user["title"],
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

    create_res = api_request.post("/api/createAccount", form=payload)
    assert create_res.json()["responseCode"] == 201

    delete_res = api_request.delete(
        "/api/deleteAccount",
        form={"email": unique_email, "password": user["password"]},
    )
    assert delete_res.status == 200

    data = delete_res.json()
    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"

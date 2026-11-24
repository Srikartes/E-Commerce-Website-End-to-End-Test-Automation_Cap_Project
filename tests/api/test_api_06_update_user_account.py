import pytest


@pytest.mark.api
def test_update_user_account(api_request, created_user):
    updated_payload = created_user["payload"].copy()
    updated_payload["company"] = "UST Global"
    updated_payload["city"] = "Hyderabad"

    response = api_request.put("/api/updateAccount", form=updated_payload)
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"

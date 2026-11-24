import pytest


@pytest.mark.api
def test_get_user_detail_by_email(api_request, created_user):
    response = api_request.get(
        "/api/getUserDetailByEmail",
        params={"email": created_user["email"]},
    )
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert "user" in data
    assert data["user"]["email"] == created_user["email"]
    assert data["user"]["name"] == created_user["name"]

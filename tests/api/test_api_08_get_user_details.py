#import pytest
#@pytest.mark.api
#def test_api_08_get_user_details_by_email(api_client, api_registered_user):
 #   response = api_client.get_user_detail_by_email(
  #      api_registered_user["email"]
   # )
    #body = response.json()

    #assert response.status == 200
    #assert body["responseCode"] == 200
    #assert body["user"]["email"] == api_registered_user["email"]



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

#import pytest
#@pytest.mark.api
#def test_api_06_update_user_account(api_client, api_registered_user):
 #   updated_user = api_registered_user.copy()
  #  updated_user["city"] = "Bengaluru"

   # response = api_client.update_account(updated_user)
   # body = response.json()

   # assert response.status == 200
   # assert body["responseCode"] == 200
    #assert body["message"] == "User updated!"



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

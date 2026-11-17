import pytest
@pytest.mark.api
def test_api_08_get_user_details_by_email(api_client, api_registered_user):
    response = api_client.get_user_detail_by_email(
        api_registered_user["email"]
    )
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 200
    assert body["user"]["email"] == api_registered_user["email"]

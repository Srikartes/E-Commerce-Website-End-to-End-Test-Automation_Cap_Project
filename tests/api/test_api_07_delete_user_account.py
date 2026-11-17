import pytest
@pytest.mark.api
def test_api_07_delete_user_account(api_client, api_user_payload):
    # Create user first so we can verify deleting it
    api_client.create_account(api_user_payload)

    response = api_client.delete_account(
        api_user_payload["email"], api_user_payload["password"]
    )
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 200
    assert body["message"] == "Account deleted!"

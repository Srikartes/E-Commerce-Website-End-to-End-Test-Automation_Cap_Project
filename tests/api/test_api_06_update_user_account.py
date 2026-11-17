def test_api_06_update_user_account(api_client, api_registered_user):
    updated_user = api_registered_user.copy()
    updated_user["city"] = "Bengaluru"

    response = api_client.update_account(updated_user)
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 200
    assert body["message"] == "User updated!"

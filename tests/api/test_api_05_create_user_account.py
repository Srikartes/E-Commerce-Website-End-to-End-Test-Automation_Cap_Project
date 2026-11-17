def test_api_05_create_user_account(api_client, api_user_payload):
    response = api_client.create_account(api_user_payload)
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 201
    assert body["message"] == "User created!"

    # Cleanup created account
    api_client.delete_account(
        api_user_payload["email"], api_user_payload["password"]
    )

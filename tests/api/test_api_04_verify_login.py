def test_api_04_verify_login(api_client, api_registered_user):
    response = api_client.verify_login(
        api_registered_user["email"], api_registered_user["password"]
    )
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 200
    assert body["message"] == "User exists!"

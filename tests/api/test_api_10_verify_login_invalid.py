def test_api_10_verify_login_with_invalid_credentials(api_client):
    response = api_client.verify_login(
        email="nonexistent_999@test.com", password="WrongPassword123"
    )
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 404
    assert body["message"] == "User not found!"

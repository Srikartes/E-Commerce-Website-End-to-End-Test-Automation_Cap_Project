def test_api_02_get_all_brands(api_client):
    response = api_client.get_all_brands()
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 200
    assert len(body["brands"]) > 0

def test_api_01_get_all_products(api_client):
    response = api_client.get_all_products()
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 200
    assert len(body["products"]) > 0

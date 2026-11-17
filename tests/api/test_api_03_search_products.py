def test_api_03_search_products(api_client):
    response = api_client.search_products("top")
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 200
    assert len(body["products"]) > 0

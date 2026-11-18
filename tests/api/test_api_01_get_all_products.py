# import pytest
# @pytest.mark.api
# def test_api_01_get_all_products(api_client):
#     response = api_client.get_all_products()
#     body = response.json()

#     assert response.status == 200
#     assert body["responseCode"] == 200
#     assert len(body["products"]) > 0



import pytest


@pytest.mark.api
def test_get_all_products_list(api_request):
    response = api_request.get("/api/productsList")
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert "products" in data
    assert len(data["products"]) > 0


@pytest.mark.api
def test_post_all_products_list_unsupported(api_request):
    response = api_request.post("/api/productsList")
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."

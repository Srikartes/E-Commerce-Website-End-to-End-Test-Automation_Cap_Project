import pytest


@pytest.mark.api
@pytest.mark.parametrize("keyword", ["Blue Top", "Men Tshirt", "Sleeveless Dress"])
def test_search_product_valid(api_request, keyword):
    response = api_request.post("/api/searchProduct", form={"search_product": keyword})
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert "products" in data
    assert len(data["products"]) > 0


@pytest.mark.api
def test_search_product_missing_param(api_request):
    response = api_request.post("/api/searchProduct")
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, search_product parameter is missing in POST request."

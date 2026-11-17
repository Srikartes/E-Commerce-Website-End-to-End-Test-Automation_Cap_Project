import pytest

@pytest.mark.api

@pytest.mark.parametrize(
    "method_name",
    [
        "post_to_products_list",  # POST /api/productsList
        "put_to_brands_list",  # PUT /api/brandsList
        "delete_to_verify_login",  # DELETE /api/verifyLogin
    ],
)
def test_api_12_unsupported_http_methods(api_client, method_name):
    api_call = getattr(api_client, method_name)
    response = api_call()
    body = response.json()

    assert response.status == 200
    assert body["responseCode"] == 405
    assert body["message"] == "This request method is not supported."

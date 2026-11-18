#import pytest
#@pytest.mark.api
#def test_api_02_get_all_brands(api_client):
 #   response = api_client.get_all_brands()
  #  body = response.json()
    
   # assert response.status == 200
    #assert body["responseCode"] == 200
    #assert len(body["brands"]) > 0

import pytest


@pytest.mark.api
def test_get_all_brands_list(api_request):
    response = api_request.get("/api/brandsList")
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert "brands" in data
    assert len(data["brands"]) > 0


@pytest.mark.api
def test_put_all_brands_list_unsupported(api_request):
    response = api_request.put("/api/brandsList")
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."

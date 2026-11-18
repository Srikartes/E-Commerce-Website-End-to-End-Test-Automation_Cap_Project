#import pytest

#@pytest.mark.api

#@pytest.mark.parametrize(
 #   "email,password",
    #[
  #      (None, "Password123"),  # Missing email
   #     ("mohan@test.com", None),  # Missing password
    #    (None, None),  # Missing both
    #],
#)
#def test_api_11_verify_login_without_required_params(
 #   api_client, email, password
#):
 #   response = api_client.verify_login(email=email, password=password)
  #  body = response.json()

    #assert response.status == 200
    #assert body["responseCode"] == 400
    #assert (
     #   body["message"]
      #  == "Bad request, email or password parameter is missing in POST request."
    #)

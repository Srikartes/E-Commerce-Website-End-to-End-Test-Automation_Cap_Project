# from playwright.sync_api import APIRequestContext


# class EcommerceAPI:

#     def __init__(self, request: APIRequestContext):
#         self.request = request

#     def get_all_products(self):
#         return self.request.get("/api/productsList")

#     def get_all_brands(self):
#         return self.request.get("/api/brandsList")

#     def search_products(self, query: str):
#         return self.request.post(
#             "/api/searchProduct", form={"search_product": query}
#         )

#     def verify_login(self, email: str, password: str):
#         return self.request.post(
#             "/api/verifyLogin", form={"email": email, "password": password}
#         )

#     def create_account(self, user: dict):
#         return self.request.post("/api/createAccount", form=user)

#     def update_account(self, user: dict):
#         return self.request.put("/api/updateAccount", form=user)

#     def delete_account(self, email: str, password: str):
#         return self.request.delete(
#             "/api/deleteAccount", form={"email": email, "password": password}
#         )

#     def get_user_detail_by_email(self, email: str):
#         return self.request.get(
#             "/api/getUserDetailByEmail", params={"email": email}
#         )
from playwright.sync_api import APIRequestContext


class EcommerceAPI:

    def __init__(self, request: APIRequestContext):
        self.request = request

    # --- Positive Methods ---
    def get_all_products(self):
        return self.request.get("/api/productsList")

    def get_all_brands(self):
        return self.request.get("/api/brandsList")

    def search_products(self, query: str = None):
        form_data = {"search_product": query} if query is not None else {}
        return self.request.post("/api/searchProduct", form=form_data)

    def verify_login(self, email: str = None, password: str = None):
        form_data = {}
        if email is not None:
            form_data["email"] = email
        if password is not None:
            form_data["password"] = password
        return self.request.post("/api/verifyLogin", form=form_data)

    def create_account(self, user: dict):
        return self.request.post("/api/createAccount", form=user)

    def update_account(self, user: dict):
        return self.request.put("/api/updateAccount", form=user)

    def delete_account(self, email: str, password: str):
        return self.request.delete(
            "/api/deleteAccount", form={"email": email, "password": password}
        )

    def get_user_detail_by_email(self, email: str):
        return self.request.get(
            "/api/getUserDetailByEmail", params={"email": email}
        )

    # --- Unsupported HTTP Methods ---
    def post_to_products_list(self):
        return self.request.post("/api/productsList")

    def put_to_brands_list(self):
        return self.request.put("/api/brandsList")

    def delete_to_verify_login(self):
        return self.request.delete("/api/verifyLogin")

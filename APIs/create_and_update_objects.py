import requests
from APIs.Base_API import BaseAPI


class CreateUpdateAPI(BaseAPI):

    def create_object(self, payload):
        url = f"{self.base_url}{self.endpoint}"
        return requests.post(url, json=payload)

    def update_object(self, product_id, payload):
        url = f"{self.base_url}{self.endpoint}/{product_id}"
        return requests.put(url, json=payload)

    def partially_update_object(self, product_id, payload):
        url = f"{self.base_url}{self.endpoint}/{product_id}"
        return requests.patch(url, json=payload)

    @staticmethod
    def get_product_id(json_data):
        product_id = json_data.get("id")
        return product_id
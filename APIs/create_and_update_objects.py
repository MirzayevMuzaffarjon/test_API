import requests
from APIs.Base_API import BaseAPI


class CreateUpdateAPI(BaseAPI):

    def create_object(self, payload):
        url = f"{self.base_url}{self.endpoint}"
        return requests.post(url, json=payload)

    @staticmethod
    def get_product_id(json_data):
        product_id = json_data.get("id")
        return product_id
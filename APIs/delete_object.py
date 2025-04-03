import requests
from APIs.Base_API import BaseAPI


class DeleteObjectAPI(BaseAPI):

    def delete_object(self, product_id):
        url = f"{self.base_url}{self.endpoint}/{product_id}"
        return requests.delete(url)
import requests
from APIs.Base_API import BaseAPI

class GetObjects(BaseAPI):
    get_obj_endpoint = "objects"

    def get_list_of_all_objects(self):
        url = f"{self.base_url}{self.get_obj_endpoint}"
        return requests.get(url)

    def get_of_objects_by_ids(self, id_list):
        url = f"{self.base_url}{self.get_obj_endpoint}"
        params = {"id": id_list}
        return requests.get(url, params=params)

    def get_single_object(self, product_id):
        url = f"{self.base_url}{self.get_obj_endpoint}"
        params = {"id": product_id}
        return requests.get(url, params=params)
from APIs.get_objects import GetObjects
from APIs.create_and_update_objects import CreateUpdateAPI
from APIs.delete_object import DeleteObjectAPI
import pytest

payload_for_create_object = {
   "name": "Samsung galaxy iPhone 16 pro max not ultra pro plus max",
   "data": {
      "year": 2000,
      "price": 1000,
      "CPU model": "Intel Core i10",
      "Hard disk size": "10 TB"
   }
}

@pytest.fixture(scope="function")
def get_objects_api():
    return GetObjects()

@pytest.fixture(scope="function")
def create_update_api():
    return CreateUpdateAPI()

@pytest.fixture(scope="function")
def delete_api():
    return DeleteObjectAPI()

@pytest.fixture
def product_id(create_update_api):
    response = create_update_api.create_object(payload_for_create_object)
    product_id = create_update_api.get_product_id(response.json())
    return product_id

@pytest.fixture
def product_id_list(product_id):
    id_list = []
    for i in range(4):
        id_list.append(product_id)
    return id_list






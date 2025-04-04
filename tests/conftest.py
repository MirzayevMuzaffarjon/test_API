from data import data
from APIs.get_objects import GetObjects
from APIs.create_and_update_objects import CreateUpdateAPI
from APIs.delete_object import DeleteObjectAPI
import pytest

########################################################################################################################

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
    response = create_update_api.create_object(data.payload_for_create_object)
    product_id = create_update_api.get_product_id(response.json())
    return product_id

@pytest.fixture
def product_id_list(product_id):
    id_list = []
    for i in range(4):
        id_list.append(product_id)
    return id_list






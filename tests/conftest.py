from APIs.get_objects import GetObjects
import pytest

@pytest.fixture(scope="function")
def get_objects_api():
    return GetObjects()




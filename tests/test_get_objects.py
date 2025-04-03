from http.client import responses


def test_get_list_of_all_objects(get_objects_api):
    response = get_objects_api.get_list_of_all_objects()
    get_objects_api.verify_status_code_is(200, response)
    print("\n",response.json())

def test_get_of_objects_by_ids(get_objects_api):
    response = get_objects_api.get_of_objects_by_ids([3, 5, 10])
    get_objects_api.verify_status_code_is(200, response)
    print("\n",response.json())

def test_get_single_object(get_objects_api):
    response = get_objects_api.get_single_object(6)
    get_objects_api.verify_status_code_is(200, response)
    print("\n", response.json())


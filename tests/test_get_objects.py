def test_get_list_of_all_objects(get_objects_api):
    response = get_objects_api.get_list_of_all_objects()
    get_objects_api.verify_status_code_is(200, response.status_code)
    print("\n---got product list(get)---")

def test_get_of_objects_by_ids(get_objects_api, product_id_list):
    response = get_objects_api.get_of_objects_by_ids(product_id_list)
    get_objects_api.verify_status_code_is(200, response.status_code)
    print("\n---got products by IDs(get)---")

def test_get_single_object(get_objects_api, product_id):
    response = get_objects_api.get_single_object(product_id)
    get_objects_api.verify_status_code_is(200, response.status_code)
    print("\n---got product by id(get)---")
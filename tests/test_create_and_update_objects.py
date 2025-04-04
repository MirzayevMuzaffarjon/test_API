from data import data

########################################################################################################################

def test_create_object(create_update_api):
    response = create_update_api.create_object(data.payload_for_create_object)
    create_update_api.verify_status_code_is(200, response.status_code)
    create_update_api.created_product_id = create_update_api.get_product_id(response.json())
    print("\n---product created end created_product_id variable updated(post)---")

def test_update_object(create_update_api, product_id):
    response = create_update_api.update_object(product_id, data.payload_for_update_object)
    create_update_api.verify_status_code_is(200, response.status_code)
    print("\n---product updated(put)---")

def test_partially_update_object(create_update_api, product_id):
    response = create_update_api.update_object(product_id, data.payload_for_partially_update_object)
    create_update_api.verify_status_code_is(200, response.status_code)
    print("\n---product updated(patch)---")


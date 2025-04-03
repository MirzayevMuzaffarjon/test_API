def test_delete_object(delete_api, product_id):
    response = delete_api.delete_object(product_id)
    delete_api.verify_status_code_is(200, response.status_code)
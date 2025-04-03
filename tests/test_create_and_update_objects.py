payload_for_create_object = {
   "name": "Samsung galaxy iPhone 16 pro max not ultra pro plus max",
   "data": {
      "year": 2000,
      "price": 1000,
      "CPU model": "Intel Core i10",
      "Hard disk size": "10 TB"
   }
}


def test_create_object(create_update_api):
    response = create_update_api.create_object(payload_for_create_object)
    create_update_api.verify_status_code_is(200, response.status_code)
    create_update_api.created_product_id = create_update_api.get_product_id(response.json())

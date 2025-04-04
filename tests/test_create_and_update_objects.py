payload_for_create_object = {
   "name": "Samsung galaxy iPhone 16 pro max not ultra pro plus max",
   "data": {
      "year": 2000,
      "price": 1000,
      "CPU model": "Intel Core i10",
      "Hard disk size": "10 TB"
   }
}

payload_for_update_object = {
   "name": "motorolla primary",
   "data": {
      "year": 2015,
      "price": 150000,
      "CPU model": "Intel Core i19",
      "Hard disk size": "2 TB"
   }
}

payload_for_partially_update_object = {
   "name": "Nokia (Updated Name)"
}


def test_create_object(create_update_api):
    response = create_update_api.create_object(payload_for_create_object)
    create_update_api.verify_status_code_is(200, response.status_code)
    create_update_api.created_product_id = create_update_api.get_product_id(response.json())
    print("\n---product created end created_product_id variable updated---")

def test_update_object(create_update_api, product_id):
    response = create_update_api.update_object(product_id, payload_for_update_object)
    create_update_api.verify_status_code_is(200, response.status_code)
    print("\n---product updated(put)---")

def test_partially_update_object(create_update_api, product_id):
    response = create_update_api.update_object(product_id, payload_for_partially_update_object)
    create_update_api.verify_status_code_is(200, response.status_code)
    print("\n---product updated(patch)---")


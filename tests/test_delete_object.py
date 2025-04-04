def test_delete_object(delete_api, product_id):
    id_deleted_product = product_id
    response = delete_api.delete_object(id_deleted_product)
    delete_api.verify_status_code_is(200, response.status_code)
    print(f"\n---item deleted with id({id_deleted_product}) (delete)---")
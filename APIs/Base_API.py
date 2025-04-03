import os
from dotenv import load_dotenv


class BaseAPI:
    load_dotenv()
    created_product_id = None
    base_url = os.getenv("BASEURL")
    endpoint = "objects"

    @staticmethod
    def verify_status_code_is(expected_status_code: int, actual_status_code):
        assert actual_status_code == expected_status_code
        print(f"\n---status code is {expected_status_code}---")
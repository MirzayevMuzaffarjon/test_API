import os
from dotenv import load_dotenv

class BaseAPI:
    load_dotenv()
    base_url = os.getenv("BASEURL")

    @staticmethod
    def verify_status_code_is(expected_status_code: int, response):
        assert response.status_code == expected_status_code
        print(f"\nstatus code is {expected_status_code}")
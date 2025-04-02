import os
from dotenv import load_dotenv

class BaseAPI:
    load_dotenv()
    base_url = os.getenv("BASEURL")





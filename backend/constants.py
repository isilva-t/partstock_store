import os
from dotenv import load_dotenv

load_dotenv()


class Env:
    MONGO_URL = os.getenv("MONGO_URL")
    ORIGIN = os.getenv("ORIGIN")
    DATA_PATH = os.getenv("DATA_PATH")

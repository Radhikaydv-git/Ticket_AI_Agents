import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Get backend folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

print("Loading .env from:", ENV_PATH)

loaded = load_dotenv(dotenv_path=ENV_PATH)

print("Loaded:", loaded)
print("MONGO_URI:", os.getenv("MONGO_URI"))
print("DATABASE_NAME:", os.getenv("DATABASE_NAME"))

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if MONGO_URI is None:
    raise Exception("MONGO_URI not found")

if DATABASE_NAME is None:
    raise Exception("DATABASE_NAME not found")

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
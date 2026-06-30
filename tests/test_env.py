import os
from dotenv import load_dotenv

load_dotenv()

print("Server:", os.getenv("DB_SERVER"))
print("Database:", os.getenv("DB_DATABASE"))
print("Driver:", os.getenv("DB_DRIVER"))
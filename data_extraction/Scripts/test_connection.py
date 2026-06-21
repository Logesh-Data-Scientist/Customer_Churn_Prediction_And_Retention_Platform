from db_connection import get_engine

try:
    engine = get_engine()

    with engine.connect() as conn:
        print("Database Connected Successfully")

except Exception as e:
    print("Connection Failed")
    print(e)
from src.common.database.postgres import SQLVars, SQLFactoryEngine   
import os


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    sql_vars = SQLVars(
        USERNAME=os.getenv("USERNAME"),
        PASSWORD=os.getenv("PASSWORD"),
        HOST=os.getenv("HOST"),
        DATABASE=os.getenv("DATABASE")
    )

    sql_engine = SQLFactoryEngine(sql_vars)
    engine = sql_engine.get_engine()
    with engine.connect() as connection:
        result = connection.execute("SELECT 'Hello'")
        for row in result:
            print(row)
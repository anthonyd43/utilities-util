from sqlalchemy import create_engine
from pydantic import BaseModel, Field


class SQLVars(BaseModel):
    USERNAME: str
    PASSWORD: str
    HOST: str
    DATABASE: str


class SQLFactoryEngine():
    def __init__(self, sql_vars: SQLVars):
        self.engine = self.create_engine(sql_vars)

    def create_engine(self, sql_vars: SQLVars):
        engine = create_engine(f"postgresql://{sql_vars.USERNAME}:{sql_vars.PASSWORD}@{sql_vars.HOST}/{sql_vars.DATABASE}?sslmode=require&channel_binding=require")
        return engine
    
    def get_engine(self):
        return self.engine

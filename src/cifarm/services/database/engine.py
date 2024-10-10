from sqlalchemy import create_engine
from services.database.models.base import Base
import env

class PostgresEngine:
    def __init__(self):
        self.host = env.POSTGRES_HOST
        self.port = int(env.POSTGRES_PORT)
        self.database = env.POSTGRES_DB
        self.constants = env.POSTGRES_USER
        self.password = env.POSTGRES_PASSWORD
        self.engine = create_engine(f'postgresql://{self.constants}:{self.password}@{self.host}:{self.port}/{self.database}', echo=True)
        Base.metadata.create_all(self.engine) 
    

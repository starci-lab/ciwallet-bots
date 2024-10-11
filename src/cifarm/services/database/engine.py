from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from services.database.models.base import Base
from config import env
 
class PostgresEngine:
    def __init__(self):
        self.host = env.POSTGRES_HOST
        self.port = int(env.POSTGRES_PORT)
        self.database = env.POSTGRES_DB
        self.constants = env.POSTGRES_USER
        self.password = env.POSTGRES_PASSWORD
        self.engine = create_engine(f'postgresql://{self.constants}:{self.password}@{self.host}:{self.port}/{self.database}', echo=True)
        if not database_exists(self.engine.url): create_database(self.engine.url)
        Base.metadata.create_all(self.engine) 
    

import logging
import sys

from services.database.engine import PostgresEngine
from services.database.models.users import User
from sqlalchemy.orm import Session

class CreateParams:
    def __init__(self, telegram_id: str, username: str):
        self.telegram_id = telegram_id
        self.username = username

class UsersRepository:
    def __init__(self):
        self.engine = PostgresEngine().engine
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
        )

    def create(self, params: CreateParams):
        with Session(self.engine) as session:
            session.add(User(telegram_id=params.telegram_id, username=params.username))
            session.commit()

    def get_by_telegram_id(self, telegram_id: str):
        with Session(self.engine) as session:
            return session.query(User).filter(User.telegram_id == telegram_id).first()
        
    def count(self):
        with Session(self.engine) as session:
            return session.query(User).count()
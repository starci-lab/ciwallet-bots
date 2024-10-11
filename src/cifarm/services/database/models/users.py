import uuid
from services.database.models.base import Base
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id: Mapped[VARCHAR] = mapped_column(VARCHAR(10), nullable=False, unique=True)
    username: Mapped[VARCHAR] = mapped_column(VARCHAR(50), nullable=False)
from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: UUID = Field(default=uuid4, primary_key=True)
    first_name: str
    last_name: str
    username: str
    gender: str
    cpf: str
    birth_date: datetime

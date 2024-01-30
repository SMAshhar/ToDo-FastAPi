from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todo(Base):
    """
    A class representing a todo item.
    
    """
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)

class User(Base):
    """
    A class representing a user.
    
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
from sqlalchemy import Column, Integer, String
from database import Base

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(256))
    status = Column(String(256))
    priority = Column(String(256))
    due_date = Column(String(256))
    created_at = Column(String(256))
    updated_at = Column(String(256))
    deleted_at = Column(String(256))
    user_id = Column(Integer)
    def __repr__(self):
        return '<Todo %r>' % (self.description)
    

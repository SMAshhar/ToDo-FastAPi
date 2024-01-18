from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
    
app = FastAPI()

SQLALCHEMY_DATABASE_URL = "postgresql://syed.muhammad.ashhar:vqA4NDsub0TQ@ep-broad-mode-097739.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)

@app.post("/create")
async def create_todo(text: str, is_complete: bool = False):
    # Create a new session instance for this request
    with session() as s:
        new_todo = Todo(text=text, is_done=is_complete)
        s.add(new_todo)
        s.commit()
        s.refresh(new_todo)
    return {"todo added": new_todo.text}

@app.get("/")   
async def get_all_todos():
    todos_query = session().query(Todo)
    return todos_query.all()

@app.get("/done")
async def list_done_todos():
    todos_query = session().query(Todo)
    done_todos_query = todos_query.filter(Todo.is_done==True)
    return done_todos_query.all()

@app.patch("/update/{id}")
async def update_todo(id: int, text: str): 
    todo_query = session().query(Todo).filter(Todo.id==id)
    todo_query.update({"text": text})
    session().commit()
    return {"todo updated": id}

@app.delete("/delete/{id}")
async def delete_todo(id: int):
    todo_query = session().query(Todo).filter(Todo.id==id)
    todo_query.delete()
    session().commit()
    return {"todo deleted": id}
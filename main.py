import os
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from dotenv import load_dotenv
    
app = FastAPI()


load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(Base):
    """
    A class representing a todo item.
    
    """
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)

@app.post("/create")
async def create_todo(text: str, is_complete: bool = False):
    """
    Creates a new todo item.
    
    :param text: The text of the todo item.
    :type text: str
    :param is_complete: Whether the todo item is complete. Defaults to False.
    :type is_complete: bool
    :return: A dictionary containing the text of the new todo item.
    :rtype: dict
    
    :raises ValueError: If the text is empty.
    
    :Example:
    
    >>> create_todo("Buy milk")
    {'todo added': 'Buy milk'}
    
    :Example:
    
    >>> create_todo("", is_complete=True)
    Traceback (most recent call last):
    ...
    ValueError: Text cannot be empty.
    
    :Example:
    
    >>> create_todo("Buy milk", is_complete=True)
    {'todo added': 'Buy milk'}
    
    """
    try:
        with session() as s:
            new_todo = Todo(text=text, is_done=is_complete)
            s.add(new_todo)
            s.commit()
            s.refresh(new_todo)
        return {"todo added": new_todo.text}
    except ValueError as e:
        return {"error": str(e)}

@app.get("/todo")   
async def get_all_todos():
    """
    Returns a list of all todo items.
    
    :return: A list of todo items.
    :rtype: list
    
    :Example:
    
    >>> get_all_todos()
    [{'id': 1, 'text': 'Buy milk', 'is_done': False}, {'id': 2, 'text': 'Wash dishes', 'is_done': False}]
    
    """
    todos_query = session().query(Todo)
    return todos_query.all()

@app.get("/done")
async def list_done_todos():
    """
    Returns a list of all done todo items.
    
    :return: A list of done todo items.
    :rtype: list
    
    :Example:
    
    >>> list_done_todos()
    [{'id': 1, 'text': 'Buy milk', 'is_done': True}, {'id': 3, 'text': 'Buy butter', 'is_done': True}]
    
    """
    todos_query = session().query(Todo)
    done_todos_query = todos_query.filter(Todo.is_done==True)
    return done_todos_query.all()

@app.patch("/update/{id}")
async def update_todo(id: int, text: str, is_complete: bool = None):
    """
    Updates a todo item.
    
    :param id: The id of the todo item to update.
    :type id: int
    :param text: The new text of the todo item (optional).
    :type text: str
    :param is_complete: The new completion status of the todo item (optional).
    :type is_complete: bool
    :return: A dictionary containing the id of the updated todo item.
    :rtype: dict
    
    :Example:
    
    >>> update_todo(1, "Buy milk")
    {'todo updated': 1}
    
    :Example:
    
    >>> update_todo(2, is_complete=True)
    {'todo updated': 2}
    
    :Example:
    
    >>> update_todo(3, "Buy eggs", is_complete=True)
    {'todo updated': 3}
    """
    session_instance = session()
    try:
        todo_query = session_instance.query(Todo).filter(Todo.id == id)
        todo_to_update = todo_query.first()

        if not todo_to_update:
            return {"message": "Todo not found"}

        if text is not None:
            todo_to_update.text = text

        if is_complete is not None:
            todo_to_update.is_done = is_complete

        session_instance.commit()
        return {"todo updated": id}
    except Exception as e:
        session_instance.rollback()
        return {"error": str(e)}
    finally:
        session_instance.close()


@app.delete("/delete/{id}")
async def delete_todo(id: int):
    """
    Deletes a todo item.
    
    :param id: The id of the todo item to delete.
    :type id: int
    :return: A dictionary containing the id of the deleted todo item.
    :rtype: dict
    
    :Example:
    
    >>> delete_todo(1)
    {'todo deleted': 1}
    """
    session_instance = session()
    try:
        todo_query = session_instance.query(Todo).filter(Todo.id == id)
        todo_to_delete = todo_query.first()

        if not todo_to_delete:
            return {"message": "Todo not found"}

        session_instance.delete(todo_to_delete)
        session_instance.commit()
        return {"todo deleted": id}
    except Exception as e:
        session_instance.rollback()
        return {"error": str(e)}
    finally:
        session_instance.close()

# streamlit_client.py

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App - SMA")

def get_todos():
    """
    This function gets all the todos from the server and displays them in the app.
    It uses the requests library to make a GET request to the server.
    The response from the server is a JSON object containing the todos.
    The todos are displayed in the app using the st.json() function.
    The function returns nothing.
    if st.button("Get Todos"):
        response = requests.get(f"{BASE_URL}/todo")
        if response.status_code == 200:
            st.success("Todos retrieved successfully")
            st.json(response.json())
        else:
            st.error("Error retrieving todos")
    """
    if st.button("Get Todos"):
        response = requests.get(f"{BASE_URL}/todo")
        if response.status_code == 200:
            st.success("Todos retrieved successfully")
            sorted_data = sorted(response.json(), key=lambda x: x['id'])
            for element in sorted_data:
                st.write(element['id'] ,element['text'], element['is_done'])
            # st.json(response.json())
        else:
            st.error("Error retrieving todos")
            
def get_done():
    """
    This function gets all the done todos from the server and displays them in the app.
    It uses the requests library to make a GET request to the server.
    The response from the server is a JSON object containing the done todos.
    The done todos are displayed in the app using the st.json() function.
    The function returns nothing.
    
        if st.button("Get All Done Todos"):
        response = requests.get(f"{BASE_URL}/done")
        if response.status_code == 200:
            st.success("Todos retrieved successfully")
            st.json(response.json())
        else:
            st.error("Error retrieving todos")
    """
    if st.button("Get All Done Todos"):
        response = requests.get(f"{BASE_URL}/done")
        if response.status_code == 200:
            st.success("Todos retrieved successfully")
            sorted_data = sorted(response.json(), key=lambda x: x['id'])
            for element in sorted_data:
                st.write(element['id'] ,element['text'], element['is_done'])
            # st.json(response.json())
        else:
            st.error("Error retrieving todos")

def create_todo():
    
    """
    This function creates a new todo on the server and displays it in the app.
    It uses the requests library to make a POST request to the server.
    The response from the server is a JSON object containing the created todo.
    The created todo is displayed in the app using the st.json() function.
    The function returns nothing.
    
        description = st.text_area("Enter Todo Description")
        is_complete = st.checkbox("Is Todo Complete", key=2)
        if st.button("Add Todo"):
            response = requests.post(f"{BASE_URL}/create?text={description}&is_complete={is_complete}", json={"text": description, "is_complete":is_complete})
            if response.status_code == 200:
                st.success("Todo added successfully")
    """
    description = st.text_area("Enter Todo Description")
    is_complete = st.checkbox("Is Todo Complete", key=2)
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/create?text={description}&is_complete={is_complete}", json={"text": description, "is_complete":is_complete})
        if response.status_code == 200:
            st.success("Todo added successfully")
            
            
def update_todo():
    """
    This function updates an existing todo on the server and displays it in the app.
    It uses the requests library to make a PATCH request to the server.
    The response from the server is a JSON object containing the updated todo.
    The updated todo is displayed in the app using the st.json() function.
    The function returns nothing.
        
        todo_id = st.number_input("Update Todo", step=1, min_value=1, max_value=100, key=1, value=1, format="%d")
        description = st.text_area(f"Enter Todo Description ({todo_id})", key=f"description_{todo_id}")
        is_complete = st.checkbox("Is Todo Complete")
        if st.button("Update Todo"):
            response = requests.patch(f"{BASE_URL}/update/{todo_id}?text={description}&is_complete={is_complete}", json={ "id":todo_id,"text": description, "is_complete": is_complete})
            # /update/1?text=other%20again&is_complete=true
            if response.status_code == 200:
                st.success("Todo updated successfully")
    """
    todo_id = st.number_input("Update Todo", step=1, min_value=1, max_value=100, key=1, value=1, format="%d")
    description = st.text_area(f"Enter Todo Description ({todo_id})", key=f"description_{todo_id}")
    is_complete = st.checkbox("Is Todo Complete")
    if st.button("Update Todo"):
        response = requests.patch(f"{BASE_URL}/update/{todo_id}?text={description}&is_complete={is_complete}", json={ "id":todo_id,"text": description, "is_complete": is_complete})
        # /update/1?text=other%20again&is_complete=true
        if response.status_code == 200:
            st.success("Todo updated successfully")

def delete_todo():
    
    """
    This function deletes an existing todo on the server and displays a success message in the app.
    It uses the requests library to make a DELETE request to the server.
    The response from the server is a JSON object containing the deleted todo.
    The deleted todo is displayed in the app using the st.json() function.
    The function returns nothing.
    
        todo_id = st.number_input("Enter Todo ID to delete", step=1, min_value=1, max_value=100, key=3, value=1, format="%d")
        if st.button("Delete Todo"):
            response = requests.delete(f"{BASE_URL}/delete/{todo_id}")
            if response.status_code == 200:
                st.success("Todo deleted successfully")
                st.json(response.json())
            else:
                st.error("Error deleting todo")
                
        todo_id = st.number_input("Enter Todo ID to delete", step=1, min_value=1, max_value=100, key=3, value=1, format="%d")
        if st.button("Delete Todo"):
    """
    todo_id = st.number_input("Enter Todo ID to delete", step=1, min_value=1, max_value=100, key=3, value=1, format="%d")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/delete/{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully")

if __name__ == "__main__":
    st.markdown("### Get all todos.")
    get_todos()
    st.markdown("### Get all completed todos.")
    get_done()
    st.markdown("### Create new todo.")
    create_todo()
    st.markdown("### Update an existing todos.")
    update_todo()
    st.markdown("### Delete an existing todo.")
    delete_todo()
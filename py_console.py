import requests

BASE_URL = "http://127.0.0.1:8000"

def create_todo():
    """
    This function creates a new todo item.
    It takes user input for the todo description and completion status.
    It sends a POST request to the API endpoint /create with the todo description and completion status as JSON data.
    If the request is successful, it prints a success message.
    If the request fails, it prints an error message.
    The function returns nothing.
    """
    description = input("Enter Todo Description: ")
    try:
        is_complete = input("Is todo complete? True or False: ").capitalize()
    except ValueError:
        print("Invalid input. Please enter True or False.")
    response = requests.post(f"{BASE_URL}/create?text={description}&is_complete={is_complete}", json={"text": description, "is_complete":is_complete})
    if response.status_code == 200:
        print("Todo added successfully")
        
def update_todo():
    """
    This function updates an existing todo item.
    It takes user input for the todo ID, description, and completion status.
    It sends a PATCH request to the API endpoint /update with the todo ID, description, and completion status as JSON data.
    If the request is successful, it prints a success message.
    If the request fails, it prints an error message.
    The function returns nothing.
    """
    todo_id = input("Enter Todo ID to update: ")
    description = input("Enter Todo Description: ")
    try:
        is_complete = input("Is todo complete? True or False: ").capitalize()
    except ValueError:
        print("Invalid input. Please enter True or False.")
    response = requests.patch(f"{BASE_URL}/update/{todo_id}?text={description}&is_complete={is_complete}", json={ "id":todo_id,"text": description, "is_complete": is_complete})
    if response.status_code == 200:
        print("Todo added successfully")    

def delete_todo():
    """
    This function deletes an existing todo item.
    It takes user input for the todo ID.
    It sends a DELETE request to the API endpoint /delete with the todo ID as a parameter.
    If the request is successful, it prints a success message.
    If the request fails, it prints an error message.
    The function returns nothing.    
    """
    todo_id = input("Enter Todo ID to delete: ")
    response = requests.delete(f"{BASE_URL}/delete/{todo_id}")
    if response.status_code == 200:
        print("Todo deleted successfully")
        
def view_todos():
    """
    This function retrieves all todo items.
    It sends a GET request to the API endpoint /todo.
    If the request is successful, it prints a success message and the retrieved todo items.
    If the request fails, it prints an error message.
    The function returns nothing.    
    """
    response = requests.get(f"{BASE_URL}/todo")
    if response.status_code == 200:
        print("Todos retrieved successfully")
        sorted_data = sorted(response.json(), key=lambda x: x['id'])
        for element in sorted_data:
            print(element['id'] ,element['text'], element['is_done'])
            # st.json(response.json())
    else:
        print("Error retrieving todos")
        
def view_completed_todos():
    """
    This function retrieves all completed todo items.
    It sends a GET request to the API endpoint /done.
    If the request is successful, it prints a success message and the retrieved todo items.
    If the request fails, it prints an error message.
    The function returns nothing.
    """
    response = requests.get(f"{BASE_URL}/done")
    if response.status_code == 200:
        print("Todos retrieved successfully")
        sorted_data = sorted(response.json(), key=lambda x: x['id'])
        for element in sorted_data:
            print(element['id'] ,element['text'], element['is_done'])
            # st.json(response.json())
    else:
        print("Error retrieving todos")
        
functions_dictionary = {
    '1': create_todo,
    '2': update_todo,
    '3': delete_todo,
    '4': view_todos,
    '5': view_completed_todos,
}

def select_function():
    """
    This function prompts the user to select a function from a list of functions.
    It takes the user input as the function number.
    It calls the selected function.
    If the user enters an invalid function number, it prints an error message.
    The function returns nothing.    
    """
    func = input(
        """
Please enter a number from the following list:
    1. Create Todo
    2. Update Todo
    3. Delete Todo
    4. View Todos
    5. View Completed Todos
    6. Exit
Enter your choice : """
                 )
    
    functions_dictionary[func]()

if __name__ == "__main__":
    select_function()
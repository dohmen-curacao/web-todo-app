FILEPATH = 'todos.txt'
# FILEPATH = 'files/todos.txt'

def get_todos(filepath=FILEPATH):
    """ reads the contents of the file in filepath and returns the list
    of the todo-items in the file
    """
# function now uses a default argument
# this means that the call to the function can leave this argument out
# unless a different file is meant to be opened
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_to_write, filepath=FILEPATH):
    """
    Function writes the list of todo-items to a file
    :param todos_to_write:
    :param filepath:
    :return: None
    """
# function now uses a default argument
# the second, a non-default parameter has to be specified first in this case
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_to_write)
        return  # optional

if __name__ == '__main__':
    print("code inside module should only be executed when module is called")
    print("File paths is ", FILEPATH)
    todos = get_todos(FILEPATH)
    print(todos)
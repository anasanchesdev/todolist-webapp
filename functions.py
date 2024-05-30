from time import strftime
import os
import sys

# cria todos.txt caso não exista
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

FILEPATH = 'todos.txt'


def get_todos():
    """
    Creates list based on previous todos
    :return:
    """
    with open(FILEPATH, 'r') as todos_file:
        todo_list = todos_file.readlines()
    return todo_list


def update_file(todos):
    """
    Updates todos.txt file with new values of todo_list.
    :param todos: list of to-dos
    """
    with open(FILEPATH, 'w') as todos_file_f:
        todos_file_f.writelines(todos)


def index_from_todo(index_input):
    """
    Picks the index of the to-do to be edited/completed by the user.
    :param index_input: index given from the user
    :returns: the given index minus 1
    """
    todo_index = int(index_input)
    todo_index -= 1
    return todo_index


def get_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_time(hours=True):
    """
    Gets time and formats into string.
    """
    if hours:
        n = strftime('%A, %b %d, %Y %H:%M:%S')
        return n
    n = strftime('%A, %b %d, %Y')
    return n


if __name__ == '__main__':
    pass

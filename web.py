"""
TODO LIVE: Deploy on live server
- Apenas arquivos relacionados ao programa devem estar na pasta (standalone)
- Criar lista com requerimentos "requirements.txt" com -> pip freeze > requirements.txt
- "pip freeze" mostra no terminal todos as livrarias presentes no código
- "pip freeze > requirements.txt" salva informações em um arquivo de texto
- "requirements.txt" informará ao server que livrarias são necessárias para rodar o programa
- Marcar ammend ao fazer commit de mudanças não significativas
"""

import streamlit as st
import functions as f

todos_list = f.get_todos()   # gets to-dos from archive todos.txt


def add_todo():
    """
    Updates todos.txt file based on new inputs
    """
    # access widget's value according to its key (checkbox, input box, etc)
    added_todo = st.session_state['new_todo'] + '\n'

    if added_todo:
        added_todo = added_todo.capitalize()
        todos_list.append(added_todo)
        f.update_file(todos_list)
        st.session_state['new_todo'] = ''  # resets input box


# gui setup (header)
st.title('Todo List App')
st.subheader(f.get_time(hours=False))
st.text('Start being productive right now!')

# adds one checkbox for each to-do
for index, todo in enumerate(todos_list):
    todo_key = f'{todo.strip()}_{index}'
    st.checkbox(todo, key=todo_key)
    if st.session_state[todo_key]:  # verifies if user has checked any to-do
        todos_list.remove(todo)
        f.update_file(todos_list)
        del st.session_state[todo_key]  # deletes object from session_state
        st.experimental_rerun()  # updates page with new data

# on_change: action to be executed when user enters a prompt
st.text_input(label='.', placeholder='Add a new todo...', key=f'new_todo', on_change=add_todo,
              label_visibility='hidden')

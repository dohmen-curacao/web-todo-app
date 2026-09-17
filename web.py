import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todo = todo + '\n'
    todo = todo.capitalize()
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""

st.title("My Todo app")
st.subheader("This is my web todo app")
st.write("This app is meant to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Enter a new todo",
              on_change=add_todo, key='new_todo')

# st.session_state
import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This To-Do App works just like "
             "pen and paper. It works by "
             "typing in a to-do and pressing add. "
             "You can also complete to-dos "
             "by clicking the check box right "
             "next to them. Have fun with this app!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a todo",
              on_change=add_todo, key='new_todo')

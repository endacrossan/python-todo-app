import functions
import PySimpleGUI as sg

label = sg.Text("Please enter a todo item:")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg. Button("Edit")

window = sg.Window('To do app',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Century Gothic', 16))

while True:
    event, values = window.read()

    # initial logging to check button event and input box values
    #print(type(event))
    print(event)
    #print(type(values))
    print(values)
    if values is not None:
        print(values["todo"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # print(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break   # break the while loop


# window.read()  # display window

window.close()
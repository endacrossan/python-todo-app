import functions
import PySimpleGUI as sg

sg.theme('BlueMono')
label = sg.Text("Please enter a todo item:")
input_box = sg.InputText(tooltip="enter todo", key="todo", size=[31])
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[30, 10])
edit_button = sg. Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label], [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('To do app',
                   layout=layout,
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
        case "Complete":
            todo_to_complete = values['todos'][0]
            print(todo_to_complete)
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            # break   # break the while loop
            exit()


# window.read()  # display window
print("Bye")
window.close()
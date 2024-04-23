import functions
import PySimpleGUI as sg
import time

# print(time.strftime("H:M:S")
sg.theme('BlueMono')
sg.theme('Black')
label_clock = sg.Text("", key="label_clock")
label = sg.Text("Please enter a todo item:")
input_box = sg.InputText(tooltip="enter todo", key="todo", size=[31])
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[30, 10])
edit_button = sg. Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label_clock],
          [label], [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('To do app',
                   layout=layout,
                   font=('Century Gothic', 16))

while True:
    event, values = window.read(timeout=800)    # timeout=200
    #try:
    print("Event is:", event)
    # had to add an event check here for none as PySimpleGUI was causing an error
    if event is not None:
        print("running clock as event isnt NONE")
        window["label_clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))


    #LOGGING USED FOR DEBUGGING
    # print("Reached the time update....")
    #except Kill Application:

    # initial logging to check button event and input box values
    #print(type(event))
    #print(event)
    #print(type(values))
    #print(values)
    #if values is not None:
    #print(values["todo"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # print(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                # print('Please select an item to edit.')
                sg.popup("Please select an item to edit first.", font=("Century Gothic", 12))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                print(todo_to_complete)
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item to complete first.", font=("Century Gothic", 12))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
            print("Now closing window to exit app")
            print("Current event is:", event)
            print("Current values is:", values)
            #window["label_clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
            # break   # break the while loop

            #exit()



# window.read()  # display window
#print("Bye")
window.close()
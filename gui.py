import functions
import PySimpleGUI as sg

label = sg.Text("Please enter a todo item:")
input_box = sg.InputText(tooltip="enter todo")
add_button = sg.Button("Add item")

window = sg.Window('To do app', layout=[[label], [input_box], [add_button]])
window.read()  # display window
window.close()
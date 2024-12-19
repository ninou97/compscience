import PySimpleGUI as sg
import shared

layout = [
    [sg.Text("Enter String:"), sg.InputText(key="INPUT_STRING", size=(30, 1))],
    [sg.Button("Generate", expand_x=True,size=(20,3))],
    [sg.Text("Output Points:"), sg.InputText(key="OUTPUT_POINTS", size=(20, 1), readonly=True)],
]

sg.theme('LightBrown2')
window = sg.Window("Code", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Generate":
        input_string = values["INPUT_STRING"]
        if not input_string:
            sg.popup("Please enter a string.", title="Error")
            continue
        try:
            points = shared.countPoints(shared.modifyString(input_string))
            window["OUTPUT_POINTS"].update(points)
        except Exception as e:
            sg.popup(f"Error: {e}", title="Error")

window.close()
        
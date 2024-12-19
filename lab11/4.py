import PySimpleGUI as sg
import random


layout = [
    [sg.Image(filename="pngs.png", subsample=2, expand_x=True, size=(500,500))],
    [sg.Text("Randomizer bounds:"), sg.InputText(key="LOW", size=(20, 1)), sg.InputText(key="HIGH", size=(20, 1))],
    [sg.Button("Generate", expand_x=True,size=(20,3))],
    [sg.InputText(key="OUTPUT", size=(20, 1), readonly=True, expand_x=True)],
]

sg.theme('LightBrown2')
window = sg.Window("Randomizer", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Generate":
        try:
            # Get the lowest and highest bounds
            low = int(values["LOW"])
            high = int(values["HIGH"])
            # Generate a random number
            random_number = random.randint(low, high)
            # Update the output field
            window["OUTPUT"].update(random_number)
        except ValueError:
            sg.popup("Please enter valid integer bounds.", title="Error")
        except Exception as e:
            sg.popup(f"Error: {e}", title="Error")

window.close()
        
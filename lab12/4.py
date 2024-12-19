import PySimpleGUI as sg

layout = [
    [sg.Text("Number from -128 to 127:"), sg.InputText(key="NUMBER", size=(30, 1))],
    [sg.Button("Show one and two's complement", expand_x=True,size=(20,3))],
    [sg.Text("Direct code:"), sg.InputText(key="DIRECT", size=(20, 1), readonly=True)],
    [sg.Text("One's complement:"), sg.InputText(key="ONE", size=(20, 1), readonly=True)],
    [sg.Text("Two's complement:"), sg.InputText(key="TWO", size=(20, 1), readonly=True)],
]

sg.theme('LightBrown2')
window = sg.Window("Randomizer", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Show one and two's complement":
        input_string = values["NUMBER"]
        if not input_string:
            sg.popup("Please enter a num.", title="Error")
            continue
        try:
            num = ""
            num = values["NUMBER"]
            num = abs(int(num))
            if num < -128 or 127 < num:
                raise Exception("Number lesser than -128 or greater than 127.")
            binary = bin(num)[2:]
            while len(binary) < 8:
                binary = "0" + binary
            if int(values["NUMBER"]) < 0:
                binary = "1" + binary[1:]

            one = bin(0b11111111 ^ num)[2:]
            two = bin((num - 1) ^ 0b11111111)[2:]

            
            

            window["DIRECT"].update(binary)
            window["ONE"].update(one)
            window["TWO"].update(two)
        except Exception as e:
            sg.popup(f"Error: {e}", title="Error")

window.close()
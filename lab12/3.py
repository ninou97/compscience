
import PySimpleGUI as sg
import random

c_image = [[sg.Image("bio.png")]]
c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
           [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

def calculateBacterias(k,x,count):
    for _ in range(count):
        b = random.randint(0, 4)  # Случайное число от 0 до 4
        x = k*x + b

    return x


while 1:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    # micro = value["micro"]  #здесь хранится количество бактерий изначально
    # count = value["count"]  #здесь хранится количество секунд для которых требуется рассчитать
    # res = 0                 #здесь будет храниться результат


    #код надо писать здесь

    x = int(value["micro"])  
    count = int(value["count"])  
    k = 2  

    res = calculateBacterias(k,x,count)


    if event == "Рассчитать":
        try:
            window["res"].update(res)

        except ValueError:
            window["res"].update("Ошибка")
            sg.popup("Введите корректные числа!", title="Ошибка")


window.close()


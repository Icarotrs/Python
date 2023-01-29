import PySimpleGUI as sg
import math

def calculate():
    try:
        expression = values['input']
        result = eval(expression)
        sg.popup(result)
    except:
        sg.popup("Error")

layout = [
    [sg.Input(key='input')],
    [sg.Button('Sin'), sg.Button('Cos'), sg.Button('Tan'), sg.Button('Log')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('+')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('*')],
    [sg.Button('.'), sg.Button('0'), sg.Button('='), sg.Button('/')],
    [sg.Button('Exp'), sg.Button('Pi')]
]

window = sg.Window('Calculadora Científica', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    if event in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/'):
        window['input'].update(values['input'] + event)
    if event in ('Sin', 'Cos', 'Tan', 'Log', 'Exp', 'Pi'):
        window['input'].update(values['input'] + event + '(')
    if event == '=':
        calculate()

window.close()

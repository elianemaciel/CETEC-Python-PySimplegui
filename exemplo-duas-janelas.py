import PySimpleGUI as sg

layout_janela1 = [
    [sg.Text('janela1')],
    [sg.Button('exit')]
]

janela1 = sg.Window('Titulo Janela 1', layout_janela1)
layout_janela2 = [
    [sg.Text('janela2')],
    [sg.Button('exit')]
]

janela2 = sg.Window('Titulo Janela 2', layout_janela2)

janela2.move(janela1.current_location()[0], janela1.current_location()[1]+220)

while True:
    janela, eventos, valores = sg.read_all_windows()

    if janela == sg.WIN_CLOSED:
        break
    if eventos == 'exit':
        break

janela.close()

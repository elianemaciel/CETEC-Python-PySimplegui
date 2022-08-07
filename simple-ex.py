
import PySimpleGUI as sg

# Adicionando tema a interface gráfica
sg.theme('DarkTeal2')


# Dentro da variável layout deve ter todos os campos contidos na tela

layout = [
    [sg.Text ("Nome:     "), sg.Input( key ='nome')],  # Cada linha é delimitada por colchetes
    [sg.Text ("e-mail:"), sg.Input( key ='email')],
    [sg.Text ("endereço:        "), sg.Input( key ='end')],
    [sg.Button ("Registrar") ],
    [sg.Text (key="text") ],
]
# Criação da janela
janela = sg.Window ("Cadastro de cliente", layout )

# Cria o evento de loop
while True :
    eventos , valores = janela.read ()
    
    if eventos == "Registrar" or eventos == sg.WIN_CLOSED :
        # Atualiza a variável de texto
        janela['text'].update('Salvo com sucesso')

        break

janela.close ()
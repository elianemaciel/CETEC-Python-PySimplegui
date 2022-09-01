import PySimpleGUI as pg

layout = [
    [pg.Text("Selecione um arquivo"), pg.FileBrowse(key="arquivo")],
    [pg.Button("Ler arquivo")],
    [pg.Button("Cadastrar aluno")],
    
]

janela = pg.Window("Cadastro de alunos", layout)

while True:
    eventos, valores = janela.read()

    if eventos == "Ler arquivo":
        nome_arquivo = valores['arquivo']
        arquivo = open(nome_arquivo, 'r+')
        linhas = arquivo.readlines()
        print(linhas)
        for linha in linhas:
            print(linha)

        
    if eventos == pg.WIN_CLOSED :
        break

janela.close()


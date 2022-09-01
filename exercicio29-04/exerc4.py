import PySimpleGUI as pg

lista_codigos = []
lista_nomes = []

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
        for linha in linhas:
            aux = linha.split(',')
            lista_codigos.append(aux[0])
            lista_nomes.append(aux[1])

        
    if eventos == pg.WIN_CLOSED :
        break

janela.close()


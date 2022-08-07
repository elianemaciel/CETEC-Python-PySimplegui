import PySimpleGUI as pg


layout = [
    [pg.Text("Valor em R$:"), pg.Input(key="valor-real")],
    [pg.Button("Calcular")],
    [pg.Text(key="valor-dolar")]
]


janela = pg.Window("Conversão de valores", layout)


while True:
    eventos, valores = janela.read()


    if eventos == "Calcular":
        valor_real = float(valores['valor-real'])
        total = valor_real / 5.10
        janela['valor-dolar'].update(
            f"Total em dolar : U$ {total}"
        )
    if eventos == pg.WIN_CLOSED :
        break


janela.close()
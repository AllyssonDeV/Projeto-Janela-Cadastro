from PySimpleGUI import PySimpleGUI as sg

# .:layout:.
sg.theme("Reddit")
layout = [
    [sg.Text("Usuário:"), sg.Input(key="usuario", size=( 20, 1))],
    [sg.Text("Senha:  "), sg.Input(key="senha", password_char="*", size=( 20, 1))],
    [sg.Checkbox("Salvar o login?")],
    [sg.Button("Entrar")]
]
cor1= "#3b3b3b"
# .:Janela:.
janela = sg.Window("Tela de login", layout)


# .:Ler os eventos:.
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos =="Entrar":
        if valores["usuario"] == "Allysson" and valores["senha"] == "12345678": 
            janela1 = sg.popup('Seja bem vindo!')
        else: janela1 = sg.popup("Usuário ou senha não estão corretos!")
        
import PySimpleGUI as sg

class TelaSistema():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Button('Cliente', key='1', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Funcionario', key='2', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Carro', key='3', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Aluguel', key='4', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Finalizar sistema', key='0', size=(22, 1), button_color='#500000')],
                  ]
        self.__window = sg.Window('HOME').Layout(layout)
        

    def tela_opcoes(self):
        self.init_components()
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        self.close()
        return int(botao)

    def close(self):
        self.__window.close()

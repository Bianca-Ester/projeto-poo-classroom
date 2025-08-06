'''
1) Configurar funções
2) alterar 'self.label_matricula_resutado' para combobox
3) criar função em 'mat' para criar uma lista de turmas que determinada matricula faz parte
4) atualizar o combobox vazio
5) habilitar botões
'''

from tkinter import Frame, Label, Entry, Button, CENTER
import manipulacao_arquivos.manipulador_arquivos_turma as mat

class JanelaAcessarTurma:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_matricula = Label(self.frame, text="Matrícula:")
        label_matricula.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_matricula = Entry(self.frame)
        self.entrada_matricula.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        self.entrada_matricula.focus()

        self.botao = Button(self.frame, text="Buscar", command=self.buscar_turma)
        self.botao.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.label_matricula_resultado = Label(self.frame) #turn into combobox
        self.label_matricula_resultado.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        self.botao_acessar = Button(self.frame, text="Acessar", command=self.acessar_turma, state="disabled") #habilitar
        self.botao_acessar.grid(row=6, column=0, sticky="E", padx=5, pady=5)

        self.botao_remover = Button(self.frame, text="Remover", command=self.remover_turma, state='disabled') #habilitar
        self.botao_remover.grid(row=6, column=1, sticky='W', padx=5, pady=5)

    def limpar_campos(self):
        self.entrada_matricula.delete(0 ,'end')        
        self.entrada_matricula.focus()

    def buscar_turma(self):
        self.limpar_campos()
        #terminar
        
    def acessar_turma(self):
        self.limpar_campos()
        #terminar

    def remover_turma(self):
        self.limpar_campos()
        #terminar
    

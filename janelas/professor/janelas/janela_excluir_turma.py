from tkinter import Frame, Label, Entry, Button, tkk, messagebox, CENTER

class JanelaExcluirTurma:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_nome_turma = Label(janela, text="Turma:")
        label_nome_turma.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_turma = Entry(janela)
        self.entrada_turma.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        self.entrada_turma.focus()

        '''
        se existir uma turma igual ao nome:
            self.botao = Button(janela, text="Excluir", command=self.excluir_turma)
            self.botao.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        else:
            erro = messagebox.showerror('Erro', 'Turma não encontrada')
        '''

    def limpar_campos(self):
        self.entrada_turma.delete(0 ,'end')        
        self.entrada_codigo.delete(0 ,'end')

        self.entrada_turma.focus()

    def excluir_turma(self):
        self.limpar_campos()
        #terminar

#configurar funções

from tkinter import Frame, Label, Entry, Button, ttk, messagebox, CENTER
import manipulacao_arquivos.manipulador_arquivos_turma as mat

class JanelaSairTurma:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_nome_turma = Label(janela, text="Turma:")
        label_nome_turma.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_turma = Entry(janela)
        self.entrada_turma.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        self.entrada_turma.focus()

        nome_digitado_turma = self.entrada_turma.get()
        turma = mat.buscar_turma_por_nome(nome_digitado_turma)        
        if turma:
            self.botao = Button(janela, text="Sair", command=self.sair_turma)
            self.botao.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        else:
            messagebox.showerror('Erro', 'Turma não encontrada')

    def limpar_campos(self):
        self.entrada_turma.delete(0 ,'end')        
        self.entrada_codigo.delete(0 ,'end')

        self.entrada_turma.focus()

    def sair_turma(self):
        self.limpar_campos()
        #terminar

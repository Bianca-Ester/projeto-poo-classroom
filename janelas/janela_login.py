from tkinter import Frame, Label, Entry, Button, ttk, messagebox, CENTER
import manipulacao_arquivos.manipulador_arquivos_aluno as maa
import manipulacao_arquivos.manipulador_arquivos_professor as map
import utils as ut
from janelas.professor.janela_principal_professores import JanelaPrincipalProfessor
from janelas.aluno.janela_principal_alunos import JanelaPrincipalAluno

class JanelaLogin:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_matricula = Label(self.frame, text="Matrícula:")
        label_matricula.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_matricula = Entry(self.frame)
        self.entrada_matricula.grid(row=0, column=1, sticky="W", padx=5, pady=5)

        label_senha = Label(self.frame, text="Senha:")
        label_senha.grid(row=1, column=0, sticky="E", padx=5, pady=5)

        self.entrada_senha = Entry(self.frame)
        self.entrada_senha.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        opcoes = ["Aluno", "Professor"]
        self.combobox = ttk.Combobox(self.frame, values=opcoes, state="readonly")
        self.combobox.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        self.combobox.set("Selecione uma opção")

        botao = Button(self.frame, text="Salvar", command=self.selecao_combobox)
        botao.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def limpar_campos(self):
        self.entrada_matricula.delete(0 ,'end')
        self.entrada_senha.delete(0, 'end')
        
        self.entrada_matricula.focus()

    def abrir_janela_principal_professor(self):
        self.limpar_campos()
        JanelaPrincipalProfessor()

    def abrir_janela_principal_aluno(self):
        self.limpar_campos()
        JanelaPrincipalAluno()

    def check_existencia_professor(self):
        matricula_digitada = self.entrada_matricula.get()
        
        var = map.buscar_professor_por_matricula(matricula_digitada)
        if var is not None:
            self.abrir_janela_principal_aluno()
        else:
            messagebox.showerror("Erro", "Professor não encontrado")

    def check_existencia_aluno(self):
        matricula_digitada = self.entrada_matricula.get()
        
        var = maa.buscar_aluno_por_matricula(matricula_digitada)
        if var is not None:
            self.abrir_janela_principal_aluno()
        else:
            messagebox.showerror("Erro", "Aluno não encontrado")

    def check_preenchimento_campos(self):
        matricula = self.entrada_matricula.get()
        senha = self.entrada_senha.get()        
        recuperacao_combobox = self.combobox.get()

        if not matricula or not senha or not recuperacao_combobox:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
        else:
            self.selecao_combobox()

    def selecao_combobox(self):
        recuperacao_combobox = self.combobox.get()
        
        if recuperacao_combobox == "Professor":
            self.check_existencia_professor()
        elif recuperacao_combobox == "Aluno":
            self.check_existencia_aluno()
        else:
            messagebox.showerror('Erro', 'Selecione aluno ou professor')


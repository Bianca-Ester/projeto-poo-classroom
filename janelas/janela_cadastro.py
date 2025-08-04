from tkinter import Frame, Label, Entry, Button, ttk, messagebox, CENTER
import manipulacao_arquivos.manipulador_arquivos_aluno as maa
import manipulacao_arquivos.manipulador_arquivos_professor as map
import utils as ut
from models.aluno import Aluno
from models.professor import Professor

class JanelaCadastro:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_matricula = Label(self.frame, text="Matrícula:")
        label_matricula.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_matricula = Entry(self.frame)
        self.entrada_matricula.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        self.entrada_matricula.focus()

        label_senha = Label(self.frame, text="Senha:")
        label_senha.grid(row=1, column=0, sticky="E", padx=5, pady=5)

        self.entrada_senha = Entry(self.frame)
        self.entrada_senha.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        opcoes = ["Aluno", "Professor"]
        self.combobox = ttk.Combobox(self.frame, values=opcoes)
        self.combobox.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        self.combobox.set("Selecione uma opção")

        botao = Button(self.frame, text="Salvar", command=self.check_preenchimento_campos)
        botao.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def limpar_campos(self):
        self.entrada_matricula.delete(0 ,'end')
        self.entrada_senha.delete(0, 'end')
        
        self.entrada_matricula.focus()

    def cadastrar_professor(self):
        matricula = self.entrada_matricula.get()
        senha = self.entrada_senha.get()
        
        professor = Professor(senha, matricula)       
        resultado, professor = map.adicionar_professor(professor)                
        ut.exibir_mensagem(resultado, "Cadastrado com sucesso!", "Erro no cadastro.")       
        self.limpar_campos()
        self.entrada_matricula.focus()


    def cadastrar_aluno(self):
        matricula = self.entrada_matricula.get()
        senha = self.entrada_senha.get()
        
        aluno = Aluno(senha, matricula)       
        resultado, aluno = maa.adicionar_aluno(aluno)                
        ut.exibir_mensagem(resultado, "Cadastrado com sucesso!", "Erro no cadastro.")       
        self.limpar_campos()
        self.entrada_matricula.focus()

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
            self.cadastrar_professor()
        elif recuperacao_combobox == "Aluno":
            self.cadastrar_aluno()
        else:
            messagebox.showerror('Erro', 'Selecione aluno ou professor')

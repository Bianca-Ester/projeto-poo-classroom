from tkinter import Tk, Menu
from janelas.aluno.janelas.janela_acessar_turma import JanelaAcessarTurma
from janelas.aluno.janelas.janela_sair_turma import JanelaSairTurma

class JanelaPrincipalAluno:
    def __init__(self):
        self.janela = Tk()   
        self.janela.title("Área do Aluno")

        self.menu_bar = Menu(self.janela)

        self.menu_turmas = Menu(self.menu_bar, tearoff=0)
        self.menu_turmas.add_command(label="Buscar", command=self.abrir_janela_acessar_turma)
        self.menu_turmas.add_command(label="Desinscrever", command=self.abrir_janela_sair_turma)

        self.menu_bar.add_command(label="Sair", command=self.janela.quit)

        self.centralizar_janela()
        self.janela.mainloop()

    def centralizar_janela(self):
        largura = 350
        altura = 300
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()

        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)

        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def limpar_widgets(self):
        if len(self.janela.winfo_children()) > 1:
            self.janela.winfo_children()[1].destroy()

    def abrir_janela_acessar_turma(self):
        self.limpar_widgets()
        JanelaAcessarTurma(self.janela)

    def abrir_janela_sair_turma(self):
        self.limpar_widgets()
        JanelaSairTurma(self.janela)

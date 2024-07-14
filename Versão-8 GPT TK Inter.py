import tkinter as tk
from tkinter import simpledialog, messagebox

class Invalida:
    @staticmethod
    def erro():
        messagebox.showerror("Erro", "Opção inválida! Digite novamente!")

def Linha_Divisoria():
    print("----------------------------------\n----------------------------------")

def Linha_Divisoria_Simples():
    print("----------------------------------")

class Identificador:
    def __init__(self, root):
        self.root = root

    def pergunta(self):
        while True:
            x = simpledialog.askinteger("Identificação", 
                                        "Digite 0 para Terminar o Programa\nDigite 1 para entrar como professor\nDigite 2 para entrar como aluno")
            if x is None:
                continue

            if x == 0:
                Fim(x)
                break

            elif x == 1:
                self.perfil = IdentificadorPessoa(self.root)
                self.perfil.identificando()
                MenuProfessor(self.perfil, self.root)

            elif x == 2:
                self.perfil = IdentificadorAluno(self.root)
                self.perfil.identificando()
                perguntas_aluno = PerguntasAluno(self.perfil.nome, self.root)
                perguntas_aluno.perguntas()
                
            else:
                Invalida.erro()

class IdentificadorPessoa(Identificador):
    def identificando(self):
        self.nome = simpledialog.askstring("Identificação", "Digite o seu nome:")
        messagebox.showinfo("Bem-vindo", f"Olá Professor {self.nome}! \nSeja bem-vindo à ESTANTE VIRTUAL!")
        Linha_Divisoria()
        print("Esse programa foi desenvolvido por GABRIEL REHBEIN")
        print("Esse Programa tem como objetivo organizar as salas de vocês professores")
        print("assim como organizar a vida de nossos alunos!")
        Linha_Divisoria()

class IdentificadorAluno(Identificador):
    def identificando(self):
        self.nome = simpledialog.askstring("Identificação", "Digite o seu nome:")
        messagebox.showinfo("Bem-vindo", f"Olá Aluno {self.nome}! \nSeja bem-vindo à ESTANTE VIRTUAL!")
        Linha_Divisoria_Simples()
        print("Não esqueça de fazer os temas!")
        Linha_Divisoria_Simples()

class Adicionar_atividade:
    def __init__(self, root):
        self.root = root
        self.atividade = simpledialog.askstring("Atividade", "Qual é a atividade?")
        self.materia = simpledialog.askstring("Atividade", "De que matéria é a atividade?")
        self.vale_nota = simpledialog.askstring("Atividade", "Esta atividade vale nota? (SIM/NÃO)").strip().upper()

        if self.vale_nota == "SIM":
            try:
                self.pontos = float(simpledialog.askstring("Atividade", "Quantos pontos vale essa atividade?"))
                messagebox.showinfo("Atividade", f"Atividade '{self.atividade}' da matéria '{self.materia}' postada. Vale {self.pontos} pontos.")
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido para pontos. Atividade não foi postada.")
        else:
            messagebox.showinfo("Atividade", f"Atividade '{self.atividade}' da matéria '{self.materia}' postada.")

class Fim:
    def __init__(self, x):
        messagebox.showinfo("Fim", f"Você digitou {x}\nFim do Programa")
        Linha_Divisoria()
        print("Esta é a versão 6 deste programa, em breve haverá novas atualizações!")

class PerguntasAluno:
    def __init__(self, nome, root):
        self.root = root
        self.temas = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.media = None
        self.nome = nome

    def mensagem_de_erro_aluno(self):
        messagebox.showerror("Erro", f"Por favor Aluno {self.nome}, digite corretamente!")

    def perguntas(self):
        self.trabalhos()
        
    def trabalhos(self):
        self.temas = simpledialog.askstring("Trabalhos", "Você já fez todos os trabalhos? (SIM/NÃO)").strip().upper()
        if self.temas == "SIM":
            self.receber_notas()
        elif self.temas == "NÃO":
            self.mensagem()
        else:
            self.mensagem_de_erro_aluno()

    def receber_notas(self):
        try:
            self.p1 = float(simpledialog.askstring("Notas", "Você tirou quanto na primeira prova?"))
            self.p2 = float(simpledialog.askstring("Notas", "E na segunda?"))
            self.p3 = float(simpledialog.askstring("Notas", "E na trimestral?"))
            self.calcular_media()
            messagebox.showinfo("Média", f"Sua média foi {self.media:.2f}")
            self.passou()
        except ValueError:
            self.mensagem_de_erro_aluno()

    def mensagem(self):
        messagebox.showinfo("Mensagem", "Olá Aluno! Não esqueça de realizar todos os trabalhos!")
        Linha_Divisoria_Simples()

    def calcular_media(self):
        self.media = (self.p1 + self.p2 + self.p3) / 3

    def passou(self):
        if self.media >= 6:
            messagebox.showinfo("Resultado", f"Sua média foi {self.media:.2f}, parabéns! Você passou de ano!")
        else:
            messagebox.showinfo("Resultado", f"Sua média foi {self.media:.2f}, você foi reprovado...")

class EstanteDoGabriel:
    def __init__(self):
        self.nichos = {}
        l_salas = [1, 2, 3, 4, 5, 6, 7, 8]
        for sala in l_salas:
            for x in range(5):
                self.nichos[sala * 10 + x] = None

    def colocar_pote_na_estante(self, numero, pote):
        self.nichos[numero] = pote

    def retirar_pote_da_estante(self, numero):
        pote = self.nichos[numero]
        self.nichos[numero] = None
        return pote

    def imprimir(self):
        estante_str = ""
        for k, n in self.nichos.items():
            estante_str += f"{k}: {n}\n"
        messagebox.showinfo("Estante", estante_str)

class Pote:
    def __init__(self, numero):
        self.chave = None
        self.numero = numero
        self.caneta = None
        self.ctrl_ar = None
        self.ctrl_projetor = None

    def imprimir(self):
        print(f"{self.chave} - {self.numero} {self.caneta} - {self.ctrl_ar} - {self.ctrl_projetor}")

    def __str__(self):
        return f"{self.chave} - {self.numero} {self.caneta} - {self.ctrl_ar} - {self.ctrl_projetor}"

class Usuarios:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Usuario(Usuarios):
    def __init__(self, nome, endereco, telefone):
        super().__init__(nome, endereco, telefone)
        self.pote = None

class Funcionario(Usuarios):
    def __init__(self, nome, endereco, telefone, num_func, setor):
        super().__init__(nome, endereco, telefone)
        self.num_func = num_func
        self.setor = setor

class Professor(Usuarios):
    def __init__(self, nome, endereco, telefone, num_func, turno):
        super().__init__(nome, endereco, telefone)
        self.num_func = num_func
        self.turno = turno

    def pegar_pote(self, num_sala, estante):
        self.pote = estante.retirar_pote_da_estante(num_sala)

    def imprimir(self):
        messagebox.showinfo("Professor", f"{self.nome} - {self.pote}")

def MenuProfessor(professor, root):
    estante = EstanteDoGabriel()

    while True:
        x = simpledialog.askinteger("Menu Professor", "Digite 0 para Terminar o Programa\nDigite 1 para Gerenciamento de salas\nDigite 2 para Gerenciar atividades do aluno")

        if x is None:
            continue

        if x == 0:
            Fim(x)
            break

        elif x == 1:
            GerenciamentoSalas(estante, root)

        elif x == 2:
            messagebox.showinfo("Gerenciamento de Atividades", "\n--------> Gerenciando Atividades do Aluno <--------")
            Adicionar_atividade(root)

        else:
            Invalida.erro()

def GerenciamentoSalas(estante, root):
    while True:
        x = simpledialog.askinteger("Gerenciamento de Salas", "Digite 0 para Terminar o Gerenciamento de Salas\nDigite 1 para Colocar pote na Estante\nDigite 2 para Retirar pote da estante\nDigite 3 para Imprimir elementos dentro do Pote")

        if x is None:
            continue

        if x == 0:
            Fim(x)
            break

        elif x == 1:
            messagebox.showinfo("Estante", "\n--------> Colocando Pote na Estante <--------")
            num_sala = simpledialog.askinteger("Estante", "Digite o número da sala:")
            numero_pote = simpledialog.askinteger("Estante", "Digite o número do pote:")
            pote = Pote(numero_pote)
            estante.colocar_pote_na_estante(num_sala, pote)
            messagebox.showinfo("Estante", f"Pote {numero_pote} colocado na sala {num_sala}.")
            Linha_Divisoria_Simples()

        elif x == 2:
            messagebox.showinfo("Estante", "\n--------> Retirando Pote da Estante <--------")
            num_sala = simpledialog.askinteger("Estante", "Digite o número da sala:")
            pote_retirado = estante.retirar_pote_da_estante(num_sala)
            if pote_retirado:
                messagebox.showinfo("Estante", f"Pote {pote_retirado.numero} retirado da sala {num_sala}.")
            else:
                messagebox.showinfo("Estante", "Não há pote na sala especificada.")
            Linha_Divisoria_Simples()

        elif x == 3:
            messagebox.showinfo("Estante", "\n--------> Imprimindo Potes na Estante <--------")
            estante.imprimir()
            Linha_Divisoria_Simples()

        else:
            Invalida.erro()

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    identificador = Identificador(root)
    identificador.pergunta()

if __name__ == "__main__":
    main()


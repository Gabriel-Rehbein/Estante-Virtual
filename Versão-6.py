class Invalida:
    @staticmethod
    def erro():
        print("Opção inválida! Digite novamente!")

def Linha_Divisoria():
    print("----------------------------------\n----------------------------------")

def Linha_Divisoria_Simples():
    print("----------------------------------")

class Identificador:
    def pergunta(self):
        while True:
            try:
                x = int(input("Digite 0 para Terminar o Programa\nDigite 1 para entrar como professor \nDigite 2 para entrar como aluno\n"))

                if x == 0:
                    Fim(x)
                    break

                elif x == 1:
                    self.perfil = IdentificadorPessoa()
                    self.perfil.identificando()
                    MenuProfessor(self.perfil)

                elif x == 2:
                    self.perfil = IdentificadorAluno()
                    self.perfil.identificando()
                    perguntas_aluno = PerguntasAluno()
                    perguntas_aluno.perguntas()
                    

                else:
                    print("Opção inválida! Por favor, digite o número 0, 1 ou 2!")

            except ValueError:
                Invalida.erro()


class IdentificadorPessoa(Identificador):
    def identificando(self):
        self.nome = input("Digite o seu nome: ")
        print(f"Olá Professor {self.nome}! \nSeja bem-vindo à ESTANTE VIRTUAL!")
        Linha_Divisoria()
        print("Esse programa foi desenvolvido por GABRIEL REHBEIN")
        print("Esse Programa tem como objetivo organizar as salas de vocês professores")
        print("assim como organizar a vida de nossos alunos!")
        Linha_Divisoria()

class IdentificadorAluno(Identificador):
    def identificando(self):
        self.nome = input("Digite o seu nome: ")
        print(f"Olá Aluno {self.nome}! \nSeja bem-vindo à ESTANTE VIRTUAL!")
        Linha_Divisoria_Simples()
        print("Não esqueça de fazer os temas!")
        Linha_Divisoria_Simples()

class Adicionar_atividade:
    def __init__(self):
        self.atividade = input("Qual é a atividade? ")
        self.materia = input("De que matéria é a atividade? ")
        self.vale_nota = input("Esta atividade vale nota? (SIM/NÃO) ").strip().upper()

        if self.vale_nota == "SIM":
            try:
                self.pontos = float(input("Quantos pontos vale essa atividade? "))
                print(f"Atividade '{self.atividade}' da matéria '{self.materia}' postada. Vale {self.pontos} pontos.")
            except ValueError:
                print("Valor inválido para pontos. Atividade não foi postada.")
        else:
            print(f"Atividade '{self.atividade}' da matéria '{self.materia}' postada.")

class Fim:
    def __init__(self, x):
        print(f"Você digitou {x}")
        Linha_Divisoria_Simples()
        print("Fim do Programa")
        Linha_Divisoria()
        print("Esta é a versão 6 deste programa, em breve haverá novas atualizações!")

class PerguntasAluno:
    def __init__(self):
        self.temas = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.media = None
        self.nome = None

    def mensagem_de_erro_aluno(self):
        print(f"Por favor Aluno {self.nome}, digite corretamente!")

    def perguntas(self):
        self.identificador = IdentificadorAluno()
        self.identificador.pergunta()
        self.nome = self.identificador.nome
        self.identificador.identificando()
        self.trabalhos()
        
    def trabalhos(self):
        self.temas = input("Você já fez todos os trabalhos? (SIM/NÃO) ").strip().upper()
        if self.temas == "SIM":
            self.receber_notas()
        elif self.temas == "NÃO":
            self.mensagem()
        else:
            self.mensagem_de_erro_aluno()

    def receber_notas(self):
        try:
            self.p1 = float(input("Você tirou quanto na primeira prova? "))
            self.p2 = float(input("E na segunda? "))
            self.p3 = float(input("E na trimestral? "))
            self.calcular_media()
            print(f"Sua média foi {self.media:.2f}")
            self.passou()
        except ValueError:
            self.mensagem_de_erro_aluno()

    def mensagem(self):
        print("Olá Aluno! Não esqueça de realizar todos os trabalhos!")
        Linha_Divisoria_Simples()

    def calcular_media(self):
        self.media = (self.p1 + self.p2 + self.p3) / 3

    def passou(self):
        if self.media >= 6:
            print(f"Sua média foi {self.media:.2f}, parabéns! Você passou de ano!")
        else:
            print(f"Sua média foi {self.media:.2f}, você foi reprovado...")

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
        for k, n in self.nichos.items():
            print(k, n)

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
        print(f"{self.nome} - {self.pote}")

def MenuProfessor(professor):
    estante = EstanteDoGabriel()

    while True:
        try:
            x = int(input("Digite 0 para Terminar o Programa\nDigite 1 para Gerenciamento de salas\nDigite 2 para Gerenciar atividades do aluno\n"))

            if x == 0:
                Fim(x)
                break

            elif x == 1:
                GerenciamentoSalas(estante)

            elif x == 2:
                print("\n--------> Gerenciando Atividades do Aluno <--------")
                Adicionar_atividade()

            else:
                Invalida.erro()
        
        except ValueError:
            Invalida.erro()

def GerenciamentoSalas(estante):
    while True:
        try:
            x = int(input("Digite 0 para Terminar o Gerenciamento de Salas\nDigite 1 para Colocar pote na Estante\nDigite 2 para Retirar pote da estante\nDigite 3 para Imprimir elementos dentro do Pote: "))

            if x == 0:
                Fim(x)
                break

            elif x == 1:
                print("\n--------> Colocando Pote na Estante <--------")
                num_sala = int(input("Digite o número da sala: "))
                numero_pote = int(input("Digite o número do pote: "))
                pote = Pote(numero_pote)
                estante.colocar_pote_na_estante(num_sala, pote)
                print(f"Pote {numero_pote} colocado na sala {num_sala}.")
                Linha_Divisoria_Simples()

            elif x == 2:
                print("\n--------> Retirando Pote da Estante <--------")
                num_sala = int(input("Digite o número da sala: "))
                pote_retirado = estante.retirar_pote_da_estante(num_sala)
                if pote_retirado:
                    print(f"Pote {pote_retirado.numero} retirado da sala {num_sala}.")
                else:
                    print("Não há pote na sala especificada.")
                Linha_Divisoria_Simples()

            elif x == 3:
                print("\n--------> Imprimindo Potes na Estante <--------")
                estante.imprimir()
                Linha_Divisoria_Simples()

            else:
                Invalida.erro()

        except ValueError:
            Invalida.erro()

identificador = Identificador()
identificador.pergunta()

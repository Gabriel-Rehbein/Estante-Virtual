#Gabriel Menezes Rehbein

class Estante_do_gabriel:
    def __init__(self):
        self.nichos = {}
        l_salas = [1, 2, 3, 4, 5, 6, 7, 8]

        for sala in l_salas:
            for x in range(5):
                self.nichos[sala + x] = None

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


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.pote = None

    def pegar_pote(self, num_sala, estante):
        self.pote = estante.retirar_pote_da_estante(num_sala)

    def imprimir(self):
        print(f"{self.nome} - {self.pote}")


class Linha_Divisoria:
    def __init__(self):
        print("----------------------------------\n----------------------------------")


class Linha_Divisoria_Simples:
    def __init__(self):
        print("----------------------------------")


class Menu:
    Linha_Divisoria()
    estante = Estante_do_gabriel()

    while True:
        x = input("Digite 0 para Terminar o Programa\n Digite 1 para Colocar pote na Estante\n Digite 2 para Retirar pote da estante\n Digite 3 para Imprimir elementos dentro do Pote: ")

        x = int(x)

        if (x == 0):
            print(f"Você digitou {x}")
            Linha_Divisoria_Simples()
            print("Fim do Programa")
            break

        elif (x == 1):
            print(f"Você digitou {x} \n Colocando Pote")
            Linha_Divisoria_Simples()
            num_sala = int(input("Digite o número da sala: "))
            numero_pote = int(input("Digite o número do pote: "))
            pote = Pote(numero_pote)
            estante.colocar_pote_na_estante(num_sala, pote)
            print("Pote colocado na estante.")

        elif (x == 2):
            print(f"Você digitou {x} \n Retirando pote")
            Linha_Divisoria_Simples()
            num_sala = int(input("Digite o número da sala: "))
            pote_retirado = estante.retirar_pote_da_estante(num_sala)
            if pote_retirado:
                print(f"Pote retirado da sala {num_sala}.")
            else:
                print(f"A sala {num_sala} está vazia.")

        elif (x == 3):
            print(f"Você digitou {x} \n Imprimindo elementos do Pote")
            Linha_Divisoria_Simples()
            num_sala = int(input("Digite o número da sala: "))
            pote = estante.nichos[num_sala]
            if pote:
                print("Elementos do pote:")
                pote.imprimir()
            else:
                print(f"A sala {num_sala} está vazia.")

        else:
            print("Por favor, digite corretamente!")

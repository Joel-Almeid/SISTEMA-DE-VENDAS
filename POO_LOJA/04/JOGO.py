#THIAGO
# importando as funções necessarias
import random
import time

# Apenas cosmetico
def escreva(x):
    ler = len(x) + 4
    print("-" * ler)
    print(f"  {x}")
    print("-" * ler)

# função para visualizar os status dos perssonagens em batalha, reduzindo linhas de codigo


def visualizar():
    print(f"\nStatus: {jogador1.nome} - Vida: {jogador1.vida}, Energia: {jogador1.energia}")
    print(f"Status: {jogador2.nome} - Vida: {jogador2.vida}, Energia: {jogador2.energia}\n")


# criando a classe principal erdada pelas outras seguintes
#o self refere a instancia atua
class Personagem:
    def _init_(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.energia = 50

    # definindo metodo principal atacar, que será igual a todos os perssonagens

    def atacar(self, alvo):
        dano = random.randint(5, 15)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")
        return dano

#JOEL
# Define uma classechamada arqueiro que herda da classe base 'Personagem'

class Guerreiro(Personagem):
    def habilidade_especial(self, alvo):
        if self.energia >= 10:
            dano = random.randint(12, 28)
            alvo.vida -= dano     #subtrai o dano dos pontos de vida do (alvo.vida)
            self.energia -= 10    #Supõe  que tem 8 pontos de energia do arqueiro
            print(f"\n{self.nome} usa habilidade especial em {alvo.nome} causando {dano} de dano!") #imprime uma mensagem indicando que o arqueiro usa habilidade especial no alvo
            return dano
        else:
            print(f"\n{self.nome} não tem energia suficiente para usar a habilidade especial!")  #se a energia for insuficiente, imprime uma msg que o arqueiro não pode usar habilidade especial
            return 0      #retorna 0 de dano

class Arqueiro(Personagem):
    def habilidade_especial(self, alvo):
        if self.energia >= 8:
            dano = random.randint(16, 24)
            alvo.vida -= dano
            self.energia -= 8
            print(f"\n{self.nome} usa habilidade especial em {alvo.nome} causando {dano} de dano!")
            return dano
        else:
            print(f"\n{self.nome} não tem energia suficiente para usar a habilidade especial!")
            return 0


class Paladino(Personagem):
    def habilidade_especial(self, alvo):
        if self.energia >= 10:
            regen = random.randint(5, 25)
            self.vida += regen
            self.energia -= 10

            print(f"\n{self.nome} usa habilidade especial recuperando {regen} de vida!")
            return regen

        else:
            print(f"\n{self.nome} não tem energia suficiente para usar a habilidade especial!")
            return 0


class Necromante(Personagem):

    def habilidade_especial(self, alvo):
        pass

    def renascer(self):
        if self.energia >= 50:
            self.vida += 50
            self.energia -= 50
            print(f"\nNecromante {self.nome} ressurge das sombras como um lich!!\n")
        else:
            print("\nNecromante tenta reviver novamente, porém os DEVs não permitem.\n")
        return self.vida

#LUCAS
# aqui definimos uma função para instanciar os objetos das classes ate então criadas
def criar_personagem():
    while True:
        nome = input("Digite o nome do seu personagem: ")
        if nome == '':
            print("Coloque um nome por favor.")
        else:
            break
    classe = ''
    while classe not in ['guerreiro', 'arqueiro', 'paladino', 'necromante']:
        classe = input("Escolha uma classe (Guerreiro/Arqueiro/Paladino/Necromante): ").lower()
        if classe not in ['guerreiro', 'arqueiro', 'paladino', 'necromante']:
            print("Classe inválida. Por favor, escolha 'Guerreiro', 'Arqueiro', 'Paladino' ou 'Necromante'.")
    if classe == 'guerreiro':
        return Guerreiro(nome, classe)
    elif classe == 'paladino':
        return Paladino(nome, classe)
    elif classe == 'necromante':
        return Necromante(nome, classe)
    else:
        return Arqueiro(nome, classe)


# aqui é onde o codigo realmente começa a funcionar, de forma que há dois jogadores que interagem entre si usando das
# intancias dass classes

print("\nCriação do Jogador 1:")
jogador1 = criar_personagem()
print("\nCriação do Jogador 2:")
jogador2 = criar_personagem()
print("\n\n\n\n\n")

# aqui a batalha entre os jogadores acontece em formato de turnos
while jogador1.vida > 0 and jogador2.vida > 0:

    # a variavel esp define a chance de um dos objetos utlizar o metodo 'habilidade especial'
    esp = random.randint(1, 3)
    jogador1.atacar(jogador2)
    jogador2.atacar(jogador1)
    if esp == 1:
        jogador1.habilidade_especial(jogador2)
    elif esp == 2:
        jogador2.habilidade_especial(jogador1)

#WILTON
    # estas proximas linhas de codigo definem que um objeto não fique com o atributo vida negativo, e que a instancia da
    # classe necromante utilize seu metodo 'reviver' corretamente
    if jogador1.vida <= 0 or jogador2.vida <= 0:
        if jogador1.vida <= 0 and jogador2.vida <= 0:
            setattr(jogador1, 'vida', 0)
            setattr(jogador2, 'vida', 0)
            if jogador1.classe == 'necromante' or jogador2.classe == 'necromante':
                visualizar()
                if jogador1.classe == 'necromante' and jogador2.classe == 'necromante':
                    jogador1.renascer()
                    jogador2.renascer()
                elif jogador1.classe == 'necromante':
                    jogador1.renascer()
                else:
                    jogador2.renascer()
        elif jogador1.vida <= 0:
            setattr(jogador1, 'vida', 0)
            if jogador1.classe == 'necromante':
                visualizar()
                jogador1.renascer()
        else:
            setattr(jogador2, 'vida', 0)
            if jogador2.classe == 'necromante':
                visualizar()
                jogador2.renascer()
        visualizar()
    else:
        visualizar()
    time.sleep(2)

# aqui é onde definimos a menssagem de finalização, anunciando se houve ou vencedor ou se anbos perderam,
# para isso se utiliza a função escreva citada no começo
if jogador1.vida > 0:
    escreva(f"{jogador1.nome} venceu a batalha!")
elif jogador2.vida > 0:
    escreva(f"{jogador2.nome} venceu a batalha!")
else:
    escreva("Ambos os jogadores caíram em batalha!😕")


import time

def valida(cpf):
    return len(cpf) == 11

apelido = print('@gmail.com:')


class Usuario:

    def __init__(self, nome, apelido, senha, rg, cpf, telefone):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        self.email = f"{nome} + {apelido}"
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone


class Cliente(Usuario):
    def __init__(self, nome, rg, cpf, telefone, apelido, senha, endereco):
        super().__init__(nome, apelido, senha, rg, cpf, telefone)
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.apelido = apelido
        self.__senha = senha
        self.endereco = endereco


class Funcionario(Usuario):
    def __init__(self,  nome, apelido, senha, cargo, rg, cpf, telefone):
        super().__init__(nome, apelido, senha, rg, cpf, telefone)
        self.nome = nome
        self.apelido = apelido
        self.cargo = cargo
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone


class Produto:
    def __init__(self, id_produto, nome, preco, descricao, tipo, marca, categoria):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.tipo = tipo
        self.marca = marca
        self.categoria = categoria

    def exibir_detalhes(self):
        return f" Produto: {self.nome}, Preço: R${self.preco:.2f}"


class Pagamento:
    def __init__(self, id_forma_pagamento, id_cliente, valor, produto):
        self.id_cliente = id_cliente
        self.id_forma_pagamento = id_forma_pagamento
        self.valor = valor
        self.produto = produto


class Entrega:
    def __init__(self, id_entregador, nome_entregador, produto, endereco_entrega, numero_residencial):
        self.id_entregador = id_entregador
        self.nome = nome_entregador
        self.produto = produto
        self.endereco_entrega = endereco_entrega
        self.numero_residencial = numero_residencial


class Pedido:
    def __init__(self, lista=[]):
        self.produtos = lista
        self.valor_total = 0


def menu():
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Funcionário")
    print("3. Cadastrar Produto")
    print("4. Realizar Pagamento")
    print("5. Realizar Entrega")
    print("6. Sair")
    return input("Escolha uma opção: ")


if __name__ == '__main__':
    while True:
        opcao = menu()
        if opcao == '1':
            nome = input('Nome do Cliente:')
            rg = input('RG do Cliente:')
            cpf = input('CPF do Cliente:')
            telefone = input('Telefone do cliente:')
            apelido = input('Apelido do cliente:')
            senha__ = input('Senha do cliente:')
            endereco = input('Endereço do cliente:')

            if valida(cpf):
                cli = Cliente(nome, rg, cpf, telefone, apelido, endereco)


            else:
                print('CPF inválido.')

        elif opcao == '2':
            name = input('Digite nome do funcionário:')
            ape = input('Digite apelido:')
            id_func = input('Qual cargo do funcionário')
            Dt_Nasc = ('Digite seu nascimento')
            sen = ('Digite seu senha:')
            ema = input('Digite seu email ')


            #enh =  senha, rg, cpf, telefone))


            pass
        elif opcao == '3': #id_produto, nome, preco, descricao, tipo, marca, categoria)
            nom = input('Digite o nome do Produto :')
            valor = input('Digite o valor do produto: R$ ')
            print("Vericaremos se esse produto já está cadastrado:")
            tipo = input('Digite o tipo do produto:')
            marca = input('Digite o marca do produto:')
            categoria = input('Digite o categoria do produto:')


            time.sleep(5)
            print("Cadastrado com sucesso")


            # Código para cadastrar produto
            pass
        elif opcao == '4':
            # Código para realizar pagamento
            pass
        elif opcao == '5':
            input()
            pass
        elif opcao == '6':
            break
        else:
            print('Opção inválida.')
#sessao = none
#for usu in lista_func:
    #if(usu.username == usuario_informado and uso.senha == senha_informada)
    #sessao = usu
    #break


def valida(cpf):
    if len(cpf) == 11:
        return True
    else:
        return False


class Usuario:
    def __init__(self, nome, apelido, senha, rg, cpf, telefone):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        self.email = f"{nome} {apelido}"
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone


class Cliente(Usuario):
    def __init__(self, nome, rg, cpf, telefone, apelido, senha, endereco):
        super().__init__(nome, apelido, senha)
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.__senha = ()


class Funcionario(Usuario):
    def __init__(self, nome, apelido, senha, cargo):
        super().__init__(nome, apelido, senha)
        self.cargo = cargo
        self.__senha = ()


class Produto:
    def __init__(self, id_produto,nome, preco, descrição, tipo, marca, categoria):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.descricao = descrição
        self.tipo = tipo
        self.marca = marca
        self.categoria = categoria

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")


class Pagamento:
    def __init__(self, id_forma_pagamento, id_cliente, valor,  produto,):
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


if __name__ == '__main__':
    try:
        username = input('Qual seu nome de usuário, interagiremos atráves desse apelido:' )
        clie = Cliente(
            input('CPF do Cliente:'),
            username,
            input('Senha do cliente:'),
            input('Informe o endereço do cliente:')
        )

        func = Funcionario( input('Nome do funcionário:'),
            input('Apelido do funcionário:'),
            input('Senha do funcionário:'),
            input('Cargo do funcionário:')
        )

        prod = Produto(
            input('Nome do produto:'), float(input('Preço do produto: R$ '))
        )

        pag = Pagamento(clie,
            prod,
            input('Método de pagamento:'))

        entreg = Entrega(
            clie,
            prod,
            input('Endereço de entrega:'))

        ped = Pedido()

    except:
        print('Não foi possível cadastrar devido ao CPF inválido.')

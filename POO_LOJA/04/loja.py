def valida(cpf):
    if len(cpf) == 11:
        return True
    else:
        return False


class Usuario:
    def __init__(self, nome, apelido, senha):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        self.email = nome + apelido


class Cliente(Usuario):
    def __init__(self, nome, apelido, senha, endereco):
        super().__init__(nome, apelido, senha)
        self.endereco = endereco
        self.__senha = ()


username = input('Qual seu nome de usuário, interagiremos atráves desse apelido:' )


class Funcionario(Usuario):
    def __init__(self, nome, apelido, senha, cargo):
        super().__init__(nome, apelido, senha)
        self.cargo = cargo
        self.__senha = (print ('Defina sua senha:'))



class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")


class Pagamento:
    def __init__(self, cliente, produto, metodo_pagamento):
        self.cliente = cliente
        self.produto = produto
        self.metodo_pagamento = metodo_pagamento


class Entrega:
    def __init__(self, cliente, produto, endereco_entrega):
        self.cliente = cliente
        self.produto = produto
        self.endereco_entrega = endereco_entrega


print(Usuario)


class Pedido:
    def __init__(self, lista=[]):
        self.produtos = lista
        self.valor_total = 0


if __name__ == '__main__':
    try:

        clie = Cliente(
        input('CPF do Cliente:'),
        input('RG do cliente:'),
        input('Irforme o endereço do cliente:'),
    )

    except:
        print('Não Foi possivel cadastrar devido ao cpf inválido')











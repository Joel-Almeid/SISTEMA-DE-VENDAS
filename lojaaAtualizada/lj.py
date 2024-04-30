import time

def valida(cpf):
    return len(cpf) == 11

class Usuario:
    def __init__(self, nome, apelido, senha, rg, cpf, telefone):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        self.email = f"{nome}@{apelido}.com"
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso!")

class Cliente(Usuario):
    def __init__(self, nome, rg, cpf, telefone, apelido, senha, endereco):
        super().__init__(nome, apelido, senha, rg, cpf, telefone)
        self.endereco = endereco

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print("Endereço alterado com sucesso!")

class Funcionario(Usuario):
    def __init__(self,  nome, apelido, senha, cargo, rg, cpf, telefone):
        super().__init__(nome, apelido, senha, rg, cpf, telefone)
        self.cargo = cargo

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

class Pedido:
    def __init__(self):
        self.produtos = []
        self.valor_total = 0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.valor_total += produto.preco
        print(f"Produto {produto.nome} adicionado ao pedido. Valor total: R${self.valor_total:.2f}")

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
            senha = input('Senha do cliente:')
            endereco = input('Endereço do cliente:')

            if valida(cpf):
                cli = Cliente(nome, rg, cpf, telefone, apelido, senha, endereco)
            else:
                print('CPF inválido.')

        elif opcao == '2':
            nome = input('Digite nome do funcionário:')
            apelido = input('Digite apelido:')
            cargo = input('Qual cargo do funcionário')
            senha = input('Digite seu senha:')
            rg = input('Digite seu RG:')
            cpf = input('Digite seu CPF:')
            telefone = input('Digite seu telefone ')

            if valida(cpf):
                func = Funcionario(nome, apelido, senha, cargo, rg, cpf, telefone)
            else:
                print('CPF inválido.')

        elif opcao == '3':
            id_produto = input('Digite o ID do Produto :')
            nome = input('Digite o nome do Produto :')
            preco = float(input('Digite o valor do produto: R$ '))
            descricao = input('Digite a descrição do produto:')
            tipo = input('Digite o tipo do produto:')
            marca = input('Digite a marca do produto:')
            categoria = input('Digite a categoria do produto:')

            prod = Produto(id_produto, nome, preco, descricao, tipo, marca, categoria)
            print("Produto cadastrado com sucesso")

        elif opcao == '4':
            pass
        elif opcao == '5':
            pass
        elif opcao == '6':
            break

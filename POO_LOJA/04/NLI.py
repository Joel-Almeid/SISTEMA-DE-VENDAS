class Usuario:
    def __init__ (self, nome, apelido, senha):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        self.email = nome + apelido


class Cliente(Usuario):
    def __init__(self, nome, apelido, senha):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha

class Funcionario(Usuario):
    def __init__(self, nome, apelido, senha):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha


class pagamento:

    def __init__(self):
        self.carros_vendidos = []

    def adicionar_carro(self, carro):
        self.carros_vendidos.append(carro)

    def gerar_relatorio(self):
        print("Relatório de Vendas:")
        for carro in self.carros_vendidos:
            print(f"Modelo: {carro.modelo}, Marca: {carro.marca}, Placa: {carro.placa}, Quilometragem: {carro.quilometragem} km")

# Exemplo de uso
if __name__ == "__main__":
    concessionaria = Concessionaria()

    carro1 = Carro("Civic", "Honda", "ABC123", 50000)
    carro2 = Carro("Corolla", "Toyota", "XYZ789", 60000)

    concessionaria.adicionar_carro(carro1)
    concessionaria.adicionar_carro(carro2)

    concessionaria.gerar_relatorio()
er
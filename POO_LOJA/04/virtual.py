class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")


class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.marca = marca

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Marca: {self.marca}")


# Exemplo de uso
produto1 = Produto(nome="Camiseta", preco=39.99)
produto2 = ProdutoEletronico(nome="Smartphone", preco=899.99, marca="Samsung")

produto1.exibir_detalhes()
produto2.exibir_detalhes()

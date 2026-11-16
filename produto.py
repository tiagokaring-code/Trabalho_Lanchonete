class Produto:
    def __init__(self, nome, preco, descricao=""):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    @property
    def descricao(self):
        return self._descricao

    def exibir_info(self):
        return f"{self._nome} - R$ {self._preco:.2f}"

    def __str__(self):
        return self.exibir_info()
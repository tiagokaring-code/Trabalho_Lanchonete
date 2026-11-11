from Produto import Produto
class Bebida(Produto):
    def __init__(self,nome, valor, mls):
        super().__init__(nome,valor)
        self.mls = mls
    @property
    def mls(self) -> int:
        return self._mls

    @mls.setter
    def mls(self, valor: int):
        if valor <= 0:
            raise ValueError("O volume deve ser maior que 0")
        self._mls = valor

    def servir_com_gelo(self) -> str:
        return f"{self.nome} servido com gelo e limao!"

    def calcular_valor_final(self) -> float:
        return self.valor * 1.05

    def __str__(self) -> str:
        return f"[Bebida] {self._nome} ({self._mililitros}ml) - R$ {self.calcular_preco_final():.2f}"

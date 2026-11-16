from produto import Produto

class bebida(Produto):
    def __init__(self,nome: str, valor: float, mls: int):
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
        return self.preco * 1.05

    def __str__(self) -> str:
        return f"[Bebida] {self.nome} ({self._mls}ml) - R$ {self.calcular_valor_final():.2f}"
from produto import produto
class bebida(produto):
    def __init__(self,nome: str, valor: float, mls: int):
        super().__init__(nome,valor)
        self.mls = mls
    @property
    def mls(self) -> int:
        return self._mls

    @mls.setter
    def mls(self, valor: int):
        if valor <= 0:
            raise valueError("O volume deve ser maior que 0")
        self._mls = valor

    def servir_com_gelo(self) -> str:

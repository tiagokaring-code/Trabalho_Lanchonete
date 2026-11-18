from Produto import Produto
class Lanche(Produto):
    def __init__(self, nome, valor, ingredientes):
        super().__init__(nome,valor)
        self._ingredientes = ingredientes

    @property
    def ingredientes(self) -> list:
        return self._ingredientes

    def adicionar_ingredientes_extra(self, ingredientes: str):
        self._ingredientes.append(ingredientes)
        self.valor += 2.0 #valor do extra

    def calcular_valor_final(self) -> float:
        return self.valor + 1.50 #taxa do preparador do lanche

    def __str__(self) -> str:
        ingredientes_str = ",".join(self.ingredientes)
        return f"[lanche] {self.nome} ({ingredientes_str}) - R$ {self.calcular_valor_final():.2f}"
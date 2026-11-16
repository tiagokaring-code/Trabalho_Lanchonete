from produto import Produto
class lanche(Produto):
    def __init__(self,nome:str,valor:float,ingredientes:list):
        super().__init__(nome,valor)
        self._ingredientes = ingredientes

    @property
    def ingredientes(self) -> list:
        return self._ingredientes

    def adicionar_ingredientes_extra(self, ingredientes: str):
        self._ingredientes.append(ingredientes)
        self.preco += 2.0

    def calcular_valor_final(self) -> float:
        return self.preco + 1.50
    def __str__(self) -> str:
        ingredientes_str = ",".join(self.ingredientes)
        return f"[lanche] {self.nome} ({ingredientes_str}) - R$ {self.calcular_valor_final():.2f}"
from produto import Produto


class Sobremesa(Produto):

  def __init__(
      self, nome: str, preco: float, tamanho: str = "Médio", descricao: str = ""
  ):
    super().__init__(nome, preco, descricao)
    self.tamanho = tamanho

  @property
  def tamanho(self) -> str:
    return self._tamanho
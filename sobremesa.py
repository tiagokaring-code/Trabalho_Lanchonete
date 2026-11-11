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

  @tamanho.setter
  def tamanho(self, valor: str):
    if not valor or not isinstance(valor, str):
      raise ValueError("O tamanho deve ser um texto válido.")
    self._tamanho = valor

  def __str__(self) -> str:
    return f"[Sobremesa] {self.nome} ({self.tamanho}) - R$ {self.preco:.2f}"

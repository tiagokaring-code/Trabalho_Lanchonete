from produto import Produto


class Lanchonete:

  def __init__(self, nome: str):
    self.nome = nome
    self._cardapio: list[Produto] = []

  @property
  def cardapio(self) -> list[Produto]:
    return self._cardapio

  def adicionar_produto(self, produto: Produto) -> None:
    if isinstance(produto, Produto):
      self._cardapio.append(produto)
      print(f"Produto '{produto.nome}' adicionado com sucesso.")
    else:
      raise TypeError("O item deve ser uma instância de Produto.")
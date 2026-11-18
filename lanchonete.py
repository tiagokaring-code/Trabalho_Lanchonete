
from produto import Produto


class Lanchonete:
    """Gerencia os produtos e o cardápio da lanchonete."""

    def __init__(self, nome: str):
        """Inicializa a lanchonete e seu cardápio."""
        self.nome = nome
        self._cardapio: list[Produto] = []

    @property
    def cardapio(self) -> list[Produto]:
        """Retorna os produtos cadastrados."""
        return self._cardapio

    def adicionar_produto(self, produto: Produto) -> None:
        """Adiciona um produto ao cardápio."""
        if isinstance(produto, Produto):
            self._cardapio.append(produto)
            print(f"Produto '{produto.nome}' adicionado com sucesso.")
        else:
            raise TypeError("O item deve ser uma instância de Produto.")

    def remover_produto(self, nome: str) -> bool:
        """Remove um produto pelo nome."""
        for item in self._cardapio:
            if item.nome.lower() == nome.lower():
                self._cardapio.remove(item)
                print(f"Produto '{nome}' removido do cardápio.")
                return True

        print(f"Produto '{nome}' não encontrado no cardápio.")
        return False

    def buscar_produto(self, nome: str) -> Produto | None:
        """Busca um produto pelo nome."""
        for item in self._cardapio:
            if item.nome.lower() == nome.lower():
                return item

        return None

    def listar_cardapio(self) -> None:
        """Exibe todos os produtos cadastrados."""
        if not self._cardapio:
            print("\nO cardápio está vazio.")
            return

        print(f"\n========== CARDÁPIO: {self.nome.upper()} ==========")

        for idx, item in enumerate(self._cardapio, start=1):
            print(f"{idx}. {item}")

        print("==============================================")

    def calcular_valor_total_cardapio(self) -> float:
        """Calcula a soma dos preços dos produtos."""
        return sum(item.preco for item in self._cardapio)

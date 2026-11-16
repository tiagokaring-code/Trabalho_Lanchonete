from produto import Produto
from lanche import lanche
from bebida import bebida
from lanchonete import Lanchonete


def exibir_menu():
    """Exibe as opções disponíveis no sistema."""
    print("\n========== LANCHONETE DELIVERY ==========")
    print("1 - Cadastrar produto")
    print("2 - Listar cardápio")
    print("3 - Buscar produto")
    print("4 - Executar ação polimórfica")
    print("5 - Remover produto")
    print("6 - Sair")
    print("=========================================")


def cadastrar_produto(lanchonete):
    """Permite cadastrar um novo produto no cardápio."""
    print("\n--- CADASTRAR PRODUTO ---")
    print("1 - Lanche")
    print("2 - Bebida")

    opcao = input("Escolha o tipo de produto: ")

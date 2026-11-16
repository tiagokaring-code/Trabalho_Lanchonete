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

    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))

        if opcao == "1":
            ingredientes = input("Ingredientes (separados por vírgula): ")
            lista_ingredientes = [
                item.strip() for item in ingredientes.split(",")
            ]

            produto = lanche(nome, preco, lista_ingredientes)

        elif opcao == "2":
            mls = int(input("Volume em ml: "))
            produto = bebida(nome, preco, mls)

        else:
            print("Opção inválida.")
            return

        lanchonete.adicionar_produto(produto)

    except ValueError as erro:
        print(f"Erro ao cadastrar: {erro}")


def listar_produtos(lanchonete):
    """Exibe todos os produtos cadastrados."""
    lanchonete.listar_cardapio()


def buscar_produto(lanchonete):
    """Busca um produto pelo nome."""
    nome = input("Digite o nome do produto: ")

    produto = lanchonete.buscar_produto(nome)

    if produto:
        print("\nProduto encontrado:")
        print(produto)
    else:
        print("Produto não encontrado.")


def executar_polimorfismo(lanchonete):
    """Executa o método sobrescrito de cada tipo de produto."""
    if not lanchonete.cardapio:
        print("Não existem produtos cadastrados.")
        return

    print("\n--- AÇÕES DOS PRODUTOS ---")

    for produto in lanchonete.cardapio:
        print(produto)
        print(f"Valor final: R$ {produto.calcular_valor_final():.2f}")
        print("--------------------------------")


def remover_produto(lanchonete):
    """Remove um produto do cardápio."""
    nome = input("Digite o nome do produto que deseja remover: ")
    lanchonete.remover_produto(nome)


def main():
    """Executa o sistema principal da lanchonete."""
    lanchonete = Lanchonete("Nexus Lanches")

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(lanchonete)

        elif opcao == "2":
            listar_produtos(lanchonete)

        elif opcao == "3":
            buscar_produto(lanchonete)

        elif opcao == "4":
            executar_polimorfismo(lanchonete)

        elif opcao == "5":
            remover_produto(lanchonete)

        elif opcao == "6":
            print("Obrigado por utilizar o sistema!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
from modelos import Produto, listar_produtos

def exibir_menu():
    print (f"""\n
    ====== MENU DE PRODUTOS ======
    
    0 - Sair
    1 - Cadastrar produto
    2 - Listar produto

    =================================
    """)

def cadastrar():
    nome = input("Digite o nome: ")
    preco = float(input("Digite o preço:"))
    categoria = input("Digite a categoria: ")

    produto = Produto(nome, preco, categoria)
    produto.salvar()

def mostrar():
    for produto in listar_produtos():
        produto.exibir()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        mostrar()
    else:
        print("Opção inválida! Tente novamente.")
from modelos import Aluno, listar_aluno

def exibir_menu():
    print (f"""\n
    ====== ESCOLHA UMA OPÇÃO ======
    
    0 - Sair
    1 - Cadastrar aluno
    2 - Listar aluno

    =================================
    """)

def cadastrar():
    nome = input("Digite o nome: ")
    media = float(input("Digite a média: "))
    aluno = Aluno(nome, media)
    aluno.salvar()

def mostrar():
    for aluno in listar_aluno():
        aluno.exibir()

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
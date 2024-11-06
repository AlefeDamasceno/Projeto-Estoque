def menu():
    print("""
MENU DE OPÇÕES:
[ 1 ] Adicionar novo produto
[ 2 ] Remover produto
[ 3 ] Atualizar Quant. do produto
[ 4 ] Todos produtos
[ 5 ] Sair""")

def verific_entrada():
    global opc_usuario
    while True:
        menu()
        opc_usuario = int(input("Opção: "))
        if opc_usuario not in (1, 2, 3, 4, 5):
            print("Entrada Inválida.. Tente Novamente")
        else:
            opcao()
 
def opcao():
    if opc_usuario == 1:
        print("Você escolheu 'Adicionar novo produto'")
        adicionar_prod()
    elif opc_usuario == 2:
        print("Você escolheu 'Remover produto'")
    elif opc_usuario == 3:
        print("Você escolheu 'Atualizar Quant. de produtos'")
    elif opc_usuario == 4:
        print("Você escolheu 'Todos produtos'")
    elif opc_usuario == 5:
        print("Obrigado por usar o programa!")
        exit()

def verificar_prod_quant(produto, quant):
    global produto_ok 
    produto_tratado = produto.replace(" ", "")
    
    if produto_tratado.isalpha():
        try:
            quant_int = int(quant)
            produto_ok = True
        except ValueError:
            print("Quantidade inválida! Deve ser um número.")
            produto_ok = False
    else:
        print("Entrada inválida! O nome do produto deve conter apenas letras.")
        produto_ok = False
        
def adicionar_prod():
    while True:
        produto = input("Nome do produto: ")
        quant = input("Quant. produto: ")
        
        verificar_prod_quant(produto, quant)
        
        if produto_ok: 
            for verific in estoque:
                if verific == produto:
                    print(f"O Produto {produto} já está em Estoque!")
                    break
            else:
                estoque[produto] = int(quant)
                print(f"Produto {produto} adicionado!")
            break 

estoque = {"banana": 14, "tomate": 124}

verific_entrada()
print(estoque)

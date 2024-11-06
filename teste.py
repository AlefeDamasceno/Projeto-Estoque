def verificar_prod_quant(produto,quant):
    produto_sem_espaco = produto.replace(" ", "")
    if produto_sem_espaco.isalpha():
        print("Só caracter")
    else:
        print("Entrada Invalida!")
    
    
    
verificar_prod_quant(" ale fe 14", 14)
    
    
    

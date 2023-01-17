def condicionais():
    x = input("Digite o valor de x:")
    y = input("Digite o valor de y:")
    
    if x < y:
        print("x é menor que y")
    elif x == y:
        print("são iguais")
    else:
        print("x não é menor que y")
        
if __name__ == '__main__':
    condicionais()
def main():
    print ("FUNDAMENTOS BÁSICOS PYTHON\n")
    print("Hello World!")
    
    ''' VARIÁVEIS '''
    print("\nVariáveis")
    f = 0
    print(f"f: {f}, {type(f)}")
    print("\nMudando o tipo da variável")
    f = "abc"
    print(f"f: {f}, {type(f)}",)
    
    # Gerando erro de tipos:
    # print("Isto é uma string" + 123) - resolução: cast str(123)
    print("Isto é uma string" + str(123))
    
if __name__ == "__main__":
    main()
def funcDois():
    f = "def"
    return f

def funcTres():
    global f
    f = "ghi"
    return f

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

''' FUNÇÕES '''
print("\nFunções")
# Comparar valores entre duas variáveis em escopos diferentes
print(f"f na func2 (LOCAL): '{funcDois()}', f na main (GLOBAL): '{f}'")
# chamando func com f de escopo global
print(f"f na func2 (LOCAL): '{funcDois()}', f na func3 (GLOBAL): '{funcTres()}', f na main (GLOBAL): '{f}'")
    
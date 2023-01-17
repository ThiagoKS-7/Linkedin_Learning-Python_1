'''
Procedimento/Subrotina: Parte de um programa ou classe que roda instruções mas não retorna um valor;
Função: Parte de um programa ou classe que roda instruções e retorna um valor;
Método: Procedimento ou função pertencente a uma classe.
'''
# Subrotina
def func1():
    print("sou a func1")
    
# Subrotina com parametros
def func2(arg1, arg2):
    print(arg1 + " " +  arg2)
    
# funcão com parametros
def potencia(base, expoente):
    return base**expoente
    
#  Subrotina com parametros
def tabuada(base):
    res = 0
    for i in range(1, 10 +1):
        res = base*i
        print(f"{base} * {i} = {res}")
    
if __name__ == "__main__":
    func1()
    func2("Thiago", "Kasper")
    print(potencia(2,3))
    tabuada(2)
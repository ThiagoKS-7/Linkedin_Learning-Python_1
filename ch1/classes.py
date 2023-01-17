class MinhaClasse():
    def __init__(self):
        self.meu_atributo = "Passou pelo construtor"
    
    def meu_metodo(self):
        print("Passou por meu_metodo")
    
    def metodo_dois(self, valor):
        self.outro_atributo = valor
        print(f"passou por meu metodo 2  - {self.outro_atributo}")
        
        
def cria_obj():
    meu_obj = MinhaClasse()
    var1 = meu_obj.meu_atributo
    meu_obj.meu_metodo()
    meu_obj.metodo_dois("testando metodo2")
    print(var1)

if __name__ == '__main__':	
    cria_obj()    
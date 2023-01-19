
def cria_arquivo():
    arquivo = open("novo_arquivo.txt", "w+")
    arquivo.write("Linha gerada com cria_arquivo\r\n")
    arquivo.close()
    
def escrever_no(name=str, value=str):
    arquivo = open(name, "a")
    arquivo.write(value + "\r\n")
    arquivo.close()

def main():
    cria_arquivo()
    escrever_no("novo_arquivo.txt", "teste")

if __name__ == '__main__':
    main()
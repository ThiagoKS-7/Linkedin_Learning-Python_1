def leitura_arquivo(name=str):
    f = open(name, "r")
    if f.mode == 'r':
        print(f.read())
    f.close()
    

def leitura_arquivo_grande(name=str):
    f = open(name, "r")
    if f.mode == 'r':
       for line in f.readlines():
           print(line)
    
def main():
    leitura_arquivo("novo_arquivo.txt")
    leitura_arquivo_grande("novo_arquivo.txt")

if __name__ == '__main__':
    main()
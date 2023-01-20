
from os import path
import time

def dados_arquivo(value=str):
    return {
        'existe': path.exists(value),
        'eh_dir': path.isdir(value),
        'path_real':  path.realpath(value),
        'path_relativo':  path.relpath(value),
        'dt_criacao':  time.ctime(path.getctime(value)),
        'dt_modificacao':   time.ctime(path.getmtime(value))
    }
    

def mostra_dados(res):
    for key in res:
        print(f"{key}->{res[key]}")

def main():
    mostra_dados(dados_arquivo("novo_arquivo.txt"))


if __name__ == '__main__':
    main()
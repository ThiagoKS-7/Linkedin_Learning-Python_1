from os import path,rename, remove
import shutil
from shutil import make_archive
from zipfile import ZipFile

def copia_arquivo(value=str):
    if path.exists(value):
        path_atual = path.realpath(value)
        novo_path = path_atual + ".bkp"
        shutil.copy(path_atual, novo_path)
        shutil.copystat(path_atual, novo_path)

def renomear_arquivo(value=str, new_name=str):
    if path.exists(value):
        rename(value, new_name)

def cria_zip(value=str, format=str, path=str):
    shutil.make_archive(value,format, path)
    
def cria_zip_2(value=str, files=str):
    with ZipFile(value, "w") as novo_zip:
        for file in files:
            novo_zip.write(file)
    novo_zip.close()

def excluir_arquivo(value=str):
    remove(value)

def main():
    copia_arquivo("novo_arquivo.txt")
    renomear_arquivo("novo_arquivo.txt.bkp", "backup.bkp")
    cria_zip("arq_zip", "zip", "/home/thiago/Linux/python/linkedin-learning/lkdPythonI/ch2")
    cria_zip_2("arq_zip2.zip", ["backup.bkp", "arq_zip.zip", "novo_arquivo.txt"])
    excluir_arquivo("backup.bkp")
    

if __name__ == '__main__':
    main()
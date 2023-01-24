
import sqlite3

# Suporta Insert e update
def manipula_dados(banco=str, cmd=str) -> None:
    con = sqlite3.connect(banco)
    cursor = con.cursor()
    cursor.execute(cmd)
    con.commit()
    print("Comando realizado com sucesso!")
    con.close()


def seleciona_dados(banco=str, cmd=str) -> list:
    con = sqlite3.connect(banco)
    cursor = con.cursor()
    cursor.execute(cmd)
    linhas = cursor.fetchall()
    cursor.close()
    res = []
    for l in linhas:
        res.append(l)
        print(l)
    return l


def insert_estado(nome=str,sigla=str, capital=str) -> str:
    return f"INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('{nome}', '{sigla}', '{capital}')"


def lista_estados() -> str:
    return "SELECT nome_estado, sigla_estado, nome_capital FROM estados"
    
def main():
    banco = "/home/thiago/Linux/python/linkedin-learning/lkdPythonI/ch5/BancoDeDados.db"
    manipula_dados(banco, insert_estado('TESTE2', 'YY', 'Teste inclusao2'))
    seleciona_dados(banco, lista_estados())

if __name__ == '__main__':
    main()
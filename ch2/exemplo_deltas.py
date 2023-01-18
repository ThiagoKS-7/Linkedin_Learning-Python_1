'''
Criar um codigo para comparar a diferença entre duas datas
'''

from datetime import date, time, datetime, timedelta


def checa_tipo_data(value, res):
    if (type(value) is date):
        print(f"{res}\n")
    else:
        print("Formato inválido. Aceita só datetime.date")
        
        
def string_para_datetime(dtm):
    d1 = dtm.split(" ")[0].split("-")
    t1 = dtm.split(" ")[1].split(":")
    return datetime(year=int(d1[0]), 
                   month=int(d1[1]), 
                   day=int(d1[2]),
                   hour=int(t1[0]), 
                   minute=int(t1[1]), 
                   second=int(t1[2]))


def comparar_duas():
    td1 = input("Digite uma primeira data (formato yyyy-mm-dd hh:mm:ss): ")
    nd1 = string_para_datetime(td1)
    td2 = input("Agora, digite outra (formato yyyy-mm-dd hh:mm:ss): ")
    nd2 = string_para_datetime(td2)
    print(f"A diferença é de {str(abs(nd2-nd1)).replace('days', 'dias')} horas." )
    

def comparar_com_hj():
    td1 = input("Digite uma data (formato yyyy-mm-dd hh:mm:ss): ")
    nd1 = string_para_datetime(td1)
    print(f"A diferença é de {str(abs(nd1-datetime.now())).replace('days', 'dias')} horas." )

def checa_comparacao():
    q = ""
    while q != 'y' and q != 'n':
        q = input("Deseja comparar com data corrente? (y/n): ")  
        if q == "y":
            comparar_com_hj()
        elif q == 'n':
            comparar_duas()

#2022-10-31 07:08:30    
#2021-09-10 10:30:50 
def main():
    checa_comparacao()

 
if __name__ == '__main__':
    main()
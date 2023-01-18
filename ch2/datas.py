from datetime import date, time, datetime

def checa_tipo_data(value, res):
    if (type(value) is date):
        print(f"{res}\n")
    else:
        print("Formato inválido. Aceita só datetime.date")
    
def mostra_partes_data(value):
    checa_tipo_data(value, f"dia: {value.day}, mês: {value.month}, ano: {value.year}")
    
def mostra_dia_semana(value):
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    num= f"Número dia semana: {value.weekday()}\n"
    nome = f"Nome do dia da semana: {dias[value.weekday()]}"
    res = num+nome
    checa_tipo_data(value, res)

def manipula_data_e_hora():
    hj = date.today()
    print(f"Hoje é: {hj} - {type(hj)}")
    mostra_partes_data(hj)
    mostra_dia_semana(hj)
    print("Data e hora de hj: " + str(datetime.now()))
    print(f"Hora de hj: {datetime.now().time()}")
    
    

if __name__ == '__main__':
    manipula_data_e_hora()
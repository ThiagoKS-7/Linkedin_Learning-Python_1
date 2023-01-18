from datetime import date, time, datetime

def checa_tipo_data(value, res):
    if (type(value) is date):
        print(f"{res}\n")
    else:
        print("Formato inválido. Aceita só datetime.date")

def mostra_data_formatada(value):
    checa_tipo_data(value, f"data formatada dd/mm/yyyy: {value.strftime('%d/%m/%Y')}") 
    
def mostra_hora_formatada(value):
    checa_tipo_data(value,"Hora de hj formatada (BR): " + str(datetime.now().strftime('%H:%M:%S')))
    checa_tipo_data(value,"Hora dcom meridiano: " + str(datetime.now().strftime('%H:%M:%S %p')))
    
def mostra_data_hora_formatada(value):
    checa_tipo_data(value,"Data e hora de hj formatada: " + str(datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
    
def mostra_data_hora_local(value):
    checa_tipo_data(value,str(datetime.now().strftime('%c')))
    

def manipula_formatos():
    hj = date.today()
    mostra_data_formatada(hj) 
    mostra_hora_formatada(hj)
    mostra_data_hora_formatada(hj)
    mostra_data_hora_local(hj)

if __name__ == '__main__':
    manipula_formatos()
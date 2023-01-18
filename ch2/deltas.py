from datetime import date, time, datetime, timedelta

def checa_tipo_data(value, res):
    if (type(value) is date):
        print(f"{res}\n")
    else:
        print("Formato inválido. Aceita só datetime.date")

def delta_tempo():
    delta = timedelta(days=86, hours=8532, minutes=7645)
    print(f"Delta: {delta} ")
    hj = datetime.now() 
    print(f"No futuro: {(hj + delta).strftime('%d/%m/%Y %H:%M:%S')}")      
    print(f"No passado: {(hj - delta).strftime('%d/%m/%Y %H:%M:%S')}")    
        
def main():
    delta_tempo()

if __name__ == "__main__":
    main()
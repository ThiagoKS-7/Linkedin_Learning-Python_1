from datetime import date, time, datetime

def checa_tipo_data(value, res):
    if (type(value) is date):
        print(f"{res}\n")
    else:
        print("Formato inválido. Aceita só datetime.date")
        
        
def main():
    pass

if __name__ == "__main__":
    main()
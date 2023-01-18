import calendar

def imprime_mes_e_dia():
    for mes in calendar.month_name:
        print (mes)
    for dia in calendar.day_name:
        print (dia)
        

def main():
    imprime_mes_e_dia()
    
if __name__ == '__main__':	
    main()
import calendar
import webbrowser 

def calendario_texto():
    cld = calendar.TextCalendar(calendar.SUNDAY)
    return cld.formatmonth(2023,1)

def calendario_html():
    cld = calendar.HTMLCalendar(calendar.SUNDAY)
    html_cld = cld.formatmonth(2023,1)
    with open("calendario.html", "w") as f:
        f.write(html_cld)
    f.close()
    webbrowser.open('calendario.html')  

def main():
    print(calendario_texto())
    calendario_html()

if __name__ == '__main__':
    main()
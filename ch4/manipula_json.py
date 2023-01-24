import urllib.request
import json
import webbrowser

def manipula_json(link=str) -> dict:
    web_url = urllib.request.urlopen(link)
    if web_url.getcode() == 200:
        return json.loads(web_url.read())
        
def monta_relatorio(res) ->None:
    with open("relatorio.html", "w+") as f:
        f.write("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD' crossorigin='anonymous'><title>RELATÓRIO</title></head><body style='background:#212529; color:white; '><h3>Locais com magnetude maior que 2.5: </h3><ul>")
        for local in res["features"]:
           f.write(f"<li>{local['properties']['place']}</li>")
        f.write(f"</ul><h4>Total: {res['metadata']['count']} lugares.</h4>")
        f.write("</body><script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js' integrity='sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN' crossorigin='anonymous'></script></html>")
        f.close()
        webbrowser.open('relatorio.html')  

def main():
    res = manipula_json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    monta_relatorio(res)
if __name__ == '__main__':
    main()
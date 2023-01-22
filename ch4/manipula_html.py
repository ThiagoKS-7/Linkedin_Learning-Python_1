from html.parser import HTMLParser
from datetime import datetime

class myParser(HTMLParser):
    def write_response(self, response):
        with open("response.txt", "a+") as f: 
            f.write(response)
        f.close()
        
    def handle_starttag(self, tag, attrs):
        if tag == "title":
            hj = datetime.now()
            self.write_response(f"{hj.strftime('%c')}\n")
        if tag=="img" and attrs.__len__() > 1:
           self.write_response(f"{tag}-{attrs[1][1]} => {attrs[0][1]}\n")
        elif tag=="img" and attrs.__len__() > 0:
            self.write_response(f"{tag}-N/A => {attrs[0][1]}\n")
        
    def handle_comment(self,data):
        print(f"comentario: {data}")

    def handle_endtag(self, tag: str):
        if tag == "html": 
            self.write_response("\n")
            print("[INFO] - Dados salvos em response.txt!")
        
    def handle_data(self, data):
        return
                  


def main():
    mp = myParser()
    arquivo = open("exemplo.html", "r")
    dados = arquivo.read()
    mp.feed(dados)
    arquivo.close()
        
if __name__ == "__main__":
    main()
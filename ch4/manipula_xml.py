import xml.dom.minidom
import xml.etree.ElementTree as et

def manipula_xml(value=str) -> None:
    doc = xml.dom.minidom.parse(value)
    tree = et.parse(value)

    first_name = doc.getElementsByTagNameNS('*','firstname')[0].firstChild.nodeValue
    last_name = doc.getElementsByTagNameNS('*','lastname')[0].firstChild.nodeValue
    print(f"Primeira tag {tree.getroot()[0]}  - {tree.getroot()[0].text}")
    print("\nDADOS:")
    print(f"Nome: {str(first_name)} {str(last_name)}")
    print("\nSKILLS:")
    for s in doc.getElementsByTagNameNS('*','skill'):
        print(f"- {s.getAttribute('name')}")

def main():
    manipula_xml("/home/thiago/Linux/python/linkedin-learning/lkdPythonI/examplo.xml")

if __name__ == '__main__':
    main()
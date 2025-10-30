import json
import re
import time
import urllib.request
from random import randint

from database import inserttoDatabase
from datetime import datetime, timedelta


def segundaCrawler(): # esto es para ir probando sin tener que ir al sitio a cada rato.
    with open('lasegunda.json', 'r') as file:
        data = json.load(file)
    #print (data)
    for hits in data['hits']['hits']:

        print (hits['_source']['titulo'])
        texto = cleanhtml(hits['_source']['texto'])
        print(texto)

        print(hits['_source']['permalink'])
        print(hits['_source']['fechaModificacion'])
        #inserttoDatabase()


def segunda_Crawler():
    now = datetime.now() + timedelta(days=1)
    fechaFin = now.strftime("%Y-%m-%d") # le agrego un dia más para que el sitio me devuelva los datos del dia en curso
    link = f"https://newsapi.ecn.cl/NewsApi/emol/buscador/lasegunda?q=&size=50&from=0&fechaPublicacion={fechaFin}"
    req = urllib.request.Request(
        link,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    with urllib.request.urlopen(req) as url:
        data = json.load(url)

        for hits in data['hits']['hits']:
             try:
                 titulo= hits['_source']['titulo']
                 texto= cleanhtml(hits['_source']['texto'])
                 link= hits['_source']['permalink']
                 fechaModificacion= hits['_source']['fechaModificacion']
                 #print (titulo, texto, link, fechaModificacion, sep="\r")
                 inserttoDatabase(titulo, texto, link, fechaModificacion, id_diario=5640, fotourl='')

             except Exception as error:
                print(error)

    return True


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def tiempo_espera():
    espera = randint(300, 600)
    return espera

## Enlace
## https://newsapi.ecn.cl/NewsApi/emol/buscador/lasegunda?q=&size=40&from=0&fechaPublicacion=2026-01-01


# Parse the JSON string into a Python dictionary
#python_dict = json.loads(json_string)

#print(python_dict)
#print(type(python_dict))
#print(python_dict["hits"])

if __name__ == '__main__':
    while True:
        tiempo = tiempo_espera()
        print("Descargando\n")
        print("=" * 15)
        segunda_Crawler()
        time.sleep(tiempo)
    #segundaCrawler()



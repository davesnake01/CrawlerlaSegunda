import json
import re
import urllib
from database import inserttoDatabase


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
        #inserttoDatabase( )


def segunda_Crawler():

    link = f"https://newsapi.ecn.cl/NewsApi/emol/buscador/lasegunda?q=&size=50&from=0&fechaPublicacion=2025-10-25"
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
                 print(hits['_source']['id'])
                 print(hits['_source']['titulo'])
                 print(hits['_source']['texto'])
                 print(hits['_source']['permalink'])
                 print(hits['_source']['fechaModificacion'])


             except Exception as error:
                print(error)

    return True


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


## Enlace
## https://newsapi.ecn.cl/NewsApi/emol/buscador/lasegunda?q=&size=40&from=0&fechaPublicacion=2026-01-01


# Parse the JSON string into a Python dictionary
#python_dict = json.loads(json_string)

#print(python_dict)
#print(type(python_dict))
#print(python_dict["hits"])

if __name__ == '__main__':
    segundaCrawler()
    #segunda_Crawler()
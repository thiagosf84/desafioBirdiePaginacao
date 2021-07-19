import json
from bs4 import BeautifulSoup
import pandas as pd
import requests
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0", 
           "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9, image/webp,*/*;q=0.8"}
import numpy as np
#url da apido Extra conseguida após consultar a seção de Internet na 
inspeção da página.
url = 'https://www.extra.com.br/api/catalogo-ssr/products/?Filtro=c1_c2&PaginaAtual=2&RegistrosPorPagina=20&Platform=2'

#produtos

#paginação para obter o máximo de produtos
for x in range(50):
    links = f'https://www.extra.com.br/api/catalogo-ssr/products/?Filtro=c1_c2&PaginaAtual={x}&RegistrosPorPagina=20&Platform=2'
    res = requests.get(links, headers =headers)
    res = json.loads(res.content)
    for i in res['products']:
        print("Produto: ",i ['name'])
        print("URL : ",i ['urls'])
        print("SKU :", i['urls'][-8:])
        print('-'*110)
        
#avaliações


#url onde ficam os comentários dos produtos. Foi usado somente um 
produto para teste
url = 'https://pdp-api.extra.com.br/api/v2/reviews/product/21689640/source/EX?page=1&size=3&orderBy=DATE'
for x in range(10):
    links = f'https://pdp-api.extra.com.br/api/v2/reviews/product/21689640/source/EX?page={x}&size=10&orderBy=DATE'
    res = requests.get(links, headers =headers)
    res = json.loads(res.content.decode('utf-8'))
    for avaliacao in res['review']['userReviews']:
     
        print("Nota: ",avaliacao['rating'])
        print("Nome do Cliente: ",avaliacao['name'])
        print("Avaliação: ",avaliacao['text'])
        print("-"*110)

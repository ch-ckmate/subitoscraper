from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os
import csv
ricerca='cassetti ufficio'
prezzo=50



appdata=os.getenv('LOCALAPPDATA')
appdata=appdata+'\\Temp\\'
inizio='https://www.subito.it/annunci-lombardia/vendita/usato/?q='+ricerca
url=['https://www.subito.it/annunci-lombardia/vendita/usato/?q='+ricerca]
listavecchia=[]
try:
    with open(appdata+'subitohistory.csv') as file:
        hyst=pd.read_csv(appdata+'subitohistory.csv')  
    for l in hyst['0']:
        listavecchia.append(l)
except:
    pass
    
    
page = requests.get(inizio)
soup = BeautifulSoup(page.text)
paginafinale=soup.find_all('button')
for pag in paginafinale:
    for l in pag.find_all('span'):
        lastapag=l.getText()[-1]
lastapag=int(lastapag)
for i in range(2,lastapag+1):
    url.append(inizio+"&o="+str(i))
pagine=[]
for u in url:
    page=requests.get(u)
    pagine.append(BeautifulSoup(page.text))
totaleitem=[]
for i in range(len(pagine)):
    totaleitem.append(pagine[i].find_all(class_='items__item'))
import itertools
tota = list(itertools.chain(*totaleitem)) 
totconprize=[]
for tot in tota:
    if '€' in str(tot):
        totconprize.append(tot)
url=[]
price=[]
data=[]
for i in totconprize:
    for a in i.findAll('a'):
        #for span in a.findAll('span'):
            #if 'date' in str(span):
                #data.append(span.getText())
        for p in a.findAll('p'):
    
            if 'price' in str(p):
                url.append(a['href'])
                price.append(re.sub("[^0-9]", "",p.getText().replace('\xa0','')))
                
df = pd.DataFrame({'Url':url,'Prezzo':price})
df['Prezzo']=pd.to_numeric(df['Prezzo'])
df=df[df['Prezzo']<prezzo]
def make_clickable(val):
    return '<a href="{}">{}</a>'.format(val,val)
nuovi=[]

listaatt=[]
for i in df['Url']:
    listaatt.append(i)

for rec in listaatt:
    if rec in listavecchia:
        pass
    else:
        nuovi.append(rec)
nuovi=pd.DataFrame(nuovi)
nuovi.to_csv(appdata+'subitohistory.csv', mode='a',index=False)
nuovi.style.format({'Url':make_clickable})
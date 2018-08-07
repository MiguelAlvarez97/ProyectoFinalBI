#-*- coding: utf-8 -*-
import couchdb
import sys
import urllib2
import re
import json
import matplotlib.pyplot as plt
from textblob import TextBlob
import unicodedata
from couchdb import view
from googletrans import Translator

def dibujar(arreglo):
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Positivos', 'Negativos', 'Neutros'
    sizes = arreglo
    colors = ['yellowgreen', 'gold', 'lightskyblue']
    explode = (0, 0, 0)  # explode a slice if required

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True)

    # draw a circle at the center of pie to make it look like a donut
    centre_circle = plt.Circle((0, 0), 0.75, color='black', fc='white', linewidth=1.25)
    fig = plt.gcf()
    fig.suptitle('PORTUGAL SAB 30 JUN', fontsize=12)
    fig.gca().add_artist(centre_circle)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()

def filtrarDatos(text):
    #s = unicode(text, "utf-8")
    emoji_pattern = emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2) 
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
        "+", flags=re.UNICODE)
    texto = (emoji_pattern.sub(r'', text.strip()))  # no emoji
    #print texto
    translator = Translator()
    try:
        textoTraducido = translator.translate(str(texto))
        #print textoTraducido.text
        num = re.sub(r'[^a-zA-Z 0-9.]+', "", textoTraducido.text)
        #print num
        return num
    except:
        pass




URL = 'localhost'
db_name = 'portugaltotal'

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  # ('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

url = 'http://localhost:5984/portugaltotal/_design/etiquetado/_view/twitter'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
dic = {}
label = ""
json_data = []
cont_positives = 0
cont_negatives = 0
cont_neutrals = 0
cont_total = 0
for x in d['rows']:
    a = x['value']
    datoslimpios = filtrarDatos(a)
    #try:
    testimonial = TextBlob(str(datoslimpios))
    if str(datoslimpios) != 'None':
        if testimonial.sentiment.polarity > 0:
            label = 'positive'
            cont_positives = cont_positives + 1
        elif testimonial.sentiment.polarity < 0:
            label = 'negative'
            cont_negatives = cont_negatives + 1

        else:
            label = 'neutral'
            cont_neutrals = cont_neutrals + 1
        cont_total = cont_total + 1

        dic['text'] = str(datoslimpios).strip()
        dic['label'] = label
        json_data.append(dict(dic))
        print json_data
        #if cont_total == 100:
            #break

# print dic
jsonfinal = json.dumps(json_data)
fichero = open('sentimientosPortugal30.json', 'w')
fichero.write(jsonfinal)
arreglo = [cont_positives, cont_negatives, cont_neutrals]
dibujar(arreglo)
print jsonfinal
fichero.close()

f.close()

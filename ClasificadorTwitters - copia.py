#-*- coding: utf-8 -*-
from textblob import TextBlob
import sys
import couchdb
import json
import nltk
import urllib2
import re
import matplotlib.pyplot as plt
from couchdb import view
# nltk.download('punkt')
from textblob.classifiers import NaiveBayesClassifier

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
    fig.gca().add_artist(centre_circle)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()


with open('sentimientosFrancia30.json', 'r') as fp:
    print 'LOADING DATA...'
    cl = NaiveBayesClassifier(fp, format='json')
    print cl

URL = 'localhost'
db_name = 'franciatotal'

'''========couchdb'=========='''
server = couchdb.Server('http://' + URL + ':5984/')  # ('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    # print db_name
    db = server[db_name]
    print 'Correcta conexion a la vista...'

finally:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

url = 'http://localhost:5984/franciatotal/_design/pruebaFecha/_view/twitter'
req = urllib2.Request(url)
f = urllib2.urlopen(req)

d = json.loads(f.read())
cont_positives = 0
cont_negatives = 0
cont_neutrals = 0
cont_total = 0
print 'CLASSIFYING VIEW (TEXT)...'
for x in d['rows']:
    a = x['value']
    datoslimpios = filtrarDatos(a)
    #try:
    aux = cl.classify(str(datoslimpios))
    if str(datoslimpios) != 'None':
        if aux == 'positive':
            label = 'positive'
            cont_positives = cont_positives + 1
        elif aux == 'negative':
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

'''print 'EVALUATING CLASSIFIERS...'
with open('sentimientosTest.json', 'r') as fp2:
    print 'ACCURACY:' + str(cl.accuracy(fp2, format='json'))'''

cl.show_informative_features(5)
arreglo = [cont_positives, cont_negatives, cont_neutrals]
dibujar(arreglo)
fp.close()
fp2.close()
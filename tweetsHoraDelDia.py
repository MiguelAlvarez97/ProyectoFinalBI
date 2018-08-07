#-*- coding: utf-8 -*-
import sys
import couchdb
import urllib2
import json
URL = 'localhost'
db_name = 'rusiatotal'

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  # ('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

url = 'http://localhost:5984/rusiatotal/_design/hora/_view/hora'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
dic = {}
for x in d['rows']:
    a = x['value']
    arreglo = str(a).split(" ")
    arreglo2 = arreglo[3].split(':')
    hora = arreglo2[0]
    if dic.has_key(hora):
        dic[hora]=dic.get(hora)+1
    else:
        dic[hora]=1

print dic


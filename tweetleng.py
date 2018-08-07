#-*- coding: utf-8 -*-
import sys
import couchdb
import urllib2
import json
URL = 'localhost'
db_name = 'uruguaytotal'

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  # ('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

url = 'http://localhost:5984/uruguaytotal/_design/leng/_view/leng'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
dic = {}
for x in d['rows']:
    a = x['value']

    if dic.has_key(a):
        dic[a]=dic.get(a)+1
    else:
        dic[a]=1

print dic


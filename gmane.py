import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

baseurl = "https://api.data.gov.in/resource/1731b51f-8714-4b8f-9243-0526063da4a5?format=xml&api-key=579b464db66ec23bdd000001e54d9f049d9f423c7f0fea5b54317529"

cur.executescript('''DROP TABLE IF EXISTS revenue;''')
cur.execute('''CREATE TABLE  revenue
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, service TEXT, y2006_07 INTEGER,
     y2007_08 INTEGER,y2008_09 INTEGER,y2009_10 INTEGER,
     y2010_11 INTEGER,y2011_12 INTEGER,y2012_13 INTEGER,
     y2013_14 INTEGER,y2014_15 INTEGER,y2015_16 INTEGER, Growth INTEGER)''')

document = urllib.request.urlopen(baseurl, None, 30, context=ctx)
text = document.read().decode()
dom = ET.fromstring(text)
all =dom.findall('records/item')
print('Dict count:', len(all))

for entry in all:
    name = entry[0].text
    y2006_07 = entry[1].text
    y2007_08 = entry[2].text
    y2008_09 = entry[3].text
    y2009_10 = entry[4].text
    y2010_11 = entry[5].text
    y2011_12 = entry[6].text
    y2012_13 = entry[7].text
    y2013_14 = entry[8].text
    y2014_15 = entry[9].text
    y2015_16 = entry[10].text
    growth = entry[11].text

    if y2006_07=="NA":
        y2006_07=-1
    if y2007_08=="NA":
        y2007_08=-1
    if y2008_09=="NA":
        y2008_09=-1
    if y2009_10=="NA":
        y2009_10=-1
    #print(name,y2006_07,y2007_08,y2008_09,y2009_10,y2010_11,y2011_12,y2012_13,y2013_14,y2014_15,y2015_16,growth)
    cur.execute('''INSERT INTO revenue
            (service, y2006_07,
             y2007_08,y2008_09 ,y2009_10,
             y2010_11 ,y2011_12 ,y2012_13 ,
             y2013_14 ,y2014_15 ,y2015_16 , Growth )
            VALUES ( ?, ?, ?, ?, ?,?, ?, ?, ?, ? ,?,? )''',(name,y2006_07,y2007_08,y2008_09,y2009_10 ,y2010_11 ,y2011_12,y2012_13,y2013_14 ,y2014_15 ,y2015_16 ,growth ) )

conn.commit()

cur.close()

https://api.data.gov.in/resource/b46200c1-ca9a-4bbe-92f8-b5039cc25a12?format=xml&api-key=579b464db66ec23bdd000001e54d9f049d9f423c7f0fea5b54317529
https://api.data.gov.in/resource/6911b243-d924-404d-a587-7717bd7c7eb9?format=xml&api-key=579b464db66ec23bdd000001e54d9f049d9f423c7f0fea5b54317529

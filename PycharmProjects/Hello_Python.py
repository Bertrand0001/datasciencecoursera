import random
import sys
import os

V_Name = "Bertrand Loison"
V_shortname = "Bertrand"

print ("Hello World")
print(V_Name)
print(V_shortname)
print("Resultats",2**3)

Test = "Marianne"
print(len(Test))
print(Test.upper())

x=5
def hello(x):
    print("hello",x)
x=6
hello(x)

#Ce programme permet d'identifier les bus qui se dirige au nord du bureau de Dave

import urllib.request
u=urllib.request.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
data=u.read()
f=open("rt22.xml","wb")
f.write(data)
f.close()

daves_latitude=41.98062
daves_longitude=-87.668452

from xml.etree.ElementTree import parse
doc=parse("rt22.xml")

for bus in doc.findall("bus"):
    lat=float(bus.findtext("lat"))
    if lat > daves_latitude:
        direction=bus.findtext("d")
        if direction.startswith("North"):
            busid=bus.findtext("id")
            print (busid, lat)

#Bus candidats

import urllib.request
Candidates=["1412","1720"]

def distance (lat1, lat2):
    #renvoie la distance en miiles entre les deux latitudes
    return 69*abs(lat1-lat2)

def monitor():
   u=urllib.request.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
   doc=parse(u)
   for bus in doc.findall("bus"):
       busid=bus.findtext("id")
       if busid in Candidates:
           lat=float(bus.findtext("lat"))
           dis=distance(lat, daves_latitude)
           print(busid,dis,"miles")
           print("-"*10)

import time
while True:
    monitor()
    time.sleep(10)







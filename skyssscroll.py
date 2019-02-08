import requests
import signal
import time
import scrollphathd
from scrollphathd.fonts import font3x5

def getTime():
    r = requests.get("https://skyss.giantleap.no/public/departures?Hours=1&StopIdentifiers=12015491")
    json_result = r.json()
    for x in json_result:
        forsteDest = r.json()["PassingTimes"][0]["TripDestination"] #førstkommende avgang representert ved 0
        nesteDest = r.json()["PassingTimes"][1]["TripDestination"] #neste avgang representert ved 1
        forsteBuss = r.json()["PassingTimes"][0]["DisplayTime"]
        nesteBuss = r.json()["PassingTimes"][1]["DisplayTime"]
        str1 = (forsteDest, ' ', forsteBuss,', ', nesteDest, ' ', nesteBuss)

    while True:
        scrollphathd.write_string(str1, y=1, font=font3x5, brightness=0.5)
        scrollphathd.flip(x,y)
        scrollphathd.scroll()    
        scrollphathd.show()
        print(str1)
        
while True:
    getTime() 

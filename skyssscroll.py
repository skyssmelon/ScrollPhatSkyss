
import requests
import signal
import scrollphathd
from scrollphathd.fonts import font3x5


r = requests.get("https://skyss.giantleap.no/public/departures?Hours=1&StopIdentifiers=12015491")
dest = r.json()["PassingTimes"][0]["TripDestination"]
avgang = r.json()["PassingTimes"][0]["DisplayTime"]
dest2 = r.json()["PassingTimes"][1]["TripDestination"]
avgang2 = r.json()["PassingTimes"][1]["DisplayTime"]

linje2 = dest + " " + avgang + ",   " + dest2 + " " + avgang2 + ",   "

    

while True:
     scrollphathd.write_string(str1, y=1, font=font3x5, brightness=0.5)
     scrollphathd.flip(x,y)
     scrollphathd.scroll()    
     scrollphathd.show()
        print(linje2)

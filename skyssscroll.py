import requests
import time
import scrollphathd as sphd

r = requests.get('https://skyss.giantleap.no/public/departures?Hours=1&StopIdentifiers=12015491') #henter ruteinfo

d1 = r.json()["PassingTimes"][0]["TripDestination"] #førstkommende avgang representert ved 0
d2 = r.json()["PassingTimes"][1]["TripDestination"] #neste avgang representert ved 1
t1 = r.json()["PassingTimes"][0]["DisplayTime"]
t2 = r.json()["PassingTimes"][1]["DisplayTime"]

str1 = (d1, ' ', t1, ',  ', d2, ' ', t2)

sphd.write_string(str1)

while True:
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)

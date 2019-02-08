"""
Direct copy of ansias scrollphatbus script
Not testet yet
"""

import requests
import signal
import time
import scrollphathd
from scrollphathd.fonts import font3x5

def getTime():
    r = requests.get("https://skyss.giantleap.no/public/departures?Hours=1&StopIdentifiers=12015491")
    json_result = r.json()
    my_stops = []
    for x in json_result:
        y = str(int(x['TripDestination']/60)).zfill(2)
        z = ' min ' + str(x['DisplayTime'])
        my_stops.append(y)
        my_stops.sort()
        str1 = ', '.join(my_stops) +', '

    while True:
        scrollphathd.write_string(str1, y=1, font=font3x5, brightness=0.5)
        scrollphathd.flip(x,y)
        scrollphathd.scroll()    
        scrollphathd.show()
        print(str1)
        
while True:
    getTime() 

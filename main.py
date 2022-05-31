####
# TODO:harmonogram is saved to a json, so the app can be quit safely
#       it is also saved after every delay

####

import os
from playsound import playsound
import datetime

from utillities import *


## FILE PATHS
sound_block_path = os.path.normpath("sounds/beep.mp3")
sound_pause_start_path = os.path.normpath("sounds/ding.mp3")
sound_pause_end_path = os.path.normpath("sounds/wood.mp3")

harmonogram_path = "data/harmonogram.json"

## INTERVAL class
class interval:
    def __init__(self, when, who, what, time, where, date):
        year = "2022_"
        format = "%Y_%d.%m.%H:%M"
        start, end = when.split("-")
        self.start_time = datetime.datetime.strptime(year+date+start, format)
        self.end_time = datetime.datetime.strptime(year+date+end, format)
        self.who = who
        if what == "pauza" or what == "pause":
            self.type = "pause"
            self.title = "pause"
        else:
            self.type = "block"
            self.title = what
        self.duration = time
        self.location = where
        self.done = False

    def __repr__(self):
        return f"{self.start_time} {self.type} {self.title}"

    def __str__(self):
        return f"{self.start_time} {self.type} {self.title}"

## CONVERSION to harmonogram
def md2harmonogram(inp):
    inp = inp.replace("`"," ")
    lines = inp.split('\n')
    ret=[]
    keys=[]
    day=""
    date=""
    harmonogram = []

    for i,line in enumerate(lines):
        line = line.strip(" ")
        if i == 0:
            # from the first line in the table, get the day and dat by spliting at space
            day, date = line.split('|')[1].strip().split(" ")
        elif i == 2:
            keys=[_i.strip() for _i in line.split('|')]
        else:
            ret.append({keys[_i]:v.strip() for _i,v in enumerate(line.split('|')) if  _i>0 and _i<len(keys)-1})
        for dict in ret:
            if not dict:
                ret.remove(dict)

    for i, dict in enumerate(ret):
        item = interval(dict["WHEN"], dict["WHO"], dict["WHAT"], dict["TIME"], dict["WHERE"], date)
        harmonogram.append(item)
    return harmonogram

## HARMONOGRAM functions
def add_delay(harmonogram, minutes):
    for item in harmonogram:
        if not item.done:
            item.start_time + datetime.timedelta(minutes=minutes)
            item.end_time + datetime.timedelta(minutes=minutes)


tabulka = """| PÁTEK 30.5.                   |                                |                                          |          | AGD1 |
    | ----------------------------- | ------------------------------ | ---------------------------------------- | -------- | ----- |
    | WHEN                          | WHO                            | WHAT                                     | TIME     | WHERE |
    | `12:00-13:00`                 |                                | příchod / společný oběd v ateliéru       |          |       |
    | `13:00-13:40`                 | @Zuzana                        | update pracovní skupina “favu-hodnocení” | 40 min   |       |
    | `13:40-14:20`                 | @JakubS                        | project-log                              | 40 min   |       |
    | `14:20-14:40`                 |                                | `pauza`                                  | 20 min   |       |
    | `14:40-15:20`                 | @xvburak+                      | agdx-sustredko                           | 40 min   |       |
    | `15:20-16:00`                 | @ondrej                        | agdx-merch - diskuze(?)                  | 40 min   |       |
    | `16:00-16:20`                 |                                | `pauza`                                  | 20 min   |       |
    | `16:20-18:00`                 | @Zuzana + #final-thesis people | Update k pracem, pojetí obhajob atp.     | 1h 40min |       |
    | `19:17-18:20`                 |                                | `pauza`                                  | 20 min   |       |
    | `19:18-19:00`                 | @agd1/x                        | (klauzury?)                              | 40 min   |       |
    | `19:19-23:59`                 | @agdx                          | afterka                                  | ?        |       |
   """

harmonogram = md2harmonogram(tabulka)
save_harmonogram(harmonogram, harmonogram_path)

bola_pauza = False
current_time = datetime.datetime.now()
for item in harmonogram:
    while not item.done:
        current_time = datetime.datetime.now()
        # if start_time uz bol, ale nie davnejseie ako 1 minutu dozadz, tak zvon
        if item.start_time <= current_time < item.start_time + datetime.timedelta(seconds=30):
            if item.type == "pause":
                bola_pauza = True
                playsound(sound_pause_start_path)
                item.done = True
            elif bola_pauza == True:
                bola_pauza = False
                playsound(sound_pause_end_path)
                item.done = True
            else :
                playsound(sound_block_path)
                item.done = True
        # ak start_time uz bol, davnejsie ako 1 minutut dozadu, tak proste done
        elif item.start_time < current_time:
            item.done = True
####
# TODO: save_harmonogram
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
    def __init__(self, date, when, who="", what="", time="", where=""):
        year = "2022_"
        format = "%Y_%d.%m.%H:%M"
        
        self.start_time = datetime.datetime.strptime(year+date+when.split("-")[0], format)
        try:
            self.end_time = datetime.datetime.strptime(year+date+when.split("-")[1], format)
        except:
             self.end_time = ""
        self.duration = time # this is not used right now
        
        self.who = who
        if what == "pauza" or what == "pause":
            self.type = "pause"
            self.title = "pause"
        else:
            self.type = "block"
            self.title = what
        self.location = where
        self.done = False

    def __repr__(self):
        return f"{self.start_time} {self.type} {self.title}"

    def __str__(self):
        return f"{self.start_time} {self.type} {self.title}"

## CONVERSION from markdown to harmonogram
def md2harmonogram(inp):
    inp = inp.replace("`"," ")
    lines = inp.split('\n')
    list=[]
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
            # the third line holds keys
            keys=[_i.strip() for _i in line.split('|')]
        else:
            dict = ({keys[_i]:v.strip() for _i,v in enumerate(line.split('|')) if  _i>0 and _i<len(keys)-1})
            if dict:
                list.append(dict)
    for dict in list:
        item = interval(date, dict.get("WHEN",""), dict.get("WHO",""), dict.get("WHAT",""), dict.get("TIME",""), dict.get("WHERE",""))
        harmonogram.append(item)
    return harmonogram

## HARMONOGRAM functions
def add_delay(harmonogram, minutes):
    for item in harmonogram:
        if not item.done:
            item.start_time + datetime.timedelta(minutes=minutes)
            item.end_time + datetime.timedelta(minutes=minutes)


tabulka = """| ŠTVRTOK 2.6. |                      |                                                 |
| ------------ | -------------------- | ----------------------------------------------- |
| WHEN         | WHO                  | WHAT                                            |
| 10:00        | @everyone            | příchod                                         |
| 10:15        | @Zuzana              | úvod                                            |
| 10:30        | @danielmstc @hellboi | #agdx-irl (agdx-report)                         |
| 11:00        | @honza_suchy         | Untitled menu app (agdx-project)                |
| 11:30        | @everyone            | pauza (10min)                                   |
| 11:40        | @petr                | KAM (agdx-project)                              |
| 12:10        | @julie               | podcast (agdx-project)                          |
| 12:40        | @everyone            | obed (60min)                                    |
| 13:40        | @v.adela             | metodika psaní, myšlenky o textu (agdx-project) |
| 14:10        | @Ondřej              | typo report, in progress type (agdx-project)    |
| 14:40        | @everyone            | pauza (10min)                                   |
| 14:50        | @JakubS              | web Duholeum - generátor                        |
| 15:20        | @FlyingMochi         | VR podcast                                      |
| 15:50        | @everyone            | pauza (10min)                                   |
| 16:00        | @everyone            | diskuse o sebahodnocení                         |

"""

harmonogram = md2harmonogram(tabulka)
save_harmonogram(harmonogram, harmonogram_path)
# harmonogram = load_harmonogram(harmonogram_path)
# for item in harmonogram:
#     print(type(item))

# bola_pauza = False
# current_time = datetime.datetime.now()
# for item in harmonogram:
#     while not item.done:
#         current_time = datetime.datetime.now()
#         # if start_time uz bol, ale nie davnejseie ako 1 minutu dozadz, tak zvon
#         if item.start_time <= current_time < item.start_time + datetime.timedelta(seconds=30):
#             if item.type == "pause":
#                 bola_pauza = True
#                 playsound(sound_pause_start_path)
#                 item.done = True
#             elif bola_pauza == True:
#                 bola_pauza = False
#                 playsound(sound_pause_end_path)
#                 item.done = True
#             else :
#                 playsound(sound_block_path)
#                 item.done = True
#         # ak start_time uz bol, davnejsie ako 1 minutut dozadu, tak proste done
#         elif item.start_time < current_time:
#             item.done = True
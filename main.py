####
# TODO: timer methods - add 10 minutes
####

import os
from time import time
from playsound import playsound
import datetime
import json


## FILE PATHS
sound_block_path = os.path.normpath("sounds/beep.mp3")
sound_pause_start_path = os.path.normpath("sounds/ding.mp3")
sound_pause_end_path = os.path.normpath("sounds/wood.mp3")

harmonogram_path = "data/harmonogram.json"

## CONVERSION from markdown to harmonogram
def md2harmonogram(inp):
    inp = inp.replace("`"," ")
    lines = inp.split('\n')
    list=[]
    keys=[]
    day=""
    date=""
    when=""
    year = "2022-"
    type="block"
    harmonogram = []
    format = "%Y-%d.%m.%H:%M"

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
    
    # turn the table list of dicts to a harmonogram of intervals
    for i, dict in enumerate(list):
        when = dict.get("WHEN")
        start = datetime.datetime.strptime(year+date+when.split("-")[0], format)
        end = ""

        what = dict.get("WHAT","")
        if "pauza" in what or "pause" in what or "příchod" in what:
            type = "pause"
        else:
            type = "block"

        item = interval( start, end, type, dict.get("WHO",""), what, dict.get("TIME",""), dict.get("WHERE",""))
        harmonogram.append(item)
    
    # add end_time to all items
    for i, item in enumerate(harmonogram):
        try:
            item.end_time = harmonogram[i+1].start_time
        except:
            item.end_time = datetime.datetime.strptime(year+date+"00:00", format)

    return harmonogram

## INTERVAL class
class interval:
    def __init__(self, start, end="", type="block", who="", title="", time="", where=""):
        
        self.start_time = start

        self.end_time = end # this should ideally be optional
        self.duration = time # this is not used right now
        
        self.type = type
        self.who = who
        self.title = title
        self.location = where
        self.done = False

    def __repr__(self):
        return f"{self.start_time} {self.type} {self.title}"

    def __str__(self):
        return f"{self.start_time} {self.type} {self.title}"

## TIMER class
class timer:
    def __init__(self, harmonogram):
        self.harmonogram = harmonogram
    
    def arm(self):
        current_time = datetime.datetime.now()
        for i, item in enumerate(self.harmonogram):
            while not item.done:
                current_time = datetime.datetime.now()
                # if start_time uz bol, ale nie davnejseie ako 30 sekund, tak zvon
                if item.start_time <= current_time < item.start_time + datetime.timedelta(seconds=30):
                    if item.type == "pause":
                        playsound(sound_pause_start_path)
                        item.done = True
                        print(item)
                    elif harmonogram[i-1].type == "pause":
                        playsound(sound_pause_end_path)
                        item.done = True
                        print(item)
                    else:
                        playsound(sound_block_path)
                        item.done = True
                        print(item)
                # ak start_time uz bol, davnejsie ako 1 minutu dozadu, tak je uz item done
                elif item.start_time < current_time:
                    item.done = True

## HARMONOGRAM functions
def save_harmonogram(harmonogram, file_path):
    with open(file_path, "w") as f:
        data = []
        for item in harmonogram:
            data.append(item.__dict__)
        json.dump(data, f, indent=4, default=str)
    return True

def load_harmonogram(file_path):
    harmonogram = []
    format = "%Y-%m-%d %H:%M:%S"
    with open(file_path) as f:
        try: list = json.load(f)
        except: return False
    for dict in list:
        start_time = datetime.datetime.strptime(dict.get("start_time"), format)
        end_time = datetime.datetime.strptime(dict.get("end_time"), format)
        harmonogram.append(interval(start_time, end_time, dict.get("type","block"), dict.get("who",""), dict.get("what",""), dict.get("time",""), dict.get("location","")))
    return harmonogram

def add_delay(harmonogram, minutes):
    for item in harmonogram:
        if not item.done:
            item.start_time + datetime.timedelta(minutes=minutes)
            try:
                item.end_time + datetime.timedelta(minutes=minutes)
            except:
                pass
    return harmonogram


tabulka = """| ŠTVRTOK 31.5. |                      |                                                 |
| ------------ | -------------------- | ----------------------------------------------- |
| WHEN         | WHO                  | WHAT                                            |
| 17:40        | @everyone            | příchod                                         |
| 17:41        | @Zuzana              | úvod                                            |
| 17:42        | @danielmstc @hellboi | #agdx-irl (agdx-report)                         |
| 17:43        | @honza_suchy         | Untitled menu app (agdx-project)                |
| 17:44        | @everyone            | pauza (10min)                                   |
| 17:47        | @petr                | KAM (agdx-project)                              |
| 17:50        | @julie               | podcast (agdx-project)                          |
| 17:55        | @everyone            | obed (60min)                                    |
| 18:00        | @v.adela             | metodika psaní, myšlenky o textu (agdx-project) |
| 18:10        | @Ondřej              | typo report, in progress type (agdx-project)    |
| 18:15        | @everyone            | pauza (10min)                                   |
| 18:30        | @JakubS              | web Duholeum - generátor                        |
| 18:40        | @FlyingMochi         | VR podcast                                      |
| 18:50        | @everyone            | pauza (10min)                                   |
| 19:00        | @everyone            | diskuse o sebahodnocení                         |

"""
harmonogram = md2harmonogram(tabulka)
save_harmonogram(harmonogram, harmonogram_path)
harmonogram = load_harmonogram(harmonogram_path)

bell = timer(harmonogram)
bell.arm()
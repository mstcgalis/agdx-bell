####
# TODO: timer methods - add 10 minutes
####

import os
from playsound import playsound
from datetime import datetime, timedelta
import json


## FILE PATHS
sound_block_path = os.path.normpath("sounds/beep.mp3")
sound_pause_start_path = os.path.normpath("sounds/ding.mp3")
sound_pause_end_path = os.path.normpath("sounds/wood.mp3")

harmonogram_path = os.path.normpath("data/harmonogram.json")
harmonogram_path = "/Users/atelier/Library/Application Support/agdx-roadmap.live/harmonogram.json"

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
        start = datetime.strptime(year+date+when.split("-")[0], format)
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
            item.end_time = datetime.strptime(year+date+"00:00", format)

    return harmonogram

## INTERVAL class
class interval:
    def __init__(self, start, end="", type="block", who="", what="", time="", where=""):
        
        self.start_time = start

        self.end_time = end # this should ideally be optional
        self.duration = time # this is not used right now
        
        self.type = type
        self.who = who
        self.what = what
        self.location = where
        self.done = False

    def __repr__(self):
        return f"{self.start_time}-{self.end_time}, {self.type}, {self.who}, {self.what}"

    def __str__(self):
        return f"{self.start_time}-{self.end_time}, {self.type}, {self.who}, {self.what}"

## TIMER class
class bell:
    def __init__(self, harmonogram):
        self.harmonogram = harmonogram
        self.done = False

    def get_current_interval(self):
        for item in self.harmonogram:
            current_time = datetime.now()
            if item.end_time > current_time:
                return item
        # if there is no current interval
        return False
    
    def get_next_interval(self):
        for i, item in enumerate(self.harmonogram):
            current_time = datetime.now()
            if item.end_time > current_time:
                if type(self.harmonogram[i+1]) == interval:
                    return self.harmonogram[i+1]
                else:
                    return False
        return False

    # this will be triggered every second
    # if it is time, ring and return the item
    # else a intrval is currently in progess - return True
    # if there is no current interval, return False
    def arm(self):
        current_time = datetime.now()
        for i, item in enumerate(self.harmonogram):
                # if start_time uz bol, ale nie davnejseie ako 30 sekund, tak zvon
                if item.start_time <= current_time < item.start_time + timedelta(seconds=10) and not item.done:
                    if item.type == "pause":
                        playsound(sound_pause_start_path)
                        item.done = True
                        return item
                    elif self.harmonogram[i-1].type == "pause":
                        playsound(sound_pause_end_path)
                        item.done = True
                        return item
                    else:
                        playsound(sound_block_path)
                        item.done = True
                        return item
                # ak je item prave teraz current, return True
                elif item.start_time < current_time < item.end_time:
                    return True
                # inak je uz item done
                else: item.done = True           
        self.done = True
        return False

    def delay(self, minutes):
        self.harmonogram = add_delay(self.harmonogram, minutes)
        save_harmonogram(self.harmonogram)

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
    try:
        with open(file_path) as f:
            list = json.load(f)
    except: return False
    for dict in list:
        start_time = datetime.strptime(dict.get("start_time"), format)
        end_time = datetime.strptime(dict.get("end_time"), format)
        harmonogram.append(interval(start_time, end_time, dict.get("type","block"), dict.get("who",""), dict.get("what",""), dict.get("time",""), dict.get("location","")))
    return harmonogram

def add_delay(harmonogram, minutes):
    for item in harmonogram:
        if not item.done:
            item.start_time + timedelta(minutes=minutes)
            try:
                item.end_time + timedelta(minutes=minutes)
            except:
                pass
    return harmonogram
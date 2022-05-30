import os
from tracemalloc import start
from playsound import playsound
import datetime
import json

sound_block_path = os.path.normpath("sounds/beep.mp3")
sound_pause_start_path = os.path.normpath("sounds/ding.mp3")
sound_pause_end_path = os.path.normpath("sounds/wood.mp3")

def md2data(inp):
    lines = inp.split('\n')
    ret=[]
    keys=[]
    day=""
    date=""
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
    return [day, date, ret]
    return json.dumps(ret, indent = 4)

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

    def __repr__(self):
        return f"{self.start_time} {self.type} {self.title}"

    def __str__(self):
        return f"{self.start_time} {self.type} {self.title}"
    

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
    | `18:00-18:20`                 |                                | `pauza`                                  | 20 min   |       |
    | `18:20-19:00`                 | @agd1/x                        | (klauzury?)                              | 40 min   |       |
    | `19:00-00:00`                 | @agdx                          | afterka                                  | ?        |       |
   """

day, date, tabulka = md2data(tabulka.replace("`"," "))

harmonogram = []
for i, dict in enumerate(tabulka):
    item = interval(dict["WHEN"], dict["WHO"], dict["WHAT"], dict["TIME"], dict["WHERE"], date)
    harmonogram.append(item)

for item in harmonogram:
    # update current_time
    # check if start_time uz bol
        # if yes
            # skip to next interval
            # beep
    

beeped = False
while beeped == False:
    # get the current_time
    current_time = datetime.datetime.now()
    # check if time1 >= current_time
    if time1 <= current_time:
        # if yes, beep and break
        playsound(sound_path)
        beeped = True
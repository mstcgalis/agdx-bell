import os
from playsound import playsound
import datetime
import json

sound_path = "sounds/beep.mp3"
sound_path = os.path.normpath(sound_path)

def md2json(inp):
    lines = inp.split('\n')
    ret=[]
    keys=[]
    for i,line in enumerate(lines):
        line = line.strip(" ")
        if i==2:
            keys=[_i.strip() for _i in line.split('|')]
        else:
            ret.append({keys[_i]:v.strip() for _i,v in enumerate(line.split('|')) if  _i>0 and _i<len(keys)-1})
    return json.dumps(ret, indent = 4) 

tabulka = """| PÁTEK 30.5.                   |                                |                                          |          | AGD1 |
    | ----------------------------- | ------------------------------ | ---------------------------------------- | -------- | ---- |
    | KDY (vyplňuje WG)             | KDO                            | CO                                       | ČAS      | KDE  |
    | `12:00—13:00`                 |                                | příchod / společný oběd v ateliéru       |          |      |
    | `13:00-13:40`                 | @Zuzana                        | update pracovní skupina “favu-hodnocení” | 40 min   |      |
    | `13:40-14:20`                 | @JakubS                        | project-log                              | 40 min   |      |
    | `14:20-14:40`                 |                                | `pauza`                                  | 20 min   |      |
    | `14:40-15:20`                 | @xvburak+                      | agdx-sustredko                           | 40 min   |      |
    | `15:20-16:00`                 | @ondrej                        | agdx-merch - diskuze(?)                  | 40 min   |      |
    | `16:00-16:20`                 |                                | `pauza`                                  | 20 min   |      |
    | `16.20-18:00`                 | @Zuzana + #final-thesis people | Update k pracem, pojetí obhajob atp.     | 1h 40min |      |
    | `18:00-18:20`                 |                                | `pauza`                                  | 20 min   |      |
    | `18:20-19:00`                 | @agd1/x                        | (klauzury?)                              | 40 min   |      |
    | `19:00-XX:00`                 | @agdx                          | afterka                                  | ?        |      |
   """

tabulka = tabulka.replace("`"," ")
tabulka = md2json(tabulka)
print(tabulka)


# # datum vo formate DD-MM-YYYY
# date_string = "30-05-2022-"
# # cas v 24h formate, HH:MM
# pauza_string = "13:04-14:20"

#format = "%d-%m-%Y-%H:%M"
# time1 = datetime.datetime.strptime(date_string+pauza_string, format)

# beeped = False
# while beeped == False:
#     # get the current_time
#     current_time = datetime.datetime.now()
#     print(current_time)
#     # check if time1 >= current_time
#     if time1 <= current_time:
#         # if yes, beep and break
#         playsound(sound_path)
#         beeped = True
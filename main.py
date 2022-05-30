import os
from playsound import playsound
import datetime

sound_path = "sounds/beep.mp3"
sound_path = os.path.normpath(sound_path)

tabulka = """
    | PÁTEK 30.5.                   |                                |                                          |          | AGD1 |
    | ----------------------------- | ------------------------------ | ---------------------------------------- | -------- | ---- |
    | KDY (vyplňuje WG)             | KDO                            | CO                                       | ČAS      | KDE  |
    | `12:00—13:00`                 |                                | příchod / společný oběd v ateliéru       |          |      |
    | `13``:``00–13``:``40`         | @Zuzana                        | update pracovní skupina “favu-hodnocení” | 40 min   |      |
    | `13``:``40–14``:``20`         | @JakubS                        | project-log                              | 40 min   |      |
    | `14``:``20–14``:``40`         |                                | `pauza`                                  | 20 min   |      |
    | `14``:``40–15``:``20`         | @xvburak+                      | agdx-sustredko                           | 40 min   |      |
    | `15``:``20–16``:``00`         | @ondrej                        | agdx-merch - diskuze(?)                  | 40 min   |      |
    | `16:00–16:20`                 |                                | `pauza`                                  | 20 min   |      |
    | `16.20–18:00`                 | @Zuzana + #final-thesis people | Update k pracem, pojetí obhajob atp.     | 1h 40min |      |
    | `18:00–18:20`                 |                                | `pauza`                                  | 20 min   |      |
    | `18:20–19:00`                 | @agd1/x                        | (klauzury?)                              | 40 min   |      |
    | `19:00-XX:00`                 | @agdx                          | afterka                                  | ?        |      |
    | SOBOTA 31.5.                  |                                |                                          |          | AGD1 |
    | KDY (vyplňuje WG)             | KDO                            | CO                                       | ČAS      | KDE  |
    | `12:00-13:00`                 | @julie                         | příchod / společné vaření v ateliéru     | 60min    |      |
    | `13:``4``0–14:``2``0`         | @danielmstc                    | list.app project log                     | 40 min   |      |
    | `13:00–13:40`                 | @julie                         | podcast talk                             | 40 min   |      |
    | `14:``2``0–14:``4``0`         |                                | `pauza`                                  | 20 min   |      |
    | `14:``4``0–15:``0``0`         | @ondrej                        | project-log                              | 20 min   |      |
    | `15:``0``0–1``6``:``0``0`     | @agdx-website                  | synteza self-logs                        | 60 min   |      |
    | `16.``0``0–1``6``.20`         |                                | `pauza`                                  | 20 min   |      |
    | `1``6``:``2``0–1``7``:``0``0` | @xvburak                       | one army intro                           | 40 min   |      |
    | `1``7``:``0``0–1``7``:``4``0` | @v.adela                       | project-log                              | 40 min   |      |
    | `1``7``:``4``0–1``8``:``0``0` |                                | `pauza`                                  | 20 min   |      |
    | `1``8``:``0``0–1``8``:``4``0` | @katerina                      | organizing app (idea + discussion)       | 40 min   |      |
    | `1``8``:``4``0–1``9``:``0``0` | @agd1/x                        | (heslá na atelierové macy?)              | 20 min   |      |
    | `19:00-XX:00`                 | @agdx                          | afterka                                  | ?        |      |"""

tabulka = tabulka.strip("`")
print(tabulka)

# datum vo formate DD-MM-YYYY
date_string = "30-05-2022-"
# cas v 24h formate, HH:MM
pauza_string = "13:04-14:20"


format = "%d-%m-%Y-%H:%M"

time1 = datetime.datetime.strptime(date_string+pauza_string, format)

beeped = False
while beeped == False:
    # get the current_time
    current_time = datetime.datetime.now()
    print(current_time)
    # check if time1 >= current_time
    if time1 <= current_time:
        # if yes, beep and break
        playsound(sound_path)
        beeped = True
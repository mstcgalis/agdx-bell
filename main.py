from logic import *

## PATHS
harmonogram_path = os.path.normpath("data/harmonogram.json")


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
| 18:20        | @everyone            | pauza (10min)                                   |
| 18:21        | @JakubS              | web Duholeum - generátor                        |
| 18:22        | @FlyingMochi         | VR podcast                                      |
| 18:23        | @everyone            | pauza (10min)                                   |
| 19:00        | @everyone            | diskuse o sebahodnocení                         |

"""
harmonogram = md2harmonogram(tabulka)
save_harmonogram(harmonogram, harmonogram_path)

bell = timer(load_harmonogram(harmonogram_path))
while bell.arm != False:
    print(bell.arm())
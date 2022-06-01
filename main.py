import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer

from window import Ui_MainWindow
from logic import *

## DATA
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
| 21:55        | @JakubS              | web Duholeum - generátor                        |
| 21:59        | @FlyingMochi         | VR podcast                                      |
| 22:55        | @everyone            | pauza (10min)                                   |
| 23:00        | @everyone            | diskuse o sebahodnocení                         |

"""
harmonogram = md2harmonogram(tabulka)
save_harmonogram(harmonogram, harmonogram_path)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.bell = bell(load_harmonogram(harmonogram_path))

        self.hh_mm_format = "%H:%m"

        # creating a timer object
        timer = QTimer(self)
        # adding action to timer
        timer.timeout.connect(self.tick)
        # update the timer every second
        timer.start(1000)
    
    def tick(self):
        current = self.bell.arm()
        # if true, do nothing
        if current:
            pass
        # if a new item has rung, update the ui
        # if there is no interval lef, also update the ui
        else:
            self.update_intervals()
        # update the clock
        

    
    def update_intervals(self):
        # upłdate the current_interval
        current_interval = self.bell.get_current_interval()
        if current_interval == False:
                self.now_start_end.setText("00-00")
                self.now_who.setText("@everyone")
                self.now_what.setText("nothing")
        else:
            self.now_start_end.setText(current_interval.start_time.strftime(self.hh_mm_format) + "-" + current_interval.end_time.strftime(self.hh_mm_format))
            self.now_who.setText(current_interval.who)
            self.now_what.setText(current_interval.title)
        # update the next_interval
        next_interval = self.bell.get_next_interval()
        if next_interval == False:
            self.next_start_end.setText("00-00")
            self.next_who.setText("@everyone")
        else:
            self.next_start_end.setText(next_interval.start_time.strftime(self.hh_mm_format) + "-" + next_interval.end_time.strftime(self.hh_mm_format))
            self.now_who.setText(next_interval.who)
    
    def update_clock(self):
        self.clock.setText(datetime.datetime.now().strftime(self.hh_mm_format))



# LAUNCH
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
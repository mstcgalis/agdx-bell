import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer

from window import Ui_MainWindow
from logic import *

## DATA
harmonogram_path = os.path.normpath("data/harmonogram.json")
tabulka = """| ŠTVRTOK 1.6. |                      |                                                 |
| ------------ | -------------------- | ----------------------------------------------- |
| WHEN         | WHO                  | WHAT                                            |
| 11:50        | @everyone            | příchod                                         |
| 11:56        | @Zuzana              | úvod                                            |
| 13:00        | @danielmstc @hellboi | #agdx-irl (agdx-report)                         |
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

        self.hh_mm_format = "%H:%M"

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
            self.update_intervals()
        # if a new item has rung, update the ui
        # if there is no interval lef, also update the ui
        else:
            self.update_intervals()
        # update the clock
        self.update_clock()

    
    def update_intervals(self):
        # now block stylesheet
        now_block_stylesheet = "QWidget {\n	color: #FFFFFF;\n	background-color: #2B2B2B;\n	border-radius: 20px;\n}"
        # now pause stylesheet
        now_pause_styleheet = "QWidget {\n	color: #000000;\n	background-color: #FFFFFF;\n	border-radius: 20px;\n}"
        # next block stylesheet
        next_block_stylesheet = "QWidget {\n	color: #FFFFFF;\n	background-color: #2B2B2B;\n	border-radius: 20px;\n}"
        # next paues stylesheet
        next_pause_stylesheet = "QWidget {\n	color: #000000;\n	background-color: #FFFFFF;\n	border-radius: 20px;\n}"

        # upłdate the current_interval
        current_interval = self.bell.get_current_interval()
        if current_interval == False:
                self.now_start_end.setText("00-00")
                self.now_who.setText("@everyone")
                self.now_what.setText("nothing")
                self.now.setStyleSheet(now_pause_styleheet)
        else:
            self.now_start_end.setText(current_interval.start_time.strftime(self.hh_mm_format) + "-" + current_interval.end_time.strftime(self.hh_mm_format))
            self.now_who.setText(current_interval.who)
            self.now_what.setText(current_interval.what)
            if current_interval.type == "pause":
                self.now.setStyleSheet(now_pause_styleheet)
            else: self.now.setStyleSheet(now_block_stylesheet)
        # update the next_interval
        next_interval = self.bell.get_next_interval()
        if next_interval == False:
            self.next_start_end.setText("00-00")
            self.next_who.setText("@everyone")
            self.next.setStyleSheet(next_pause_stylesheet)
        else:
            self.next_start_end.setText(next_interval.start_time.strftime(self.hh_mm_format) + "-" + next_interval.end_time.strftime(self.hh_mm_format))
            self.next_who.setText(next_interval.who)
            if current_interval.type == "pause":
                self.next.setStyleSheet(next_pause_stylesheet)
            else: self.next.setStyleSheet(next_block_stylesheet)
    
    def update_clock(self):
        self.clock.setText(datetime.datetime.now().strftime(self.hh_mm_format))



# LAUNCH
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
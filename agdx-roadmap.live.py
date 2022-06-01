import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer, QStandardPaths

from window import Ui_MainWindow
from logic import *

## DATA
harmonogram_path = "/Users/admin/Library/Application Support/agdx-roadmap.live/harmonogram.json"

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
| 13:40        | @v.adela             | myšlenky o textu (agdx-project)                 |
| 14:10        | @Ondřej              | typo report (agdx-project)                      |
| 14:40        | @everyone            | pauza (10min)                                   |
| 14:50        | @JakubS              | web Duholeum - generátor                        |
| 15:20        | @FlyingMochi         | VR podcast                                      |
| 15:50        | @everyone            | pauza (10min)                                   |
| 16:00        | @everyone            | diskuse o sebahodnocení                         |

"""
if load_harmonogram(harmonogram_path):
    harmonogram = load_harmonogram(harmonogram_path)
else:
    harmonogram = md2harmonogram(tabulka)
    save_harmonogram(harmonogram, harmonogram_path)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.bell = bell(harmonogram)

        self.delay.clicked.connect(self.delay_ten)

        self.hh_mm_format = "%H:%M"

        # creating a timer object
        timer = QTimer(self)
        # adding action to timer
        timer.timeout.connect(self.tick)
        # update the timer every second
        timer.start(1000)

        self.pause_messages = [
            "walk around a bit :)",
            "have a coffee :)",
            "close your eyes and listen :)",
            "do nothing :)",
            "strech your body :)"
        ]

        self.update_intervals()

    
    def tick(self):
        # update the clock
        self.update_clock()
        self.update_slider()
        if type(self.bell.arm()) == interval:
            self.update_intervals()
    
    def update_intervals(self):
        # now block stylesheet
        now_block_stylesheet = "QWidget {\n	color: #FFFFFF;\n	background-color: #2B2B2B;\n	border-radius: 20px;\n}"
        # now pause stylesheet
        now_pause_styleheet = "QWidget {\n	color: #000000;\n	background-color: #FFFFFF;\n	border-radius: 20px;\n}"
        # next block stylesheet
        next_block_stylesheet = "QWidget {\n	color: #FFFFFF;\n	background-color: #2B2B2B;\n	border-radius: 20px;\n}"
        # next paues stylesheet
        next_pause_stylesheet = "QWidget {\n	color: #000000;\n	background-color: #FFFFFF;\n	border-radius: 20px;\n}"

        # update the current_interval
        current_interval = self.bell.get_current_interval()
        # if there is no current interval
        if current_interval == False:
                self.now_start_end.setText("00 – 00")
                self.now_who.setText("@everyone")
                self.now_what.setText(random.choice(self.pause_messages))
                self.now.setStyleSheet(now_pause_styleheet)
        # there is a current interval
        else:
            # general
            self.now_start_end.setText(current_interval.start_time.strftime(self.hh_mm_format) + " – " + current_interval.end_time.strftime(self.hh_mm_format))
            self.now_who.setText(current_interval.who)
            self.now_what.setText(current_interval.what)
            # pause
            if current_interval.type == "pause":
                self.now.setStyleSheet(now_pause_styleheet)
                if current_interval.what == "p\u0159\u00edchod":
                    self.now_who.setText(current_interval.what)
                else:
                    self.now_who.setText("pause")
                self.now_what.setText(random.choice(self.pause_messages))
            # block
            else: 
                self.now.setStyleSheet(now_block_stylesheet)
                self.now_who.setText(current_interval.who)
                self.now_what.setText(current_interval.what)
        # update the next_interval
        next_interval = self.bell.get_next_interval()
        if next_interval == False:
            self.next_start_end.setText("00 – 00")
            self.next_who.setText("@everyone")
            self.next.setStyleSheet(next_pause_stylesheet)
        else:
            self.next_start_end.setText(next_interval.start_time.strftime(self.hh_mm_format) + " – " + next_interval.end_time.strftime(self.hh_mm_format))
            self.next_who.setText(next_interval.who)
            if next_interval.type == "pause":
                self.next.setStyleSheet(next_pause_stylesheet)
            else: self.next.setStyleSheet(next_block_stylesheet)
    
    def update_clock(self):
        self.clock.setText(datetime.now().strftime(self.hh_mm_format))

    def update_slider(self):
        current_time = datetime.now()
        current_interval = self.bell.get_current_interval()
        # if there isnt a current interval
        if type(current_interval) == bool:
            self.progressBar.setValue(0)
            return
        # if there is a current interval
        hundred_delta = current_interval.end_time - current_interval.start_time
        delta = self.bell.get_current_interval().end_time - current_time
        x = delta.seconds / hundred_delta.seconds
        value = 100 - x * 100
        if value < 6:
            value = 6
        self.progressBar.setValue(int(value))
    
    def delay_ten(self):
        print("delay")



# LAUNCH
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
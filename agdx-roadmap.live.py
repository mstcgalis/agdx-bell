import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer

from window import Ui_MainWindow
from logic import *

## DATA
harmonogram_path = os.path.normpath("data/harmonogram.json")

tabulka = """| ŠTVRTOK 1.6. |                      |                                                 |
| ------------ | -------------------- | ----------------------------------------------- |
| WHEN         | WHO                  | WHAT                                            |
| 18:10        | @everyone            | příchod                                         |
| 18:20        | @Zuzana              | úvod                                            |
| 18:30        | @danielmstc @hellboi | #agdx-irl (agdx-report)                         |
| 18:35        | @honza_suchy         | Untitled menu app (agdx-project)                |
| 18:40        | @everyone            | pauza (10min)                                   |
| 19:00        | @petr                | KAM (agdx-project)                              |

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
                self.now_start_end.setText("00-00")
                self.now_who.setText("@everyone")
                self.now_what.setText(random.choice(self.pause_messages))
                self.now.setStyleSheet(now_pause_styleheet)
        # there is a current interval
        else:
            # general
            self.now_start_end.setText(current_interval.start_time.strftime(self.hh_mm_format) + "-" + current_interval.end_time.strftime(self.hh_mm_format))
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
            self.next_start_end.setText("00-00")
            self.next_who.setText("@everyone")
            self.next.setStyleSheet(next_pause_stylesheet)
        else:
            self.next_start_end.setText(next_interval.start_time.strftime(self.hh_mm_format) + "-" + next_interval.end_time.strftime(self.hh_mm_format))
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


# LAUNCH
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
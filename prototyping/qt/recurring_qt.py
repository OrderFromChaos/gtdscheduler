from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QMainWindow
)
from PyQt5.QtGui import (
    QColor
)
from PyQt5.QtCore import (
    QTimer,
    Qt,
    QThread
)
import sys
import time


# Use this:
# https://pythonspot.com/pyqt5-colors/


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'recurring'
        self.frame = 0
        self.initUI()

    def initUI(self):
        # Set up
        self.setWindowTitle(self.title)
        self.setAutoFillBackground(True)

        # Draw task
        self.taskarray = [
            ['Task 1', 'Task 2', 'Task 3', 'Task 4'],
            ['Task 5', 'Task 6', 'Task 7', 'Task 8'],
            ['Task 9', 'Task 10', 'Task 11', 'Task 12'],
            ['Task 13', 'Task 14', 'Task 15', 'Task 16']
        ]


        self.show()
        while True:
            self.draw()


    def draw(self):
        if self.frame == 0:
            # Create task grid
            self.verts = QVBoxLayout()
            horiz = []
            self.button_objs = []
            for taskrow in self.taskarray:
                horiz.append(QHBoxLayout()) # TODO: Keep inside a vert into a horiz instead; vertical breaks are less annoying than horizontal breaks
                curr_UI_row = horiz[-1]
                for taskname in taskrow:
                    button = QPushButton(taskname)


                    self.button_objs.append(button)
                    curr_UI_row.addWidget(button)
                self.verts.addLayout(curr_UI_row)

            # Draw onto existing window
            self.window = QWidget(self)
            self.setCentralWidget(self.window)

        for button in self.button_objs:
            if self.frame % 100 <= 50:
                button.setStyleSheet(
                    'background-color: green'
                )
            else:
                button.setStyleSheet(
                    'background-color: yellow'
                )

        self.window.setLayout(self.verts)

        self.frame += 1


    #     QTimer.singleShot(1, self.go)

    def go(self):
        print('Entered go')
        # https://stackoverflow.com/questions/1386043/how-to-make-qt-work-when-main-thread-is-busy
        while True:

            print('Loop')
            for button in self.button_objs:
                button.setStyleSheet(
                    'background-color: yellow'
                )
            # QThread.msleep(500)


if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())

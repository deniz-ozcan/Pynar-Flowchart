
from sys import argv, exit
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QCheckBox
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
)
from PyQt5.QtCore import (
    Qt,
    QPropertyAnimation,
    QEasingCurve,
)
from debug import Ui_Debug
from os.path import join, dirname, expanduser
from os import system, sep
from threading import Thread
from pathlib import Path
import pdb


class RunThread(Thread):

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        system(self.command)

# pyuic5 C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\debug.ui -o C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\debug.py
# pyrcc5 C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\icons.qrc -o C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\icons_rc.py


class MainWindow(QMainWindow, Ui_Debug):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.codeToShow()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.closeBut.clicked.connect(self.close)
        self.minimize.clicked.connect(self.restoreOrMaximized)
        self.downBut.clicked.connect(self.showMinimized)
        self.header.mouseMoveEvent = self.moveWindow
        self._1step.clicked.connect(lambda: self.sendCommand("n"))
        self._2intofunc.clicked.connect(lambda: self.sendCommand("s"))
        self._3fromfunc.clicked.connect(lambda: self.sendCommand("r"))
        self._4execution.clicked.connect(lambda: self.sendCommand("c"))
        self._5help.clicked.connect(self.helpMenu)
        self.sendButton.clicked.connect(
            lambda: self.sendCommand(self.comline.text()))

    def codeToShow(self):
        file_path = join(dirname(__file__), "./x.py")
        with open(file_path, 'r') as fp:
            for i in range(0, len(fp.readlines())):
                self.i = QCheckBox(self.breakpoints)
                self.i.setObjectName(f"checkBox{i}")
                self.i.setText(str(i+1))
                self.verticalLayout_4.addWidget(self.i)
        self.codestext.setText(open(file_path).read())
        self.q1 = QCheckBox(self.breakpoints)
        self.q1.setObjectName("q1")
        self.verticalLayout_4.addWidget(self.q1)
        self.q2 = QCheckBox(self.breakpoints)
        self.q2.setObjectName(f"q2")
        self.verticalLayout_4.addWidget(self.q2)
        self.q1.setCheckable(False)
        self.q2.setCheckable(False)
        pypath = "C:/Users/sauda/AppData/Local/Programs/Python/Python310/python.exe"
        filepath = "c:/Users/sauda/Masaüstü/SOFTWARE/WINDOWS/PyNar/ZDebug/x.py"
        command = pypath+" -m pdb "+filepath
        pdbrc_file_path = Path(expanduser("~") + sep + ".pdbrc")
        pdbrc_file_content = """
-------------------------------------------------
|    iLK {0} SATIR CALISTI...                   |
|    DEVAM iCiN enter TUSUNA BASINIZ.           |
|    CIKIS iCiN q TUSUNA BASINIZ.               |
-------------------------------------------------
!(lambda: exec(\'import gc, pdb; next(o for o in gc.get_objects() if isinstance(o, pdb.Pdb)).prompt = \">> \"\',##))()
b {1}
!print('=================PROGRAM CIKTISI=================')
{2}
!print(m)
"""
        breakpointLine = 3
        with open(pdbrc_file_path, 'w', encoding='utf-8') as file:
            file.write(pdbrc_file_content.format(breakpointLine-1, breakpointLine,
                       'c' if breakpointLine != 1 else '').replace('##', '{}'))
            self.cmdtext.setText(pdbrc_file_content.format(
                breakpointLine-1, breakpointLine, 'c' if breakpointLine != 1 else '').replace('##', '{}'))
        thread = RunThread(command)
        thread.start()

    def sendCommand(self, _com):
        if(_com == "n" or _com == "s" or _com == "r" or _com == "c"):
            thread = RunThread(_com)
            thread.start()
        elif(len(_com) > 2):
            thread = RunThread(_com)
            thread.start()
        else:
            pass

    def moveWindow(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

    def helpMenu(self):
        width = self.helpframe.maximumWidth()
        if width == 0:
            newWidth = 240
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.helpframe, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def restoreOrMaximized(self):
        if self.isMaximized():
            self.showNormal()
            icon9 = QIcon()
            icon9.addPixmap(
                QPixmap(":/icons/icons/Zres2.svg"), QIcon.Normal, QIcon.Off
            )
            self.minimize.setIcon(icon9)
        else:
            self.showMaximized()
            icon9 = QIcon()
            icon9.addPixmap(
                QPixmap(":/icons/icons/Zres1.svg"), QIcon.Normal, QIcon.Off
            )
            self.minimize.setIcon(icon9)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())

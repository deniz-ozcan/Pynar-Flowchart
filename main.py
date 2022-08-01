from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QTextEdit,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import (
    QMetaObject,
    QSize,
    Qt,
)
from sys import exit,argv

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.showNormal()
        self.console.insertPlainText = self.__insert_plain_text

    def __insert_plain_text(self, message):
        if message.startswith('step') or message.startswith('next') or message.startswith('return') or message.startswith('continue'):
            self.console.setTextColor(Qt.GlobalColor.cyan)
        elif message.startswith('***'):
            self.console.setTextColor(Qt.GlobalColor.red)
        else:
            self.console.setTextColor(Qt.GlobalColor.magenta)
        QTextEdit.insertPlainText(self.console, message)
        self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())

    def setupUi(self, Debug):
        Debug.setObjectName(u"Debug")
        Debug.resize(765, 465)
        Debug.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(Debug)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 400))
        self.centralwidget.setStyleSheet(u"*{border: none;color:white;}#centralwidget{border-radius:5px;background-color:#fff;}#console{border-radius:6px;background-color:#1e1e1e;}#cmdframe{background-color:#1e1e1e;border-radius:6px;}QScrollBar:vertical {border-radius: 5px;background:transparent;width:10px;margin:0px;}QPushButton{border:1 px solid #0d6efd;background-color:#0d6efd;color:rgb(255,255,255);font: 700 12pt \"Segoe UI\";}QPushButton:hover{background-color:#0b5ed7;}#butstep{border-top-left-radius:6px;border-bottom-left-radius:6px;}#butcontinue{border-top-right-radius:6px;border-bottom-right-radius:6px;}QScrollBar::handle:vertical {border-radius: 5px;background: #88888888;min-width:5px;max-width:5px;min-height:50px;max-height:50px;width:5px;height:5px;}QScrollBar::handle:vertical:hover {background: #888888;}QScrollBar::add-line:vertical {height: 0px;subcontrol-position: bottom;	subcontrol-origin: margin;}QScrollBar::sub-line:vertical {height: 0px;subcontrol-position: top;subcontrol-origin: margin;}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background:transparent;}QScrollBar:horizontal {border-radius: 5px;background:transparent;height:10px;margin:0px;}QScrollBar::handle:horizontal {border-radius: 5px;background: #88888888;min-width:50px;max-width:50px;min-height:5px;max-height:5px;width:5px;height:5px;}QScrollBar::handle:horizontal:hover {background: #888888;}QScrollBar::add-line:horizontal {height: 0px;subcontrol-position: bottom;	subcontrol-origin: margin;}QScrollBar::sub-line:horizontal {height: 0px;subcontrol-position: top;subcontrol-origin: margin;}QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {background:transparent;}")
        self.centlay = QVBoxLayout(self.centralwidget)
        self.centlay.setObjectName(u"centlay")
        self.butgro = QFrame(self.centralwidget)
        self.butgro.setObjectName(u"butgro")
        self.butgro.setMinimumSize(QSize(290, 40))
        self.butgro.setMaximumSize(QSize(290, 40))
        self.butgro.setFrameShape(QFrame.StyledPanel)
        self.butgro.setFrameShadow(QFrame.Raised)
        self.butlay = QHBoxLayout(self.butgro)
        self.butlay.setSpacing(0)
        self.butlay.setObjectName(u"butlay")
        self.butlay.setContentsMargins(0, 0, 0, 0)
        self.butstep = QPushButton(self.butgro)
        self.butstep.setObjectName(u"butstep")
        self.butstep.setMinimumSize(QSize(70, 35))
        self.butstep.setMaximumSize(QSize(70, 35))
        self.butstep.clicked.connect(lambda: self.console.insertPlainText("step "))
        self.butstep.setText("Step")
        self.butstep.setToolTip("<p><span style=\" color:#0d6efd;\">Mevcut seviyede kalarak bir sonraki sat\u0131ra ge\u00e7in. </span></p>")
        self.butlay.addWidget(self.butstep)        
        self.butnext = QPushButton(self.butgro)
        self.butnext.setObjectName(u"butnext")
        self.butnext.setMinimumSize(QSize(70, 35))
        self.butnext.setMaximumSize(QSize(70, 35))
        self.butnext.clicked.connect(lambda: self.console.insertPlainText("next "))
        self.butnext.setToolTip("<p><span style=\" color:#0d6efd;\">Bir sonraki sat\u0131ra ge\u00e7in ve varsa bir i\u015fleve ge\u00e7in.  </span></p>")
        self.butnext.setText("Next")
        self.butlay.addWidget(self.butnext)        
        self.butreturn = QPushButton(self.butgro)
        self.butreturn.setObjectName(u"butreturn")
        self.butreturn.setMinimumSize(QSize(70, 35))
        self.butreturn.setMaximumSize(QSize(70, 35))
        self.butreturn.setToolTip("<p><span style=\" color:#0d6efd;\">Ge\u00e7erli i\u015flevden \u00e7\u0131k\u0131n.</span></p>")
        self.butreturn.setText("Return")
        self.butreturn.clicked.connect(lambda: self.console.insertPlainText("return "))
        self.butlay.addWidget(self.butreturn)
        self.butcontinue = QPushButton(self.butgro)
        self.butcontinue.setObjectName(u"butcontinue")
        self.butcontinue.setMinimumSize(QSize(80, 35))
        self.butcontinue.setMaximumSize(QSize(80, 35))
        self.butcontinue.setToolTip("<p><span style=\" color:#0d6efd;\">Y\u00fcr\u00fctmeye devam edin.</span></p>")
        self.butcontinue.setText("Continue")
        self.butcontinue.clicked.connect(lambda: self.console.insertPlainText("continue "))
        self.butlay.addWidget(self.butcontinue)
        self.centlay.addWidget(self.butgro)
        self.cmdframe = QFrame(self.centralwidget)
        self.cmdframe.setObjectName(u"cmdframe")
        self.cmdframe.setFrameShape(QFrame.StyledPanel)
        self.cmdframe.setFrameShadow(QFrame.Raised)
        self.cmdlay = QHBoxLayout(self.cmdframe)
        self.cmdlay.setSpacing(0)
        self.cmdlay.setObjectName(u"cmdlay")
        self.cmdlay.setContentsMargins(0, 0, 0, 0)
        self.centlay.addWidget(self.cmdframe)
        self.console = QTextEdit()
        self.console.setStyleSheet("border-radius:6px;background-color:#1e1e1e;color:white;font: 400 10pt 'Segoe UI';")
        self.cmdlay.addWidget(self.console)
        Debug.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(Debug)
        Debug.setWindowTitle("Debugger")

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())

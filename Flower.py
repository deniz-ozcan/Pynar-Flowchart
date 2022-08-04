from pyflowchart import Flowchart
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget
)
from PyQt5.QtCore import (
    Qt,QPropertyAnimation,QEasingCurve,
    QUrl,QMetaObject,QSize, Qt
)
from PyQt5.QtGui import (
    QPixmap,QIcon,QFont,
    QPageSize,QPageLayout,QCursor
)

import icons
from PyQt5 import QtWebEngineWidgets as web
from sys import exit, argv
from os.path import dirname, join, abspath
# pyrcc5 icons.qrc -o icons_rc.py
# pyuic5 builder.ui -o builder.py


class Ui_Builder(object):
    def setupUi(self, Builder):
        Builder.setObjectName("Builder")
        Builder.resize(807, 580)
        Builder.setMinimumSize(QSize(807, 580))
        Builder.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/icons/download.svg"),
                       QIcon.Normal, QIcon.Off)
        Builder.setWindowIcon(icon)
        self.centralwidget = QWidget(Builder)
        font = QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("*{border: none;color:white;}#centralwidget,#htmlview{background-color:qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 rgba(112.520718,44.062154,249.437846,255),stop: 1 rgba(112.520718,44.062154,249.437846,242.25));}QLineEdit{border: 1px solid black;max-width:180px;min-width:180px;text-align: center;font-size:15px;color:black;padding: 1px;border-radius: 7px;background: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fff,stop: 0.4999 #eee,stop: 0.5 #ddd,stop: 1 #eee );width: 15px;}QLineEdit:hover{background-color: #ff0088;}QPushButton{border: 1px solid black;max-width:60px;min-width:60px;text-align: center;font: 12pt \"Segoe UI\";color:black;padding: 1px;border-radius: 7px;background-color: #00ff88;}QPushButton:hover,#output:hover,#save:hover{background-color:#007fff;color:white;border-color:white;}#output,#save{border-radius:0px;border:none;}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._1leftMenu = QFrame(self.centralwidget)
        self._1leftMenu.setMaximumSize(QSize(0, 16777215))
        self._1leftMenu.setObjectName("_1leftMenu")
        self.verticalLayout = QVBoxLayout(self._1leftMenu)
        self.verticalLayout.setContentsMargins(8, 40, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_75 = QFrame(self._1leftMenu)
        self.frame_75.setMinimumSize(QSize(200, 0))
        self.frame_75.setObjectName("frame_75")
        self.verticalLayout_85 = QVBoxLayout(self.frame_75)
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_85.setSpacing(10)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.outlabel = QLabel(self.frame_75)
        self.outlabel.setMinimumSize(QSize(200, 40))
        self.outlabel.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.outlabel.setFont(font)
        self.outlabel.setAlignment(Qt.AlignCenter)
        self.outlabel.setObjectName("outlabel")
        self.verticalLayout_85.addWidget(self.outlabel)
        self.outputpath = QLineEdit(self.frame_75)
        self.outputpath.setMinimumSize(QSize(184, 30))
        self.outputpath.setObjectName("outputpath")
        self.verticalLayout_85.addWidget(self.outputpath)
        self.browsebut = QPushButton(self.frame_75)
        self.browsebut.setMinimumSize(QSize(64, 30))
        self.browsebut.setMaximumSize(QSize(64, 30))
        self.browsebut.setFont(font)
        self.browsebut.setCursor(QCursor(Qt.PointingHandCursor))
        self.browsebut.setObjectName("browsebut")
        self.verticalLayout_85.addWidget(self.browsebut, 0, Qt.AlignHCenter)
        self.verticalLayout.addWidget(
            self.frame_75, 0, Qt.AlignHCenter | Qt.AlignTop)
        self.horizontalLayout.addWidget(self._1leftMenu)
        self.general = QWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.general.sizePolicy().hasHeightForWidth())
        self.general.setSizePolicy(sizePolicy)
        self.general.setObjectName("general")
        self.horizontalLayout_2 = QHBoxLayout(self.general)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QFrame(self.general)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setMinimumSize(QSize(62, 0))
        self.output.setFont(font)
        self.output.setCursor(QCursor(Qt.PointingHandCursor))
        self.output.setObjectName("output")
        self.verticalLayout_2.addWidget(self.output)
        self.save = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMinimumSize(QSize(62, 0))
        self.save.setFont(font)
        self.save.setCursor(QCursor(Qt.PointingHandCursor))
        self.save.setObjectName("save")
        self.verticalLayout_2.addWidget(self.save)
        self.horizontalLayout_2.addWidget(self.frame)
        self.htmlview = QFrame(self.general)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.htmlview.sizePolicy().hasHeightForWidth())
        self.htmlview.setSizePolicy(sizePolicy)
        self.htmlview.setObjectName("htmlview")
        self.horizontalLayout_3 = QHBoxLayout(self.htmlview)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addWidget(self.htmlview)
        self.horizontalLayout.addWidget(self.general)
        Builder.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(Builder)
        Builder.setWindowTitle("Pynar Flowchart")
        self.outlabel.setText("Output Directory")
        self.outputpath.setText("C:\\")
        self.browsebut.setText("Browse")
        self.output.setText("Output")
        self.save.setText("Save")


class Browser(web.QWebEngineView):

    def __init__(self, html):
        super().__init__()
        here = dirname(abspath(__file__)).replace('\\', '/')
        base_path = join(dirname(here), 'dummy').replace('\\', '/')
        self.url = QUrl('file:///' + base_path)
        self.page().setHtml(html, baseUrl=self.url)


class Web_Builder(QMainWindow, Ui_Builder):
    htmlpage = open(join(dirname(__file__), "./index.html"),
                    encoding="utf-8").read()
    htmlend = """
        </textarea>
    <button id="run" type="button">Run</button>
</div>
<div class="preview-area" id="canvas"></div>
</body>
</html>
    """

    def __init__(self):
        super(Web_Builder, self).__init__()
        self.setupUi(self)
        self.openHtlm()
        self.output.clicked.connect(self.openClose)
        self.browsebut.clicked.connect(self.browse_folder)
        self.save.clicked.connect(self.saveFile)
        self.outputpath.setText(dirname(__file__))

    def openHtlm(self):
        file_path = join(dirname(__file__), "./test.py")
        with open(file_path) as f:
            code = f.read()
        fc = Flowchart.from_code(code).flowchart()
        self.browser = Browser(Web_Builder.htmlpage +str(fc)+Web_Builder.htmlend)
        self.horizontalLayout_3.addWidget(self.browser)

    def saveFile(self):
        try:
            pagelay = QPageLayout()
            pagelay.setPageSize(QPageSize(QPageSize.PageSizeId.B0))
            pagelay.setMode(QPageLayout.Mode.FullPageMode)
            self.browser.page().printToPdf(self.outputpath.text() +"/flowchart.pdf", pageLayout=pagelay)
        except Exception as e:
            print(e)
            print("Error: Could not save file")
            exit(1)

    def openClose(self):
        width = self._1leftMenu.maximumWidth()
        if width == 0:
            newWidth = 240
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self._1leftMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def browse_folder(self):
        self.outputpath.setText(
            abspath(QFileDialog.getExistingDirectory(self, "Select Output Directory")))


if __name__ == "__main__":
    app = QApplication(argv)
    Form = Web_Builder()
    Form.show()
    exit(app.exec_())

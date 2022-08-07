from pyflowchart import Flowchart
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QFrame, QHBoxLayout, QWidget, QAction, QMenuBar, QToolBar, QStatusBar, QMenu
from PyQt5.QtCore import Qt, QUrl, QMetaObject, QSize, Qt, QRect
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPageSize, QPageLayout
import icons_rc
from PyQt5 import QtWebEngineWidgets as web
from sys import exit, argv
from os.path import dirname, join, abspath

# pyrcc5 icons.qrc -o icons_rc.py
# pyuic5 builder.ui -o builder.py


class Ui_Builder(object):
    def setupUi(self, Builder):
        Builder.setObjectName("Builder")
        Builder.resize(1066, 572)
        Builder.setMinimumSize(QSize(1050, 570))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/icons/flowchart.png"),
                       QIcon.Normal, QIcon.Off)
        Builder.setWindowIcon(icon)
        self.centralwidget = QWidget(Builder)
        self.centralwidget.setMinimumSize(QSize(1050, 570))
        font = QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.view = QFrame(self.centralwidget)
        self.view.setFrameShape(QFrame.StyledPanel)
        self.view.setFrameShadow(QFrame.Raised)
        self.view.setObjectName("view")
        self.horizontalLayout.addWidget(self.view)
        Builder.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Builder)
        self.menuBar.setGeometry(QRect(0, 0, 1066, 22))
        self.menuBar.setObjectName("menuBar")
        self.filemenu = QMenu(self.menuBar)
        self.filemenu.setObjectName("filemenu")
        self.helpmenu = QMenu(self.menuBar)
        self.helpmenu.setObjectName("helpmenu")
        Builder.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(Builder)
        self.statusBar.setObjectName("statusBar")
        Builder.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(Builder)
        self.toolBar.setMinimumSize(QSize(0, 40))
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setIconSize(QSize(40, 40))
        self.toolBar.setStyleSheet("QToolBar { border: 0px }QToolButton:hover{ background-color: transparent;margin-left:2px;margin-bottom:2px; }QToolButton:pressed{ background-color: transparent; }")
        Builder.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.savebut = QAction(Builder)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/icons/save.png"),QIcon.Normal, QIcon.Off)
        self.savebut.setIcon(icon1)
        self.savebut.setObjectName("savebut")
        self.magnifyplus = QAction(Builder)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icons/icons/yakın.png"),QIcon.Normal, QIcon.Off)
        self.magnifyplus.setIcon(icon2)
        self.magnifyplus.setObjectName("magnifyplus")
        self.magnifyminus = QAction(Builder)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icons/icons/uzak.png"),QIcon.Normal, QIcon.Off)
        self.magnifyminus.setIcon(icon3)
        self.magnifyminus.setObjectName("magnifyminus")
        self.menuBar.addAction(self.filemenu.menuAction())
        self.menuBar.addAction(self.helpmenu.menuAction())
        self.toolBar.addAction(self.savebut)
        self.toolBar.addAction(self.magnifyplus)
        self.toolBar.addAction(self.magnifyminus)
        QMetaObject.connectSlotsByName(Builder)
        Builder.setWindowTitle("Pynar Flowchart")
        self.filemenu.setTitle("Dosya")
        self.helpmenu.setTitle("Yardım")
        self.toolBar.setWindowTitle("toolBar")
        self.savebut.setText(" ")
        self.savebut.setToolTip("Kaydet")
        self.savebut.setShortcut("Ctrl+S")
        self.magnifyplus.setText(" ")
        self.magnifyplus.setToolTip("Yakınlaştır")
        self.magnifyplus.setShortcut("Ctrl++")
        self.magnifyminus.setText(" ")
        self.magnifyminus.setToolTip("Uzaklaştır")
        self.magnifyminus.setShortcut("Ctrl+-")
        self.exitact.setText("Çıkış")

class Browser(web.QWebEngineView):

    def __init__(self, html=""):
        super().__init__()
        here = dirname(abspath(__file__)).replace('\\', '/')
        base_path = join(dirname(here), 'dummy').replace('\\', '/')
        self.url = QUrl('file:///' + base_path)
        self.setHtml(html, baseUrl=self.url)


class Web_Builder(QMainWindow, Ui_Builder):
    def __init__(self):
        super(Web_Builder, self).__init__()
        self.setupUi(self)
        self.openTab()
        self.savebut.triggered.connect(self.saveFile)
        self.toolBar.setMovable(False)
        self.magnifyplus.triggered.connect(self.magnifypluser)
        self.magnifyminus.triggered.connect(self.magnifyminuser)
        self.exitact.triggered.connect(self.close)

    def openTab(self):
        self.horizontalLayout_2 = QHBoxLayout(self.view)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        htmlstart,htmlmid,htmlend = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>flowchart.js · Playground</title><style type="text/css">.start-element { fill : #d594f4; }.end-element { fill : #00FF55; }.condition-element { fill : #ffa0ea; }.inputoutput-element { fill : #55FFFF; }.operation-element { fill : #FFFF99; }.subroutine-element { fill : #a0e0ff; }.parallel-element { fill : #FFCCFF; }#code{display: none;}::-webkit-scrollbar {display:block;}::-webkit-scrollbar-thumb {border:1px solid #60a0e0;background: #c0e0ff;}::-webkit-scrollbar-thumb:hover {background: #00ffff;}</style><script src="flowchart.js"></script>""", """<script>window.onload = function () {var code = document.getElementById("code").value,chart;if (chart) {chart.clean();}chart = flowchart.parse(code);chart.drawSVG('canvas', {'x': 200,'y': 5,'roundness': 5,"arrow-end": "diamond",'line-width': 1,'maxWidth': 80,'line-length': 40,'text-margin': 15,'font-size': 11,'font': 'normal','font-family': 'Arial','font-weight': 'normal','font-color': 'black','line-color': 'black','element-color': 'black','fill': 'white','yes-text': 'Doğru','no-text': 'Yanlış','scale': 1,'symbols': {'start': {'font-color': 'black','element-color': 'green','class': 'start-element' },'end':{'class': 'end-element'},'condition': {'class': 'condition-element'},'inputoutput': {'class': 'inputoutput-element'},'operation': {'class': 'operation-element'},'subroutine': {'class': 'subroutine-element'},'parallel': {'class': 'parallel-element'}},'flowstate' : {'past' : { 'fill' : '#CCCCCC', 'font-size' : 12},'current' : {'fill' : 'yellow', 'font-color' : 'red', 'font-weight' : 'bold'},'future' : { 'fill' : '#FFFF99'},'request' : { 'fill' : 'blue'},'invalid': {'fill' : '#444444'},'approved' : { 'fill' : '#58C4A3', 'font-size' : 12, 'yes-text' : 'APPROVED', 'no-text' : 'n/a' },'rejected' : { 'fill' : '#C45879', 'font-size' : 12, 'yes-text' : 'n/a', 'no-text' : 'REJECTED' }}});};</script></head><body><div><textarea id="code" style="width: 100%;" rows="11">""","</textarea></div><div id='canvas'></div></body></html>"
        jsfile = open(join(dirname(__file__), "./flowchart.js"),encoding="utf-8").read()
        file_path = join(dirname(__file__), "./test.py")
        with open(file_path) as f:
            code = f.read()
        fc = Flowchart.from_code(code).flowchart().replace(' start ', ' Başla ').replace('end function return', 'Fonksiyon Sonu').replace(' end ', ' Son ').replace(' output: ', ' Çıktı: ').replace(' input: ', ' Girdi: ')
        self.browser = Browser(htmlstart+"<script>\n" +jsfile+"</script>\n"+htmlmid + str(fc) + htmlend)
        self.statusBar.showMessage("Dosya açıldı", 2000)
        self.horizontalLayout_2.addWidget(self.browser)

    def magnifypluser(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def magnifyminuser(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)

    def saveFile(self):
        pagelay = QPageLayout()
        pagelay.setPageSize(QPageSize(QPageSize.PageSizeId.B0))
        pagelay.setMode(QPageLayout.Mode.FullPageMode)
        try:
            self.browser.page().printToPdf(abspath(QFileDialog.getExistingDirectory(
                self, "Hedef Klasör Seçiniz"))+"/flowchart.pdf", pageLayout=pagelay)
            self.statusBar.showMessage("Dosya Kaydedildi", 2000)
        except Exception as e:
            self.statusBar.showMessage("Dosya Kaydedilemedi", 2000)


if __name__ == "__main__":
    app = QApplication(argv)
    Form = Web_Builder()
    Form.show()
    exit(app.exec_())

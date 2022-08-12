from pyflowchart import Flowchart
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QFrame, QHBoxLayout, QWidget, QAction, QMenuBar, QToolBar, QStatusBar, QMenu, QTabWidget, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QUrl, QMetaObject, QSize, Qt, QRect,QTimer
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPageSize, QPageLayout, QMovie
import icons_rc
from PyQt5 import QtWebEngineWidgets as web
from sys import exit, argv
from os.path import dirname, join, abspath, exists
from platform import system
from os import environ, makedirs
from subprocess import check_output


class Browser(web.QWebEngineView):

    def __init__(self, html=""):
        super().__init__()
        here = dirname(abspath(__file__)).replace('\\', '/')
        base_path = join(dirname(here), 'dummy').replace('\\', '/')
        self.url = QUrl('file:///' + base_path)
        self.setHtml(html, baseUrl=self.url)


class FlowchartMaker(QMainWindow):
    pagewidth = 0
    pageheight = 0

    def __init__(self):
        super(FlowchartMaker, self).__init__()
        self.setupUi(self)
        self.openTab()
        self.savebut.triggered.connect(self.saveFile)
        self.toolBar.setMovable(False)
        self.magnifyplus.triggered.connect(self.magnifypluser)
        self.magnifyminus.triggered.connect(self.magnifyminuser)
        self.exitact.triggered.connect(self.close)
        self.defhome.triggered.connect(self.defhomepage)
        self.grabpage.triggered.connect(self.grabcursor)
        self.browser.loadFinished.connect(self.onLoadFinished)
        self.movie = QMovie(":/icons/icons/flowchart.gif")
        self.label = QLabel()
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setObjectName("lb1")
        self.label.setMovie(self.movie)
        self.loading = QMessageBox()
        self.loading.layout().addWidget(self.label)
        self.loading.layout().setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.loading.setWindowFlags(Qt.FramelessWindowHint)
        self.loading.setAttribute(Qt.WA_TranslucentBackground)
        self.loading.setStandardButtons(QMessageBox.NoButton)

    def setupUi(self, Builder):
        Builder.setObjectName("Builder")
        Builder.resize(1066, 572)
        Builder.setMinimumSize(QSize(1050, 570))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/icons/flowchart.png"),QIcon.Normal, QIcon.Off)
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
        self.defhome = QAction(Builder)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/icons/defhome.png"),QIcon.Normal, QIcon.Off)
        self.defhome.setIcon(icon4)
        self.defhome.setObjectName("defhome")
        self.grabpage = QAction(Builder)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/icons/icons/grab.png"),QIcon.Normal, QIcon.Off)
        self.grabpage.setIcon(icon5)
        self.grabpage.setObjectName("grabpage")
        self.menuBar.addAction(self.filemenu.menuAction())
        self.menuBar.addAction(self.helpmenu.menuAction())
        self.toolBar.addAction(self.savebut)
        self.toolBar.addAction(self.magnifyplus)
        self.toolBar.addAction(self.magnifyminus)
        self.toolBar.addAction(self.defhome)
        self.toolBar.addAction(self.grabpage)
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
        self.exitact = QAction(Builder)
        self.exitact.setObjectName("action_k")
        self.filemenu.addAction(self.exitact)
        self.exitact.setText("Çıkış")
        self.tabWidget = QTabWidget(self.view)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("QTabWidget::pane { background: transparent;color: white;}QTabBar::tab{height: 0px;width: 0px;}QTabWidget::tab-bar:top {top: 0px;}QTabWidget::tab-bar:bottom {bottom: 0px;}QTabWidget::tab-bar:left {right: 0px;}QTabWidget::tab-bar:right {left: 0px;}QTabBar::tab:selected {color: white;background: #394b58;}QTabBar::tab:!selected {background: transparent;color: white;}QTabBar::tab:!selected:hover {background: #6b899f;color: black;}QTabBar::tab:top:last, QTabBar::tab:bottom:last,QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {margin-right: 0;}QTabBar::tab:left:last, QTabBar::tab:right:last,QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {margin-bottom: 0;}")
        self.horizontalLayout_2 = QHBoxLayout(self.view)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.tabWidget.setCurrentIndex(-1)
    
    def onLoadFinished(self, ok):
        if ok:
            self.browser.page().runJavaScript("document.getElementsByTagName('svg')[0]['clientWidth'];", self.ready1)
            self.browser.page().runJavaScript("document.getElementsByTagName('svg')[0]['clientHeight'];", self.ready2)

    def ready1(self, width):
        FlowchartMaker.pagewidth += width

    def ready2(self, height):
        FlowchartMaker.pageheight += height

    def openTab(self):
        if(self.tabWidget.currentIndex() >= 0):
            self.closeTab(self.tabWidget.currentIndex())
        self.tab = QWidget()
        self.tab.setObjectName(f"{self.tabWidget.count()}")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget.setCurrentIndex(self.tabWidget.count())
        htmlstart, htmlmid, htmlend = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><style type="text/css">body{ margin:0px;}.start-element { fill : #d594f4; }.end-element { fill : #00FF55; }.condition-element { fill : #ffa0ea; }.inputoutput-element { fill : #55FFFF; }.operation-element { fill : #FFFF99; }.subroutine-element { fill : #a0e0ff; }.parallel-element { fill : #FFCCFF; }#code{display: none;}::-webkit-scrollbar {display:block;}::-webkit-scrollbar-thumb {border:1px solid #60a0e0;background: #c0e0ff;}::-webkit-scrollbar-thumb:hover {background: #00ffff;}</style><script src="flowchart.js"></script>""", """<script>window.onload = function () {var code = document.getElementById("code").value,chart;if (chart) {chart.clean();}chart = flowchart.parse(code);chart.drawSVG('canvas', {'x': 20,'y': 20,'roundness': 5,"arrow-end": "diamond",'line-width': 1,'maxWidth': 80,'line-length': 40,'text-margin': 15,'font-size': 11,'font': 'normal','font-family': 'Arial','font-weight': 'normal','font-color': 'black','line-color': 'black','element-color': 'black','fill': 'white','yes-text': 'Doğru','no-text': 'Yanlış','scale': 1,'symbols': {'start': {'font-color': 'black','element-color': 'green','class': 'start-element' },'end':{'class': 'end-element'},'condition': {'class': 'condition-element'},'inputoutput': {'class': 'inputoutput-element'},'operation': {'class': 'operation-element'},'subroutine': {'class': 'subroutine-element'},'parallel': {'class': 'parallel-element'}},'flowstate' : {'past' : { 'fill' : '#CCCCCC', 'font-size' : 12},'current' : {'fill' : 'yellow', 'font-color' : 'red', 'font-weight' : 'bold'},'future' : { 'fill' : '#FFFF99'},'request' : { 'fill' : 'blue'},'invalid': {'fill' : '#444444'},'approved' : { 'fill' : '#58C4A3', 'font-size' : 12, 'yes-text' : 'APPROVED', 'no-text' : 'n/a' },'rejected' : { 'fill' : '#C45879', 'font-size' : 12, 'yes-text' : 'n/a', 'no-text' : 'REJECTED' }}});};</script></head><body><div><textarea id="code" style="width: 100%;" rows="11">""", "</textarea></div><div id='canvas'></div></body></html>"
        jsfile = open(join(dirname(__file__), "./flowchart.js"),encoding="utf-8").read()
        file_path = join(dirname(__file__), "./test.py")
        with open(file_path) as f:
            code = f.read()
        fc = Flowchart.from_code(code).flowchart().replace(' start ', ' Başla ').replace('end function return', 'Fonksiyon Sonu').replace(' end ', ' Son ').replace(' output: ', ' Çıktı: ').replace(' input: ', ' Girdi: ')
        self.browser = Browser(htmlstart+"<script>\n" +jsfile+"</script>\n"+htmlmid + str(fc) + htmlend)
        self.statusBar.showMessage("Dosya açıldı", 2000)
        self.horizontalLayout_3.addWidget(self.browser)
        self.tabWidget.addTab(self.tab, f"")

    def grabcursor(self):
        if(self.tabWidget.currentIndex() >= 0):
            self.closeTab(self.tabWidget.currentIndex())
        self.tab = QWidget()
        self.tab.setObjectName(f"{self.tabWidget.count()}")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget.setCurrentIndex(self.tabWidget.count())
        htmlstart, htmlmid, htmlend = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><style type="text/css">body{ margin:0px;}#canvas { cursor:move; height:100vh;width:100vw;overflow: auto;}::-webkit-scrollbar { width: 0rem;height: 0rem;}#canvas::-webkit-scrollbar { width: 1rem;height: 1rem;}.start-element { fill : #d594f4; }.end-element { fill : #00FF55; }.condition-element { fill : #ffa0ea; }.inputoutput-element { fill : #55FFFF; }.operation-element { fill : #FFFF99; }.subroutine-element { fill : #a0e0ff; }.parallel-element { fill : #FFCCFF; }#code{display: none;}::-webkit-scrollbar {display:block;}::-webkit-scrollbar-thumb {border:1px solid #60a0e0;background: #c0e0ff;}::-webkit-scrollbar-thumb:hover {background: #00ffff;}</style><script src="flowchart.js"></script>""", """<script>window.onload = function () {var code = document.getElementById("code").value,chart;if (chart) {chart.clean();}chart = flowchart.parse(code);chart.drawSVG('canvas', {'x': 20,'y': 20,'roundness': 5,"arrow-end": "diamond",'line-width': 1,'maxWidth': 80,'line-length': 40,'text-margin': 15,'font-size': 11,'font': 'normal','font-family': 'Arial','font-weight': 'normal','font-color': 'black','line-color': 'black','element-color': 'black','fill': 'white','yes-text': 'Doğru','no-text': 'Yanlış','scale': 1,'symbols': {'start': {'font-color': 'black','element-color': 'green','class': 'start-element' },'end':{'class': 'end-element'},'condition': {'class': 'condition-element'},'inputoutput': {'class': 'inputoutput-element'},'operation': {'class': 'operation-element'},'subroutine': {'class': 'subroutine-element'},'parallel': {'class': 'parallel-element'}},'flowstate' : {'past' : { 'fill' : '#CCCCCC', 'font-size' : 12},'current' : {'fill' : 'yellow', 'font-color' : 'red', 'font-weight' : 'bold'},'future' : { 'fill' : '#FFFF99'},'request' : { 'fill' : 'blue'},'invalid': {'fill' : '#444444'},'approved' : { 'fill' : '#58C4A3', 'font-size' : 12, 'yes-text' : 'APPROVED', 'no-text' : 'n/a' },'rejected' : { 'fill' : '#C45879', 'font-size' : 12, 'yes-text' : 'n/a', 'no-text' : 'REJECTED' }}});};document.addEventListener("DOMContentLoaded", function () {const ele = document.getElementById("canvas");ele.style.cursor = "move";let pos = { top: 0, left: 0, x: 0, y: 0 };const mouseDownHandler = function (e) {ele.style.cursor = "move";ele.style.userSelect = "none";pos = {left: ele.scrollLeft,top: ele.scrollTop,x: e.clientX,y: e.clientY,};document.addEventListener("mousemove", mouseMoveHandler);document.addEventListener("mouseup", mouseUpHandler);};const mouseMoveHandler = function (e) {const dx = e.clientX - pos.x;const dy = e.clientY - pos.y;ele.scrollTop = pos.top - dy;ele.scrollLeft = pos.left - dx;};const mouseUpHandler = function () {ele.style.cursor = "move";ele.style.removeProperty("user-select");document.removeEventListener("mousemove", mouseMoveHandler);document.removeEventListener("mouseup", mouseUpHandler);};ele.addEventListener("mousedown", mouseDownHandler);});</script></head><body><div><textarea id="code" style="width: 100%;" rows="11">""", "</textarea></div><div id='canvas'></body></html>"
        jsfile = open(join(dirname(__file__), "./flowchart.js"),encoding="utf-8").read()
        file_path = join(dirname(__file__), "./test.py")
        with open(file_path) as f:
            code = f.read()
        fc = Flowchart.from_code(code).flowchart().replace(' start ', ' Başla ').replace('end function return', 'Fonksiyon Sonu').replace(' end ', ' Son ').replace(' output: ', ' Çıktı: ').replace(' input: ', ' Girdi: ')
        self.browser = Browser(htmlstart+"<script>\n" +jsfile+"</script>\n"+htmlmid + str(fc) + htmlend)
        self.horizontalLayout_3.addWidget(self.browser)
        self.tabWidget.addTab(self.tab, f"")

    def closeTab(self, index):
        self.tabWidget.removeTab(index)
        self.movie.start()
        self.movie.setSpeed(250)
        self.movie.setPaused(False)
        QTimer.singleShot(1000, lambda : self.loading.done(0))
        if self.loading.exec_() == QMessageBox.Yes:
            pass
        self.movie.stop()

    def magnifypluser(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def magnifyminuser(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)

    def defhomepage(self):
        self.browser.setZoomFactor(1.0)
        self.openTab()

    def saveFile(self):
        if(FlowchartMaker.pagewidth != 0 and FlowchartMaker.pageheight != 0):
            dialog = QFileDialog(self)
            dialog.setViewMode(QFileDialog.List)
            plt = system()
            if plt == "Windows":
                documents_dir = join(
                    environ['USERPROFILE'] + "/Documents/PynarKutu/")
            elif plt == "Linux":
                documents_dir = check_output(["xdg-user-dir", "DOCUMENTS"], universal_newlines=True).strip() + "/PynarKutu"
            if not exists(documents_dir):
                makedirs(documents_dir)
            filename = dialog.getSaveFileName(
                self, "Kaydet", documents_dir, "Flowchart Pdf (*.pdf)")
            if filename[0]:
                fullpath = filename[0]
                pagelay = QPageLayout()
                pagelay.setPageSize(QPageSize(QSize(FlowchartMaker.pagewidth+100, FlowchartMaker.pageheight+100), "A4"))
                if(not fullpath.endswith(".pdf")):
                    fullpath += ".pdf"
                try:
                    self.browser.page().printToPdf(abspath(fullpath), pageLayout=pagelay)
                    self.statusBar.showMessage(fullpath + " kaydedildi", 3000)
                except Exception as e:
                    self.statusBar.showMessage('Dosya kayıt edilemedi !', 3000)
            else:
                self.statusBar.showMessage('Dosya kayıt edilemedi !', 3000)
        else:
            self.movie.start()
            self.movie.setSpeed(250)
            self.movie.setPaused(False)
            QTimer.singleShot(1000, lambda : self.loading.done(0))
            if self.loading.exec_() == QMessageBox.Yes:
                pass
            self.movie.stop()


if __name__ == "__main__":
    app = QApplication(argv)
    Form = FlowchartMaker()
    Form.show()
    exit(app.exec_())

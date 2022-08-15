from pyflowchart import Flowchart
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QFrame,QHBoxLayout,QWidget,QAction,QMenuBar,QToolBar,QStatusBar,QMenu,QTabWidget,QLabel,QLineEdit,QMessageBox
from PyQt5.QtCore import Qt,QUrl,QSize,Qt,QRect,QTimer
from PyQt5.QtGui import QPixmap,QIcon,QPageSize,QPageLayout,QMovie
import icons_rc
from PyQt5 import QtWebEngineWidgets as web
from sys import exit,argv
from os.path import dirname,join,abspath,exists
from platform import system
from os import environ,makedirs
from subprocess import check_output


class LoadingMessageBox(QMessageBox):

    def __init__(self,parent=None):
        super().__init__(parent)
        movie = QMovie(':/icons/icons/loading.gif')
        label_gif = QLabel(self)
        label_gif.setMovie(movie)
        label_gif.setAlignment(Qt.AlignCenter)
        label_gif.setGeometry(QRect(18,0,205,20))
        label_text = QLineEdit("Akış Şeması Düzenleniyor",self)
        label_text.setReadOnly(True)
        label_text.setGeometry(QRect(18,110,195,25))
        label_text.setAlignment(Qt.AlignCenter)
        label_text2 = QLineEdit("Lütfen bekleyiniz...",self)
        label_text2.setReadOnly(True)
        label_text2.setGeometry(QRect(18,135,185,25))
        label_text2.setAlignment(Qt.AlignCenter)
        movie.start()
        movie.setSpeed(250)
        movie.setPaused(False)
        self.setStyleSheet("QLineEdit{font-size: 12pt;border:none; background-color:transparent}QMessageBox{opacity: 0;border: 10px solid #00ff88;background-color: #ffff88;border-radius:10px;}QLabel{margin: 10px 10px;font-size: 12pt;height: 110px; min-height: 110px; max-height: 110px; width: 155px; min-width: 155px; max-width: 155px;}QPushButton{background-color: #00aaff;color: white;font-size: 12pt;padding: 5px 18px 5px 18px;text-align: center;text-decoration: none;display: inline-block;margin: 4px 2px;border-radius: 7px;}QPushButton:hover {background: #58c1e7;}")
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        self.setStandardButtons(QMessageBox.NoButton)


class FlowchartMaker(QMainWindow):

    pagewidth = 0
    pageheight = 0

    def __init__(self):
        super(FlowchartMaker,self).__init__()
        self.loading = LoadingMessageBox()
        self.file_path = ""
        self.mainWid = QWidget(self)
        self.horLay = QHBoxLayout(self.mainWid)
        self.view = QFrame(self.mainWid)
        self.flowBar = QMenuBar(self)
        self.filemenu = QMenu("Dosya",self.flowBar)
        self.helpmenu = QMenu("Yardım",self.flowBar)
        self.chartStatus = QStatusBar(self)
        self.toolBar = QToolBar(self)
        self.savebut = QAction(self,icon = QIcon(QPixmap(":/icons/icons/save.png")))
        self.magnifyplus = QAction(self,icon = QIcon(QPixmap(":/icons/icons/yakın.png")))
        self.magnifyminus = QAction(self,icon = QIcon(QPixmap(":/icons/icons/uzak.png")))
        self.defhome = QAction(self,icon = QIcon(QPixmap(":/icons/icons/defhome.png")))
        self.grabpage = QAction(self,icon = QIcon(QPixmap(":/icons/icons/grab.png")))
        self.openfile = QAction("Aç")
        self.exitact = QAction("Çıkış")
        self.tabWidget = QTabWidget(self.view)
        self.horLay_2 = QHBoxLayout(self.view)
        self.resize(800,500)
        self.setWindowIcon(QIcon(QPixmap(":/icons/icons/flowchart.png")))
        self.setCentralWidget(self.mainWid)
        self.setMenuBar(self.flowBar)
        self.setStatusBar(self.chartStatus)
        self.addToolBar(self.toolBar)
        self.setWindowTitle("Pynar Flowchart")
        self.horLay.addWidget(self.view)      
        self.horLay.setContentsMargins(0,0,0,0)
        self.horLay.setSpacing(0)
        self.horLay_2.setContentsMargins(0,0,0,0)
        self.horLay_2.setSpacing(0)
        self.horLay_2.addWidget(self.tabWidget)
        self.view.setMinimumSize(QSize(800,500))
        self.flowBar.addAction(self.filemenu.menuAction())
        self.flowBar.addAction(self.helpmenu.menuAction())
        self.flowBar.setGeometry(QRect(0,0,1066,22))
        self.toolBar.setMinimumSize(QSize(0,40))
        self.toolBar.setIconSize(QSize(40,40))
        self.toolBar.addAction(self.savebut)
        self.toolBar.addAction(self.magnifyplus)
        self.toolBar.addAction(self.magnifyminus)
        self.toolBar.addAction(self.defhome)
        self.toolBar.addAction(self.grabpage)
        self.toolBar.setMovable(False)
        self.filemenu.addAction(self.openfile)
        self.filemenu.addAction(self.exitact)
        self.savebut.setToolTip("Kaydet.")
        self.defhome.setToolTip("Eski Haline getir.")
        self.grabpage.setToolTip("Sayfayı Sürükle.")
        self.magnifyplus.setToolTip("Yakınlaştır.")
        self.magnifyminus.setToolTip("Uzaklaştır.")
        self.magnifyplus.setShortcut("Ctrl++")
        self.savebut.setShortcut("Ctrl+S")
        self.magnifyminus.setShortcut("Ctrl+-")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setCurrentIndex(-1)
        self.tabWidget.setMovable(False)
        self.savebut.triggered.connect(self.saveFile)
        self.magnifyplus.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor()+0.1))
        self.magnifyminus.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor()-0.1))
        self.exitact.triggered.connect(self.close)
        self.defhome.triggered.connect(lambda: self.htmlOpener("noGrab"))
        self.grabpage.triggered.connect(lambda: self.htmlOpener("grab"))
        self.openfile.triggered.connect(self.openFile)
        self.defhome.setDisabled(True)
        self.grabpage.setDisabled(True)
        self.magnifyminus.setDisabled(True)
        self.magnifyplus.setDisabled(True)
        self.savebut.setDisabled(True)
        self.mainWid.setStyleSheet("QTabWidget::pane { background: transparent;color: white;}QTabBar::tab{height: 0px;width: 0px;}QTabWidget::tab-bar:top {top: 0px;}QTabWidget::tab-bar:bottom {bottom: 0px;}QTabWidget::tab-bar:left {right: 0px;}QTabWidget::tab-bar:right {left: 0px;}QTabBar::tab:selected {color: white;background: #394b58;}QTabBar::tab:!selected {background: transparent;color: white;}QTabBar::tab:!selected:hover {background: #6b899f;color: black;}QTabBar::tab:top:last,QTabBar::tab:bottom:last,QTabBar::tab:top:only-one,QTabBar::tab:bottom:only-one {margin-right: 0;}QTabBar::tab:left:last,QTabBar::tab:right:last,QTabBar::tab:left:only-one,QTabBar::tab:right:only-one {margin-bottom: 0;}QToolBar {border: 0px;}QToolButton::hover {background-color: transparent; margin-left:2px;margin-bottom:2px;};QToolButton:pressed{background-color: transparent;}")
        self.chartStatus.setStyleSheet("QStatusBar{background-color: rgb(0,96,132);color:white;}")

    def openFile(self):
        self.file_path = QFileDialog.getOpenFileName(self,"Dosya Aç","","Python Dosyası (*.py)")[0]
        if self.file_path:
            self.htmlOpener("noGrab")

    def onLoadFinished(self,ok):
        if ok:
            self.browser.page().runJavaScript("document.getElementsByTagName('svg')[0]['clientWidth'];",self.ready1)
            self.browser.page().runJavaScript("document.getElementsByTagName('svg')[0]['clientHeight'];",self.ready2)

    def ready1(self,width):
        if(FlowchartMaker.pagewidth == 0):
            FlowchartMaker.pagewidth += width

    def ready2(self,height):
        if(FlowchartMaker.pageheight == 0):
            FlowchartMaker.pageheight += height

    def htmlOpener(self,situation):
        FlowchartMaker.pagewidth = 0
        FlowchartMaker.pageheight = 0
        QTimer.singleShot(1000,lambda: self.loading.done(0))
        self.loading.exec_() 
        start,grabcss,grabjs,middle,end = "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><style type='text/css'>body{ margin:0px;}.start-element {fill : #d594f4;}.end-element {fill : #00FF55;}.condition-element {fill : #ffa0ea;}.inputoutput-element {fill : #55FFFF;}.operation-element {fill : #FFFF99;}.subroutine-element {fill : #a0e0ff;}.parallel-element {fill : #FFCCFF;}#code{display: none;}::-webkit-scrollbar {display:block;}::-webkit-scrollbar-thumb {border:1px solid #60a0e0;background: #c0e0ff;}::-webkit-scrollbar-thumb:hover {background: #00ffff;}</style>","<style>#canvas { cursor:move; height:100vh;width:100vw;overflow: auto;}::-webkit-scrollbar {width: 0rem;height: 0rem;}#canvas::-webkit-scrollbar { width: 1rem;height: 1rem;}</style>","<script>document.addEventListener('DOMContentLoaded',function () {const ele = document.getElementById('canvas');ele.style.cursor = 'move';let pos = { top: 0,left: 0,x: 0,y: 0};const mouseDownHandler = function (e) {ele.style.cursor = 'move';ele.style.userSelect = 'none';pos = { left: ele.scrollLeft,top: ele.scrollTop,x: e.clientX,y: e.clientY,};document.addEventListener('mousemove',mouseMoveHandler);document.addEventListener('mouseup',mouseUpHandler);};const mouseMoveHandler = function (e) {const dx = e.clientX-pos.x;const dy = e.clientY-pos.y;ele.scrollTop = pos.top-dy;ele.scrollLeft = pos.left-dx;};const mouseUpHandler = function () {ele.style.cursor = 'move';ele.style.removeProperty('user-select');document.removeEventListener('mousemove',mouseMoveHandler);document.removeEventListener('mouseup',mouseUpHandler);};ele.addEventListener('mousedown',mouseDownHandler);});</script>","<script>window.onload = function () {var chart;if (chart) {chart.clean();}chart = flowchart.parse(document.getElementById('code').value);chart.drawSVG('canvas',{'x': 20,'y': 20,'roundness': 5,'arrow-end': 'diamond','line-width': 1,'maxWidth': 80,'line-length': 40,'text-margin': 15,'font-size': 11,'font': 'normal','font-family': 'Arial','font-weight': 'normal','font-color': 'black','line-color': 'black','element-color': 'black','fill': 'white','yes-text': 'Doğru','no-text': 'Yanlış','scale': 1,'symbols': {'start': {'font-color': 'black','element-color': 'green','class': 'start-element'},'end':{'class': 'end-element'},'condition': {'class': 'condition-element'},'inputoutput': {'class': 'inputoutput-element'},'operation': {'class': 'operation-element'},'subroutine': {'class': 'subroutine-element'},'parallel': {'class': 'parallel-element'} },'flowstate' : {'past' : {'fill' : '#CCCCCC','font-size' : 12},'current' : {'fill' : 'yellow','font-color' : 'red','font-weight' : 'bold'},'future' : {'fill' : '#FFFF99'},'request' : {'fill' : 'blue'},'invalid': {'fill' : '#444444'},'approved' : {'fill' : '#58C4A3','font-size' : 12,'yes-text' : 'APPROVED','no-text' : 'n/a'},'rejected' : {'fill' : '#C45879','font-size' : 12,'yes-text' : 'n/a','no-text' : 'REJECTED'} } });};</script></head><body><div><textarea id='code' style='width: 100%;' rows='11'>","</textarea></div><div style='margin-left:20px;' id='canvas'></div></body></html>"
        if(self.tabWidget.currentIndex() >= 0):
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
        self.tab = QWidget()
        self.horLay_3 = QHBoxLayout(self.tab)
        self.horLay_3.setContentsMargins(0,0,0,0)
        self.horLay_3.setSpacing(0)
        self.tabWidget.setCurrentIndex(self.tabWidget.count())
        jsfile = "<script>\n"+open(join(dirname(__file__),"./flowchart.js"),encoding="utf-8").read()+"</script>\n"
        fc = self.conditionSearch(open(self.file_path,encoding="utf-8").read())
        if(situation == "grab"):
            self.browser = web.QWebEngineView()
            self.browser.setHtml(start+grabcss+grabjs+jsfile+middle+fc+end,baseUrl=QUrl("file://"))
        if(situation == "noGrab"):
            self.browser = web.QWebEngineView()
            self.browser.setHtml(start+jsfile +middle+fc+end,baseUrl=QUrl("file://"))
        self.chartStatus.showMessage("Akış Şeması Düzenlendi.",3000)
        self.horLay_3.addWidget(self.browser)
        self.tabWidget.addTab(self.tab,f"")
        self.browser.loadFinished.connect(self.onLoadFinished)
        self.defhome.setEnabled(True)
        self.grabpage.setEnabled(True)
        self.magnifyminus.setEnabled(True)
        self.magnifyplus.setEnabled(True)
        self.savebut.setEnabled(True)

    def conditionSearch(self,code: str) -> str:
        y,n,q,c0,c1,c2,w,f = '₺₺₺₺','\n',"''\n",'if','elif','else','while','for'
        Q=[]
        for i in reversed(range(20)):
            if(i >= 10):
                Q.append('€€€€'*(i-9))
            else:
                Q.append('    '*(i+1))
        code = (n+code).replace(Q[19],Q[9]).replace(n,y).replace(y+w,n+q+w).replace(y+f,n+q+f).replace(y+c0,n+q+c0)
        for i in range(len(Q)-10):
            if(code.count(Q[i]) > 0):
                code = code.replace(y+Q[i],n+Q[i+10]+q+Q[i+10]).replace(Q[i+10]+q+Q[i+10]+c2,Q[i+10]+n+Q[i+10]+c2).replace(Q[i+10]+q+Q[i+10]+c1,Q[i+10]+n+Q[i+10]+c1)
        code = code.replace(Q[9],Q[19]).replace(y,n)
        fc = Flowchart.from_code(code).flowchart().replace(' start ',' Başla ').replace('end function return','Fonksiyon Sonu').replace(' end ',' Son ').replace(' output: ',' Çıktı: ').replace(' input: ',' Girdi: ').replace("operation: ''","operation: ㅤ")
        return fc

    def saveFile(self):
        if(FlowchartMaker.pagewidth != 0 and FlowchartMaker.pageheight != 0):
            dialog = QFileDialog(self)
            dialog.setViewMode(QFileDialog.List)
            plt = system()
            if plt == "Windows":
                documents_dir = join(environ['USERPROFILE']+"/Documents/PynarKutu/")
            elif plt == "Linux":
                documents_dir = check_output(["xdg-user-dir","DOCUMENTS"],universal_newlines=True).strip()+"/PynarKutu"
            if not exists(documents_dir):
                makedirs(documents_dir)
            filename = dialog.getSaveFileName(self,"Kaydet",documents_dir,"Flowchart Pdf (*.pdf)")
            if filename[0]:
                fullpath = filename[0]
                pagelay = QPageLayout()
                if(FlowchartMaker.pagewidth>FlowchartMaker.pageheight):
                    pagelay.setOrientation(QPageLayout.Orientation.Landscape)
                else:
                    pagelay.setOrientation(QPageLayout.Orientation.Portrait)
                pagelay.setPageSize(QPageSize(QSize(FlowchartMaker.pagewidth,FlowchartMaker.pageheight),"A4"))
                if(not fullpath.endswith(".pdf")):
                    fullpath += ".pdf"
                try:
                    self.browser.page().printToPdf(abspath(fullpath),pageLayout=pagelay)
                    self.chartStatus.showMessage(fullpath+" kaydedildi.",3000)
                except Exception as e:
                    self.chartStatus.showMessage('Akış Şeması kayıt edilemedi !',3000)
            else:
                self.chartStatus.showMessage('Akış Şeması kayıt edilemedi !',3000)
        else:
            self.chartStatus.showMessage('Akış Şeması kayıt edilemedi !',3000)

if __name__ == "__main__":
    app = QApplication(argv)
    Form = FlowchartMaker()
    Form.show()
    exit(app.exec_())

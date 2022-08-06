from pyflowchart import Flowchart
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget,QMessageBox,QTabWidget,
    QGridLayout,QToolBox
)
from PyQt5.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve,
    QUrl, QMetaObject, QSize, Qt,QRect
)
from PyQt5.QtGui import (
    QPixmap, QIcon, QFont,
    QPageSize, QPageLayout, QCursor
)

import icons_rc
from PyQt5 import QtWebEngineWidgets as web
from sys import exit, argv
from os.path import dirname, join, abspath
# from builder import Ui_Builder


# pyrcc5 icons.qrc -o icons_rc.py
# pyuic5 builder.ui -o builder.py

class Ui_Builder(object):
    def setupUi(self, Builder):
        Builder.setObjectName("Builder")
        Builder.resize(1066, 572)
        Builder.setMinimumSize(QSize(1050, 570))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/icons/download.svg"), QIcon.Normal, QIcon.Off)
        Builder.setWindowIcon(icon)
        self.centralwidget = QWidget(Builder)
        self.centralwidget.setMinimumSize(QSize(1050, 570))
        font = QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("QScrollBar:vertical {border-radius: 5px;background:transparent;width:10px;margin:0px;}QScrollBar::handle:vertical {border-radius: 5px;background: #88888888;min-width:5px;max-width:5px;min-height:50px;max-height:50px;width:5px;height:5px;}QScrollBar::handle:vertical:hover {background: #ffffff;}QScrollBar::add-line:vertical {height: 0px;subcontrol-position: bottom;    subcontrol-origin: margin;}QScrollBar::sub-line:vertical {height: 0px;subcontrol-position: top;subcontrol-origin: margin;}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background:transparent;}QScrollBar:horizontal {border-radius: 5px;background:transparent;height:10px;margin:0px;}QScrollBar::handle:horizontal {border-radius: 5px;background: #88888888;min-width:50px;max-width:50px;min-height:5px;max-height:5px;width:5px;height:5px;}QScrollBar::handle:horizontal:hover {background: #ffffff;}QScrollBar::add-line:horizontal {height: 0px;subcontrol-position: bottom;    subcontrol-origin: margin;}QScrollBar::sub-line:horizontal {height: 0px;subcontrol-position: top;subcontrol-origin: margin;}QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {background:transparent;}*{border: none;color:white;}#centralwidget,#html{background-color:rgba(112.520718,44.062154,249.437846,242.25);}QLineEdit{border: 1px solid black;text-align: center;font-size:12pt;color:black;padding: 1px;border-radius: 7px;background: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fff,stop: 0.4999 #eee,stop: 0.5 #ddd,stop: 1 #eee );width: 15px;}QLineEdit:hover{background-color: #ff0088;}QPushButton {text-align: center;font: 12pt;color: black;padding: 1px;background-color: #00ff88;border:none;}QPushButton:hover {background-color: #007fff;color: white;border-color: white;}#browsebut {border-radius: 7px;border: 1px solid black;}QToolBox::tab {border-radius: 0px;    background-color: #8800ff;text-align: center;}QToolBox::tab:hover {background-color: #007fff;}QToolBox::tab:selected { color: white;text-align: center;background-color: #00ff88;}QLabel{color:black;}QTabWidget::pane {background: transparent;color: white;}QTabBar::tab{height: 0px;width: 0px;}QTabWidget::tab-bar:top {top: 0px;}QTabWidget::tab-bar:bottom {bottom: 0px;}QTabWidget::tab-bar:left {right: 0px;}QTabWidget::tab-bar:right {left: 0px;}QTabBar::tab:selected {color: white;background: #394b58;}QTabBar::tab:!selected {background: transparent;color: white;}QTabBar::tab:!selected:hover {background: #6b899f;color: black;}QTabBar::tab:top:last, QTabBar::tab:bottom:last,QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {margin-right: 0;}QTabBar::tab:left:last, QTabBar::tab:right:last,QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {margin-bottom: 0;}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QToolBox(self.centralwidget)
        self.leftMenu.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.leftMenu.setFont(font)
        self.leftMenu.setStyleSheet("QWidget{background-color: #ff8888;}QLineEdit{color:white;}")
        self.leftMenu.setObjectName("leftMenu")
        self.page_0 = QWidget()
        self.page_0.setGeometry(QRect(0, 0, 250, 276))
        self.page_0.setMinimumSize(QSize(250, 0))
        self.page_0.setObjectName("page_0")
        self.gridLayout_8 = QGridLayout(self.page_0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.genframecolor = QLineEdit(self.page_0)
        self.genframecolor.setObjectName("genframecolor")
        self.gridLayout_8.addWidget(self.genframecolor, 6, 1, 1, 2)
        self.label_50 = QLabel(self.page_0)
        self.label_50.setObjectName("label_50")
        self.gridLayout_8.addWidget(self.label_50, 0, 0, 1, 1)
        self.genfontcolor = QLineEdit(self.page_0)
        self.genfontcolor.setObjectName("genfontcolor")
        self.gridLayout_8.addWidget(self.genfontcolor, 2, 1, 1, 2)
        self.genbackcolor = QLineEdit(self.page_0)
        self.genbackcolor.setObjectName("genbackcolor")
        self.gridLayout_8.addWidget(self.genbackcolor, 0, 1, 1, 2)
        self.genfontweight = QLineEdit(self.page_0)
        self.genfontweight.setObjectName("genfontweight")
        self.gridLayout_8.addWidget(self.genfontweight, 4, 1, 1, 2)
        self.label_51 = QLabel(self.page_0)
        self.label_51.setObjectName("label_51")
        self.gridLayout_8.addWidget(self.label_51, 5, 0, 1, 1)
        self.label_52 = QLabel(self.page_0)
        self.label_52.setObjectName("label_52")
        self.gridLayout_8.addWidget(self.label_52, 6, 0, 1, 1)
        self.label_46 = QLabel(self.page_0)
        self.label_46.setObjectName("label_46")
        self.gridLayout_8.addWidget(self.label_46, 3, 0, 1, 1)
        self.genframewidth = QLineEdit(self.page_0)
        self.genframewidth.setObjectName("genframewidth")
        self.gridLayout_8.addWidget(self.genframewidth, 5, 1, 1, 2)
        self.label_53 = QLabel(self.page_0)
        self.label_53.setObjectName("label_53")
        self.gridLayout_8.addWidget(self.label_53, 7, 0, 1, 1)
        self.genfontsize = QLineEdit(self.page_0)
        self.genfontsize.setObjectName("genfontsize")
        self.gridLayout_8.addWidget(self.genfontsize, 3, 1, 1, 2)
        self.genframeroud = QLineEdit(self.page_0)
        self.genframeroud.setObjectName("genframeroud")
        self.gridLayout_8.addWidget(self.genframeroud, 7, 1, 1, 2)
        self.label_49 = QLabel(self.page_0)
        self.label_49.setObjectName("label_49")
        self.gridLayout_8.addWidget(self.label_49, 4, 0, 1, 1)
        self.label_45 = QLabel(self.page_0)
        self.label_45.setObjectName("label_45")
        self.gridLayout_8.addWidget(self.label_45, 2, 0, 1, 1)
        self.label_54 = QLabel(self.page_0)
        self.label_54.setObjectName("label_54")
        self.gridLayout_8.addWidget(self.label_54, 1, 0, 1, 1)
        self.genlinecolor = QLineEdit(self.page_0)
        self.genlinecolor.setObjectName("genlinecolor")
        self.gridLayout_8.addWidget(self.genlinecolor, 1, 1, 1, 2)
        self.leftMenu.addItem(self.page_0, "")
        self.page_1 = QWidget()
        self.page_1.setGeometry(QRect(0, 0, 250, 276))
        self.page_1.setMinimumSize(QSize(250, 0))
        self.page_1.setObjectName("page_1")
        self.gridLayout_7 = QGridLayout(self.page_1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_43 = QLabel(self.page_1)
        self.label_43.setObjectName("label_43")
        self.gridLayout_7.addWidget(self.label_43, 0, 0, 1, 1)
        self.label_44 = QLabel(self.page_1)
        self.label_44.setObjectName("label_44")
        self.gridLayout_7.addWidget(self.label_44, 1, 0, 1, 1)
        self.label_48 = QLabel(self.page_1)
        self.label_48.setObjectName("label_48")
        self.gridLayout_7.addWidget(self.label_48, 2, 0, 1, 3)
        self.startfontcolor = QLineEdit(self.page_1)
        self.startfontcolor.setObjectName("startfontcolor")
        self.gridLayout_7.addWidget(self.startfontcolor, 2, 3, 1, 1)
        self.label_47 = QLabel(self.page_1)
        self.label_47.setObjectName("label_47")
        self.gridLayout_7.addWidget(self.label_47, 3, 0, 1, 2)
        self.startlinecolor = QLineEdit(self.page_1)
        self.startlinecolor.setObjectName("startlinecolor")
        self.gridLayout_7.addWidget(self.startlinecolor, 1, 3, 1, 1)
        self.startbackcolor = QLineEdit(self.page_1)
        self.startbackcolor.setObjectName("startbackcolor")
        self.gridLayout_7.addWidget(self.startbackcolor, 0, 3, 1, 1)
        self.startmargin = QLineEdit(self.page_1)
        self.startmargin.setObjectName("startmargin")
        self.gridLayout_7.addWidget(self.startmargin, 3, 3, 1, 1)
        self.leftMenu.addItem(self.page_1, "")
        self.page_2 = QWidget()
        self.page_2.setGeometry(QRect(0, 0, 250, 276))
        self.page_2.setMinimumSize(QSize(250, 0))
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_36 = QLabel(self.page_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_6.addWidget(self.label_36, 0, 0, 1, 1)
        self.label_37 = QLabel(self.page_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout_6.addWidget(self.label_37, 1, 0, 1, 1)
        self.label_55 = QLabel(self.page_2)
        self.label_55.setObjectName("label_55")
        self.gridLayout_6.addWidget(self.label_55, 2, 0, 1, 3)
        self.endfontcolor = QLineEdit(self.page_2)
        self.endfontcolor.setObjectName("endfontcolor")
        self.gridLayout_6.addWidget(self.endfontcolor, 2, 3, 1, 1)
        self.label_40 = QLabel(self.page_2)
        self.label_40.setObjectName("label_40")
        self.gridLayout_6.addWidget(self.label_40, 3, 0, 1, 2)
        self.endlinecolor = QLineEdit(self.page_2)
        self.endlinecolor.setObjectName("endlinecolor")
        self.gridLayout_6.addWidget(self.endlinecolor, 1, 3, 1, 1)
        self.endbackcolor = QLineEdit(self.page_2)
        self.endbackcolor.setObjectName("endbackcolor")
        self.gridLayout_6.addWidget(self.endbackcolor, 0, 3, 1, 1)
        self.endmargin = QLineEdit(self.page_2)
        self.endmargin.setObjectName("endmargin")
        self.gridLayout_6.addWidget(self.endmargin, 3, 3, 1, 1)
        self.leftMenu.addItem(self.page_2, "")
        self.page_3 = QWidget()
        self.page_3.setGeometry(QRect(0, 0, 250, 276))
        self.page_3.setMinimumSize(QSize(250, 0))
        self.page_3.setObjectName("page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_29 = QLabel(self.page_3)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 0, 0, 1, 2)
        self.label_30 = QLabel(self.page_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 1, 0, 1, 1)
        self.label_33 = QLabel(self.page_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 3, 0, 1, 3)
        self.condmargin = QLineEdit(self.page_3)
        self.condmargin.setObjectName("condmargin")
        self.gridLayout_5.addWidget(self.condmargin, 3, 3, 1, 1)
        self.label_56 = QLabel(self.page_3)
        self.label_56.setObjectName("label_56")
        self.gridLayout_5.addWidget(self.label_56, 2, 0, 1, 1)
        self.condfontcolor = QLineEdit(self.page_3)
        self.condfontcolor.setObjectName("condfontcolor")
        self.gridLayout_5.addWidget(self.condfontcolor, 2, 3, 1, 1)
        self.condlinecolor = QLineEdit(self.page_3)
        self.condlinecolor.setObjectName("condlinecolor")
        self.gridLayout_5.addWidget(self.condlinecolor, 1, 3, 1, 1)
        self.condbackcolor = QLineEdit(self.page_3)
        self.condbackcolor.setObjectName("condbackcolor")
        self.gridLayout_5.addWidget(self.condbackcolor, 0, 3, 1, 1)
        self.leftMenu.addItem(self.page_3, "")
        self.page_4 = QWidget()
        self.page_4.setGeometry(QRect(0, 0, 250, 276))
        self.page_4.setMinimumSize(QSize(250, 0))
        self.page_4.setObjectName("page_4")
        self.gridLayout_4 = QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_22 = QLabel(self.page_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QLabel(self.page_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_57 = QLabel(self.page_4)
        self.label_57.setObjectName("label_57")
        self.gridLayout_4.addWidget(self.label_57, 2, 0, 1, 2)
        self.operfontcolor = QLineEdit(self.page_4)
        self.operfontcolor.setObjectName("operfontcolor")
        self.gridLayout_4.addWidget(self.operfontcolor, 2, 3, 1, 1)
        self.label_26 = QLabel(self.page_4)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 3, 0, 1, 2)
        self.operlinecolor = QLineEdit(self.page_4)
        self.operlinecolor.setObjectName("operlinecolor")
        self.gridLayout_4.addWidget(self.operlinecolor, 1, 3, 1, 1)
        self.operbackcolor = QLineEdit(self.page_4)
        self.operbackcolor.setObjectName("operbackcolor")
        self.gridLayout_4.addWidget(self.operbackcolor, 0, 3, 1, 1)
        self.opermargin = QLineEdit(self.page_4)
        self.opermargin.setObjectName("opermargin")
        self.gridLayout_4.addWidget(self.opermargin, 3, 3, 1, 1)
        self.leftMenu.addItem(self.page_4, "")
        self.page_5 = QWidget()
        self.page_5.setGeometry(QRect(0, 0, 250, 276))
        self.page_5.setMinimumSize(QSize(250, 0))
        self.page_5.setObjectName("page_5")
        self.gridLayout_3 = QGridLayout(self.page_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_16 = QLabel(self.page_5)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_58 = QLabel(self.page_5)
        self.label_58.setObjectName("label_58")
        self.gridLayout_3.addWidget(self.label_58, 2, 0, 1, 3)
        self.inoutfontcolor = QLineEdit(self.page_5)
        self.inoutfontcolor.setObjectName("inoutfontcolor")
        self.gridLayout_3.addWidget(self.inoutfontcolor, 2, 3, 1, 1)
        self.label_19 = QLabel(self.page_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 3, 0, 1, 2)
        self.inoutlinecolor = QLineEdit(self.page_5)
        self.inoutlinecolor.setObjectName("inoutlinecolor")
        self.gridLayout_3.addWidget(self.inoutlinecolor, 1, 3, 1, 1)
        self.inoutbackcolor = QLineEdit(self.page_5)
        self.inoutbackcolor.setObjectName("inoutbackcolor")
        self.gridLayout_3.addWidget(self.inoutbackcolor, 0, 3, 1, 1)
        self.inoutmargin = QLineEdit(self.page_5)
        self.inoutmargin.setObjectName("inoutmargin")
        self.gridLayout_3.addWidget(self.inoutmargin, 3, 3, 1, 1)
        self.leftMenu.addItem(self.page_5, "")
        self.page_6 = QWidget()
        self.page_6.setGeometry(QRect(0, 0, 250, 276))
        self.page_6.setMinimumSize(QSize(250, 0))
        self.page_6.setObjectName("page_6")
        self.gridLayout_2 = QGridLayout(self.page_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QLabel(self.page_6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_59 = QLabel(self.page_6)
        self.label_59.setObjectName("label_59")
        self.gridLayout_2.addWidget(self.label_59, 2, 0, 1, 2)
        self.parfontcolor = QLineEdit(self.page_6)
        self.parfontcolor.setObjectName("parfontcolor")
        self.gridLayout_2.addWidget(self.parfontcolor, 2, 3, 1, 1)
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 2)
        self.parlinecolor = QLineEdit(self.page_6)
        self.parlinecolor.setObjectName("parlinecolor")
        self.gridLayout_2.addWidget(self.parlinecolor, 1, 3, 1, 1)
        self.parbackcolor = QLineEdit(self.page_6)
        self.parbackcolor.setObjectName("parbackcolor")
        self.gridLayout_2.addWidget(self.parbackcolor, 0, 3, 1, 1)
        self.parmargin = QLineEdit(self.page_6)
        self.parmargin.setObjectName("parmargin")
        self.gridLayout_2.addWidget(self.parmargin, 3, 3, 1, 1)
        self.leftMenu.addItem(self.page_6, "")
        self.page_7 = QWidget()
        self.page_7.setGeometry(QRect(0, 0, 250, 276))
        self.page_7.setMinimumSize(QSize(250, 0))
        self.page_7.setObjectName("page_7")
        self.gridLayout = QGridLayout(self.page_7)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QLabel(self.page_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_3 = QLabel(self.page_7)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.subbackcolor = QLineEdit(self.page_7)
        self.subbackcolor.setObjectName("subbackcolor")
        self.gridLayout.addWidget(self.subbackcolor, 0, 1, 1, 1)
        self.sublinecolor = QLineEdit(self.page_7)
        self.sublinecolor.setObjectName("sublinecolor")
        self.gridLayout.addWidget(self.sublinecolor, 1, 1, 1, 1)
        self.submargin = QLineEdit(self.page_7)
        self.submargin.setObjectName("submargin")
        self.gridLayout.addWidget(self.submargin, 5, 1, 1, 1)
        self.label = QLabel(self.page_7)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_60 = QLabel(self.page_7)
        self.label_60.setObjectName("label_60")
        self.gridLayout.addWidget(self.label_60, 3, 0, 1, 1)
        self.subfontcolor = QLineEdit(self.page_7)
        self.subfontcolor.setObjectName("subfontcolor")
        self.gridLayout.addWidget(self.subfontcolor, 3, 1, 1, 1)
        self.leftMenu.addItem(self.page_7, "")
        self.horizontalLayout.addWidget(self.leftMenu)
        self.frame = QFrame(self.centralwidget)
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setObjectName("frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.customize = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customize.sizePolicy().hasHeightForWidth())
        self.customize.setSizePolicy(sizePolicy)
        self.customize.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/icons/helpers.svg"), QIcon.Normal, QIcon.Off)
        self.customize.setIcon(icon1)
        self.customize.setObjectName("customize")
        self.verticalLayout.addWidget(self.customize)
        self.applybut = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applybut.sizePolicy().hasHeightForWidth())
        self.applybut.setSizePolicy(sizePolicy)
        self.applybut.setCursor(QCursor(Qt.PointingHandCursor))
        self.applybut.setObjectName("applybut")
        self.verticalLayout.addWidget(self.applybut)
        self.output = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setCursor(QCursor(Qt.PointingHandCursor))
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.outputframe = QFrame(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputframe.sizePolicy().hasHeightForWidth())
        self.outputframe.setSizePolicy(sizePolicy)
        self.outputframe.setMaximumSize(QSize(16777215, 0))
        self.outputframe.setObjectName("outputframe")
        self.verticalLayout_85 = QVBoxLayout(self.outputframe)
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_85.setSpacing(4)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.outlabel = QLabel(self.outputframe)
        self.outlabel.setMinimumSize(QSize(190, 50))
        self.outlabel.setMaximumSize(QSize(190, 50))
        self.outlabel.setAlignment(Qt.AlignCenter)
        self.outlabel.setObjectName("outlabel")
        self.verticalLayout_85.addWidget(self.outlabel)
        self.outputpath = QLineEdit(self.outputframe)
        self.outputpath.setMinimumSize(QSize(180, 30))
        self.outputpath.setMaximumSize(QSize(180, 30))
        self.outputpath.setCursorPosition(3)
        self.outputpath.setObjectName("outputpath")
        self.verticalLayout_85.addWidget(self.outputpath, 0, Qt.AlignHCenter)
        self.browsebut = QPushButton(self.outputframe)
        self.browsebut.setMinimumSize(QSize(90, 30))
        self.browsebut.setMaximumSize(QSize(90, 30))
        self.browsebut.setCursor(QCursor(Qt.PointingHandCursor))
        self.browsebut.setObjectName("browsebut")
        self.verticalLayout_85.addWidget(self.browsebut, 0, Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.outputframe)
        self.save = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setCursor(QCursor(Qt.PointingHandCursor))
        self.save.setIcon(icon)
        self.save.setObjectName("save")
        self.verticalLayout.addWidget(self.save)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout.addWidget(self.tabWidget)
        Builder.setCentralWidget(self.centralwidget)

        self.leftMenu.setCurrentIndex(7)
        self.leftMenu.layout().setSpacing(1)
        self.tabWidget.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(Builder)

        Builder.setWindowTitle("Pynar Flowchart")
        self.genframecolor.setText("#000000")
        self.label_50.setText("Arka Plan Rengi:")
        self.genfontcolor.setText("#000000")
        self.genbackcolor.setText("#ffffff")
        self.genfontweight.setText("400")
        self.label_51.setText("Çerçeve Kalınlığı:")
        self.label_52.setText("Çerçeve Rengi:")
        self.label_46.setText("Font Büyüklüğü:")
        self.genframewidth.setText("3")
        self.label_53.setText("Çerçeve Yuvarlaklığı:")
        self.genfontsize.setText("12")
        self.genframeroud.setText("10")
        self.label_49.setText("Font Kalınlığı:")
        self.label_45.setText("Font Rengi:")
        self.label_54.setText("Çizgi Rengi:")
        self.genlinecolor.setText("#000000")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_0), "Genel")
        self.label_43.setText("Arka Plan Rengi:")
        self.label_44.setText("Çerçeve Rengi:")
        self.label_48.setText("Font Rengi:")
        self.startfontcolor.setText("#000000")
        self.label_47.setText("Kenar-Yazı Mesafesi:")
        self.startlinecolor.setText("#000000")
        self.startbackcolor.setText("#0088ff")
        self.startmargin.setText("5")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_1), "Başla")
        self.label_36.setText("Arka Plan Rengi:")
        self.label_37.setText("Çerçeve Rengi:")
        self.label_55.setText("Font Rengi:")
        self.endfontcolor.setText("#000000")
        self.label_40.setText("Kenar-Yazı Mesafesi:")
        self.endlinecolor.setText("#000000")
        self.endbackcolor.setText("#0088ff")
        self.endmargin.setText("5")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_2), "Son")
        self.label_29.setText("Arka Plan Rengi:")
        self.label_30.setText("Çerçeve Rengi:")
        self.label_33.setText("Kenar-Yazı Mesafesi:")
        self.condmargin.setText("5")
        self.label_56.setText("Font Rengi:")
        self.condfontcolor.setText("#000000")
        self.condlinecolor.setText("#000000")
        self.condbackcolor.setText("#0088ff")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_3), "If / For")
        self.label_22.setText("Arka Plan Rengi:")
        self.label_23.setText("Çerçeve Rengi:")
        self.label_57.setText("Font Rengi:")
        self.operfontcolor.setText("#000000")
        self.label_26.setText("Kenar-Yazı Mesafesi:")
        self.operlinecolor.setText("#000000")
        self.operbackcolor.setText("#0088ff")
        self.opermargin.setText("5")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_4), "Operasyon")
        self.label_15.setText("Arka Plan Rengi:")
        self.label_16.setText("Çerçeve Rengi:")
        self.label_58.setText("Font Rengi:")
        self.inoutfontcolor.setText("#000000")
        self.label_19.setText("Kenar-Yazı Mesafesi:")
        self.inoutlinecolor.setText("#000000")
        self.inoutbackcolor.setText("#0088ff")
        self.inoutmargin.setText("5")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_5), "Girdi / Çıktı")
        self.label_8.setText("Arka Plan Rengi:")
        self.label_9.setText("Çerçeve Rengi:")
        self.label_59.setText("Font Rengi:")
        self.parfontcolor.setText("#000000")
        self.label_12.setText("Kenar-Yazı Mesafesi:")
        self.parlinecolor.setText("#000000")
        self.parbackcolor.setText("#0088ff")
        self.parmargin.setText("5")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_6), "Paralel İşlem")
        self.label_6.setText("Kenar-Yazı Mesafesi:")
        self.label_3.setText("Çerçeve Rengi:")
        self.subbackcolor.setText("#0088ff")
        self.sublinecolor.setText("#000000")
        self.submargin.setText("5")
        self.label.setText("Arka Plan Rengi:")
        self.label_60.setText("Font Rengi:")
        self.subfontcolor.setText("#000000")
        self.leftMenu.setItemText(self.leftMenu.indexOf(self.page_7), "Alt İşlem")
        self.customize.setText("Özelleştirme")
        self.applybut.setText("Özelleştirmeleri Uygula")
        self.output.setText("Hedef Klasör Seç")
        self.output.setShortcut("Ctrl+O")
        self.outlabel.setText("Hedef Klasör")
        self.outputpath.setText("C:\\")
        self.browsebut.setText("Seç")
        self.save.setText("Kaydet")
        self.save.setShortcut("Ctrl+S")


class Browser(web.QWebEngineView):

    def __init__(self, html=""):
        super().__init__()
        here = dirname(abspath(__file__)).replace('\\', '/')
        base_path = join(dirname(here), 'dummy').replace('\\', '/')
        self.url = QUrl('file:///' + base_path)
        self.setHtml(html,baseUrl=self.url)

class Web_Builder(QMainWindow, Ui_Builder):
    def __init__(self):
        super(Web_Builder, self).__init__()
        self.setupUi(self)
        self.openTab()     
        self.output.clicked.connect(lambda: self.openClose("output"))
        self.customize.clicked.connect(lambda: self.openClose("custom"))
        self.browsebut.clicked.connect(self.browse_folder)
        self.save.clicked.connect(self.saveFile)
        self.outputpath.setText(dirname(__file__))
        self.outputpath.setReadOnly(True)
        self.outputpath.setCursorPosition(0)
        self.applybut.clicked.connect(lambda:self.openTab())
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.specialHover()
    def openTab(self):
        if(self.tabWidget.currentIndex()>=0):
            self.closeTab(self.tabWidget.currentIndex())
        self.tab = QWidget()
        self.tab.setObjectName(f"{self.tabWidget.count()}")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget.setCurrentIndex(self.tabWidget.count())
        htmlstart = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <style type="text/css">
            * {
                margin: 0px;
                padding: 0px;
                box-sizing: border-box;
                font-family: Consolas, "Courier New", monospace;
                font-size: 12px;
                font-style: normal;
            }
            .codearea {
                margin-left: 0px;
                width: 0%;
                display: none;
            }
            .preview-area {
                width: 100% !important;
            }
            #run {
                margin-left: 0px;
                width: calc(100% - 40px);
                height: 40px;
                background-color: rgb(30, 30, 30);
                color: white;
                border-bottom-right-radius: 5px;
                border: none;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
            }
            #run:hover {
                background-color: #00ff88;
                color: #8800ff;
            }
            ::-webkit-scrollbar {
                display: block;
                width: 10px;
                height: 10px;
            }
            ::-webkit-scrollbar-corner {
                background: transparent;
            }
            ::-webkit-scrollbar-track {
                background: transparent;
            }

            ::-webkit-scrollbar-thumb {
                background: rgba(136, 136, 136, 100);
                border-radius: 5px;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: rgba(85, 85, 85, 100);
            }

            #code {
                display: flex;
                background-color: rgb(30, 30, 30);
                color: rgb(255, 255, 255);
                /* width: calc(100% - 80px); */
                width: 0px;

                height: 550px;
                margin-left: 40px;
                padding-left: 5px;
                border-top-right-radius: 5px;
            }

            textarea {
                resize: none;
                outline: none;
                padding: 0px;
                border: none;
                margin: 0px;
            }

            #lineCounter {
                display: flex;
                overflow-y: hidden;
                text-align: center;
                box-shadow: none;
                position: absolute;
                width: 0px;
                height: 550px;
                background-color: rgb(30, 30, 30);
                color: rgb(133, 133, 133);
                -moz-box-sizing: border-box;
                -webkit-box-sizing: border-box;
                box-sizing: border-box;
            }
            </style>
            <script src="flowchart.js"></script>
            """
        css = self.getCss()
        jsfile = open(join(dirname(__file__), "./flowchart.js"),encoding="utf-8").read()
        js = self.getJavaScript()
        htmlmid = """</head><body><div class='codearea'><textarea id='lineCounter' wrap='off' readonly>1</textarea><textarea id="code">"""
        htmlend = """</textarea><button id="run" type="button">Run</button></div><div class="preview-area" id="canvas"></div></body></html>"""
        file_path = join(dirname(__file__), "./test.py")
        with open(file_path) as f:
            code = f.read()
        fc = Flowchart.from_code(code).flowchart().replace(' start ', ' Başla ').replace(
            'end function return', 'Fonksiyon Sonu').replace(' end ', ' Son ').replace(' output: ', ' Çıktı: ').replace(' input: ', ' Girdi: ')
        self.browser = Browser(htmlstart+css+"<script>\n"+jsfile+"</script>\n"+js + htmlmid + str(fc) + htmlend)
        print(htmlstart+css+js + htmlmid + str(fc) + htmlend)
        self.horizontalLayout_2.addWidget(self.browser)
        self.tabWidget.addTab(self.tab, f"")


    def closeTab(self, index):
        # msgBox =QMessageBox.information(self,"Uyarı","Önceki Şema Kaydedilmedi<br><br>Şimdi Kaydet ?",QMessageBox.Yes,QMessageBox.No )
        # if msgBox == QMessageBox.Yes:
        #     self.saveYesClick()
        #     msgBox.Close
        # elif msgBox == QMessageBox.No:
        #     self.saveNoClick()
        # elif msgBox == QMessageBox.Cancel:
        #     self.cancelButton = True
        self.tabWidget.removeTab(index)

    def saveYesClick(self):
        self.saveFile()
        self.closeTab(self.tabWidget.currentIndex())

    def saveNoClick(self):
        self.closeTab(self.tabWidget.currentIndex())
    def getJavaScript(self):
        jsstart = """
        <script>\nwindow.onload = function () {\nvar btn = document.getElementById("run"),\ncd = document.getElementById("code"),\nchart;\n(btn.onclick = function () {\nvar code = cd.value;\nif (chart) {\nchart.clean();\n}\nchart = flowchart.parse(code);\nchart.drawSVG("canvas", {\n"arrow-end": "diamond",
        """
        jsend = """
        },\nflowstate: {past: { fill: "#CCCCCC", "font-size": 12 },current: {fill: "yellow","font-color": "red","font-weight": "bold",},future: { fill: "#0088ff" },request: { fill: "blue" },invalid: { fill: "#58C4A3" },approved: {fill: "#C45879","font-size": 12,"yes-text": "APPROVED","no-text": "n/a",},rejected: {fill: "#C45879","font-size": 12,"yes-text": "n/a","no-text": "REJECTED",},},});})();};\n</script>
        """
        jsmid = ""
        start = "start: {class: 'start-element','element-color': '"+self.startlinecolor.text()+"','font-color':'"+self.startfontcolor.text()+"','text-margin': "+self.startmargin.text()+"},"
        end = "end: {class: 'end-element','element-color': '"+self.endlinecolor.text()+"','font-color':'"+self.endfontcolor.text()+"','text-margin': "+self.endmargin.text()+"},"
        oper = "operation: {class: 'operation-element','element-color': '"+self.operlinecolor.text()+"','font-color':'"+self.operfontcolor.text()+"','text-margin': "+self.opermargin.text()+"},"
        cond = "condition: {class: 'condition-element','element-color': '"+self.condlinecolor.text()+"','font-color':'"+self.condfontcolor.text()+"','text-margin': "+self.condmargin.text()+"},"
        inout = "inputoutput: {class: 'inputoutput-element','element-color': '"+self.inoutlinecolor.text()+"','font-color':'"+self.inoutfontcolor.text()+"','text-margin': "+self.inoutmargin.text()+"},"
        par = "parallel: {class: 'parallel-element','element-color': '"+self.parlinecolor.text()+"','font-color':'"+self.parfontcolor.text()+"','text-margin': "+self.parmargin.text()+"},"
        sub = "subroutine: {class: 'subroutine-element','element-color': '"+self.sublinecolor.text()+"','font-color':'"+self.subfontcolor.text()+"','text-margin': "+self.submargin.text()+"},"
        general = ""
        general += "roundness: "+self.genframeroud.text()+",\n"
        general += "'line-width': "+self.genframewidth.text()+",\n"
        general += "'font-size': "+self.genfontsize.text()+",\n"
        general += "'font-color': '"+self.genfontcolor.text()+"',\n"
        general += "'font-weight': "+self.genfontweight.text()+",\n"
        general += "'line-color': '"+self.genlinecolor.text()+"',\n"
        general += "'element-color': '"+self.genframecolor.text()+"',\n"
        jsmid = general+"symbols: {"+start+end+oper+cond+inout+par+sub
        return jsstart+jsmid+jsend

    def getCss(self):
        cssmid = ""
        cssmid += """
        body {background: """+self.genbackcolor.text()+""";}\n
        """
        cssmid += """
        .start-element {
            fill: """+self.startbackcolor.text()+""";
        }\n
        """
        cssmid += """
        .end-element {
            fill: """+self.endbackcolor.text()+""";
        }\n
        """
        cssmid += """
        .condition-element {
            fill: """+self.condbackcolor.text()+""";
        }\n
        """
        cssmid += """
        .operation-element {
            fill: """+self.operbackcolor.text()+""";
        }\n
        """
        cssmid += """
        .inputoutput-element {
            fill: """+self.inoutbackcolor.text()+""";
        }\n
        """
        cssmid += """
        .parallel-element {
            fill: """+self.parbackcolor.text()+""";
        }\n
        """
        cssmid += """
        .subroutine-element {
            fill: """+self.subbackcolor.text()+""";
        }\n
        """
        return "<style>\n"+cssmid+"\n</style>"

    def saveFile(self):
        pagelay = QPageLayout()
        pagelay.setPageSize(QPageSize(QPageSize.PageSizeId.B0))
        pagelay.setMode(QPageLayout.Mode.FullPageMode)
        try:
            self.browser.page().printToPdf(self.outputpath.text() +f"/flowchart{str(self.tabWidget.currentIndex())}.pdf", pageLayout=pagelay)
        except Exception as e:
            print(e)
            print("Error: Could not save file")
            exit(1)

    def openClose(self, frameName):
        if(frameName == "custom"):
            width = self.leftMenu.maximumWidth()
            if width == 0:
                newWidth = 250
            else:
                newWidth = 0
            self.animation = QPropertyAnimation(self.leftMenu, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        if(frameName == "output"):
            height = self.outputframe.maximumHeight()
            if height == 0:
                newheight = 140
            else:
                newheight = 0
            self.animation = QPropertyAnimation(
                self.outputframe, b"maximumHeight")
            self.animation.setDuration(500)
            self.animation.setStartValue(height)
            self.animation.setEndValue(newheight)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def browse_folder(self):
        self.outputpath.setText(
            abspath(QFileDialog.getExistingDirectory(self, "Hedef Klasör Seçiniz")))

    def specialHover(self):
        self.parbackcolor.textChanged.connect(lambda: self.parbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.parbackcolor.text()}"+";}"))
        self.parfontcolor.textChanged.connect(lambda: self.parfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.parfontcolor.text()}"+";}"))
        self.parlinecolor.textChanged.connect(lambda: self.parlinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.parlinecolor.text()}"+";}"))
        self.operbackcolor.textChanged.connect(lambda: self.operbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.operbackcolor.text()}"+";}"))
        self.operlinecolor.textChanged.connect(lambda: self.operlinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.operlinecolor.text()}"+";}"))
        self.operfontcolor.textChanged.connect(lambda: self.operfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.operfontcolor.text()}"+";}"))
        self.endbackcolor.textChanged.connect(lambda: self.endbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.endbackcolor.text()}"+";}"))
        self.endlinecolor.textChanged.connect(lambda: self.endlinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.endlinecolor.text()}"+";}"))
        self.endfontcolor.textChanged.connect(lambda: self.endfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.endfontcolor.text()}"+";}"))
        self.condbackcolor.textChanged.connect(lambda: self.condbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.condbackcolor.text()}"+";}"))
        self.condlinecolor.textChanged.connect(lambda: self.condlinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.condlinecolor.text()}"+";}"))
        self.condfontcolor.textChanged.connect(lambda: self.condfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.condfontcolor.text()}"+";}"))
        self.startbackcolor.textChanged.connect(lambda: self.startbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.startbackcolor.text()}"+";}"))
        self.startlinecolor.textChanged.connect(lambda: self.startlinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.startlinecolor.text()}"+";}"))
        self.startfontcolor.textChanged.connect(lambda: self.startfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.startfontcolor.text()}"+";}"))
        self.inoutbackcolor.textChanged.connect(lambda: self.inoutbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.inoutbackcolor.text()}"+";}"))
        self.inoutlinecolor.textChanged.connect(lambda: self.inoutlinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.inoutlinecolor.text()}"+";}"))
        self.inoutfontcolor.textChanged.connect(lambda: self.inoutfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.inoutfontcolor.text()}"+";}"))
        self.subbackcolor.textChanged.connect(lambda: self.subbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.subbackcolor.text()}"+";}"))
        self.sublinecolor.textChanged.connect(lambda: self.sublinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.sublinecolor.text()}"+";}"))
        self.subfontcolor.textChanged.connect(lambda: self.subfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.subfontcolor.text()}"+";}"))
        self.genframecolor.textChanged.connect(lambda: self.genframecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.genframecolor.text()}"+";}"))
        self.genlinecolor.textChanged.connect(lambda: self.genlinecolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.genlinecolor.text()}"+";}"))
        self.genfontcolor.textChanged.connect(lambda: self.genfontcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.genfontcolor.text()}"+";}"))
        self.genbackcolor.textChanged.connect(lambda: self.genbackcolor.setStyleSheet("QLineEdit:hover{background-color: "+f"{self.genbackcolor.text()}"+";}"))

if __name__ == "__main__":
    app = QApplication(argv)
    Form = Web_Builder()
    Form.show()
    exit(app.exec_())

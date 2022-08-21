from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from configuration import Configuration


def CustomizeMessageBox_Yes_No(message, clickAccept=None, clickCancel=None, yes='Evet', no='Hayır', icon=QMessageBox.Question):
    c = Configuration()
    msgBox = QMessageBox()
    msgBox.setWindowTitle('Pynar Mesaj Kutusu')
    msgBox.setWindowIcon(QIcon(':/icon/images/headerLogo1.png'))
    if(icon == QMessageBox.Question):
        icontype = "question"
    if(icon == QMessageBox.Critical):
        icontype = "critical"
    if(icon == QMessageBox.Information):
        icontype = "information"
    if(icon == QMessageBox.Warning):
        icontype = "warning"
    msgBox.setText(f"<table cellpadding='2'><tr valign='middle'><td ><img src=':icon/images/{icontype}.png'/></td><td>{message}</td></tr></table>")
    msgBox.setWindowFlags(msgBox.windowFlags() |Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    font = QFont()
    font.setFamily(c.getEditorFont())
    font.setPointSize(c.getEditorFontSize())
    msgBox.setFont(font)
    borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #ffcc00;\n"
    if icontype == "critical":
        borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #ff0000;\n"
    if icontype == "information" or icon == "question":
        borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #00ccff;\n"
    msgBox.setStyleSheet(borderstyle + open(c.getHomeDir() + "qssfiles/qmessagebox.qss", "r").read())
    BtnOk = msgBox.button(QMessageBox.Ok)
    BtnOk.setText(yes)
    BtnCancel = msgBox.button(QMessageBox.Cancel)
    BtnCancel.setText(no)
    if clickAccept:
        msgBox.accepted.connect(clickAccept)
    if clickCancel:
        msgBox.rejected.connect(clickCancel)
    msgBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    msgBox.exec()


def CustomizeMessageBox_Ok(message, icon=QMessageBox.Question):
    c = Configuration()
    msgBox = QMessageBox()
    if(icon == QMessageBox.Question):
        icontype = "question"
    if(icon == QMessageBox.Critical):
        icontype = "critical"
    if(icon == QMessageBox.Information):
        icontype = "information"
    if(icon == QMessageBox.Warning):
        icontype = "warning"
    msgBox.setText(f"<table cellpadding='2'><tr valign='middle'><td ><img src=':icon/images/{icontype}.png'/></td><td>{message}</td></tr></table>")
    msgBox.setWindowTitle('Pynar Mesaj Kutusu')
    msgBox.setWindowIcon(QIcon(':/icon/images/headerLogo1.png'))
    msgBox.setWindowFlags(msgBox.windowFlags() |Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
    msgBox.setStandardButtons(QMessageBox.Ok)
    font = QFont()
    font.setFamily(c.getEditorFont())
    font.setPointSize(c.getEditorFontSize())
    msgBox.setFont(font)
    borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #ffcc00;\n"
    if icontype == "critical":
        borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #ff0000;\n"
    if icontype == "information" or icon == "question":
        borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #00ccff;\n"
    msgBox.setStyleSheet(borderstyle + open(c.getHomeDir() + "qssfiles/qmessagebox.qss", "r").read())
    BtnOk = msgBox.button(QMessageBox.Ok)
    BtnOk.setText('Tamam')
    msgBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    msgBox.exec()


def CustomizeMessageBox_Yes_No_Cancel(message, icon=QMessageBox.Question):
    c = Configuration()
    msgBox = QMessageBox()
    msgBox.setWindowTitle('Pynar Mesaj Kutusu')
    msgBox.setWindowIcon(QIcon(':/icon/images/headerLogo1.png'))
    if(icon == QMessageBox.Question):
        icontype = "question"
    if(icon == QMessageBox.Critical):
        icontype = "critical"
    if(icon == QMessageBox.Information):
        icontype = "information"
    if(icon == QMessageBox.Warning):
        icontype = "warning"
    msgBox.setText(f"<table cellpadding='2'><tr valign='middle'><td ><img src=':icon/images/{icontype}.png'/></td><td>{message}</td></tr></table>")
    msgBox.setWindowFlags(msgBox.windowFlags() |Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
    font = QFont()
    font.setFamily(c.getEditorFont())
    font.setPointSize(c.getEditorFontSize())
    msgBox.setFont(font)
    borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #ffcc00;\n"
    if icontype == "critical":
        borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #ff0000;\n"
    if icontype == "information" or icon == "question":
        borderstyle ="QPushButton{"+f"font:{c.getEditorFontSize()}pt '{c.getEditorFont()}';"+"}\n"+"border-top: 8px solid #00ccff;\n"
    msgBox.setStyleSheet(
        borderstyle + open(c.getHomeDir() + "qssfiles/qmessagebox.qss", "r").read())
    msgBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    BtnOk = msgBox.button(QMessageBox.Yes)
    BtnOk.setText('Evet')
    BtnCancel = msgBox.button(QMessageBox.No)
    BtnCancel.setText('Hayır')
    BtnClose = msgBox.button(QMessageBox.Cancel)
    BtnClose.setText('Vazgeç')
    return msgBox

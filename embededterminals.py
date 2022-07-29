# import sys
# from PyQt5 import QtGui, QtCore,QtWidgets


# class Stream(QtCore.QObject):
#     newText = QtCore.pyqtSignal(str)

#     def write(self, text):
#         self.newText.emit(str(text))

# class Window(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(Window, self).__init__()
#         self.setGeometry(50, 50, 500, 300)
#         self.setWindowTitle("PyQT tuts!")
#         w = QtWidgets.QWidget()
#         self.setCentralWidget(w)
#         lay = QtWidgets.QVBoxLayout(w)
#         btn = QtWidgets.QPushButton("Generate")
#         btn.clicked.connect(self.TextFSM)
#         self.process  = QtWidgets.QTextEdit()
#         self.process.moveCursor(QtGui.QTextCursor.Start)
#         self.process.ensureCursorVisible()
#         self.process.setLineWrapColumnOrWidth(500)
#         self.process.setLineWrapMode(QtWidgets.QTextEdit.FixedPixelWidth)
#         lay.addWidget(btn)
#         lay.addWidget(self.process)
#         self.show()
#         sys.stdout = Stream(newText=self.onUpdateText)
#         sys.stderr = Stream(newText=self.onUpdateText)
#     def onUpdateText(self, text):
#         cursor = self.process.textCursor()
#         cursor.movePosition(QtGui.QTextCursor.End)
#         cursor.insertText(text)
#         self.process.setTextCursor(cursor)
#         self.process.ensureCursorVisible()

#     def __del__(self):
#         sys.stdout = sys.__stdout__
#         sys.stderr = sys.__stderr__

#     def TextFSM(self):
#         print(5)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     GUI = Window()
#     GUI.show()
#     sys.exit(app.exec_())
##############################################################################
##############################################################################
# from contextlib import redirect_stdout
# from io import StringIO

# from PyQt5.QtWidgets import QTextEdit
# from PyQt5.QtCore import QObject, QThread, pyqtSignal


# class EmbeddedTerminal(QTextEdit):
#     def __init__(self, parent):
#         super(EmbeddedTerminal, self).__init__(parent)

#     def run_func(self, func, *args, **kwargs):
#         self.thread = QThread()
#         self.worker = TerminalWorker(func, args, kwargs)
#         self.worker.moveToThread(self.thread)
#         self.thread.started.connect(self.worker.run)
#         self.worker.progress.connect(self.update_terminal)
#         self.thread.start()

#     def update_terminal(self, text):
#         self.setText(text)


# class TerminalWorker(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(str)

#     def __init__(self, func, args, kwargs):
#         QObject.__init__(self)
#         self.func = func
#         self.args = args
#         self.kwargs = kwargs

#     def run(self):
#         with redirect_stdout(StringIO()) as f:
#             self.func(*self.args, **self.kwargs)
#         output = f.getvalue()
#         self.progress.emit(output)
##############################################################################
##############################################################################
# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore

# class OutputWrapper(QtCore.QObject):
#     outputWritten = QtCore.pyqtSignal(object, object)

#     def __init__(self, parent, stdout=True):
#         super().__init__(parent)
#         if stdout:
#             self._stream = sys.stdout
#             sys.stdout = self
#         else:
#             self._stream = sys.stderr
#             sys.stderr = self
#         self._stdout = stdout

#     def write(self, text):
#         self._stream.write(text)
#         self.outputWritten.emit(text, self._stdout)

#     def __getattr__(self, name):
#         return getattr(self._stream, name)

#     def __del__(self):
#         try:
#             if self._stdout:
#                 sys.stdout = self._stream
#             else:
#                 sys.stderr = self._stream
#         except AttributeError:
#             pass

# class Window(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__(   )
#         widget = QtWidgets.QWidget(self)
#         layout = QtWidgets.QVBoxLayout(widget)
#         self.setCentralWidget(widget)
#         self.terminal = QtWidgets.QTextBrowser(self)
#         self._err_color = QtCore.Qt.red
#         self.button = QtWidgets.QPushButton('Test', self)
#         self.button.clicked.connect(self.handleButton)
#         layout.addWidget(self.terminal)
#         layout.addWidget(self.button)
#         stdout = OutputWrapper(self, True)
#         stdout.outputWritten.connect(self.handleOutput)
#         stderr = OutputWrapper(self, False)
#         stderr.outputWritten.connect(self.handleOutput)

#     def handleOutput(self, text, stdout):
#         color = self.terminal.textColor()
#         self.terminal.moveCursor(QtGui.QTextCursor.End)
#         self.terminal.setTextColor(color if stdout else self._err_color)
#         self.terminal.insertPlainText(text)
#         self.terminal.setTextColor(color)

#     def handleButton(self):
#         if QtCore.QTime.currentTime().second() % 2:
#             print('Printing to stdout...')
#         else:
#             print('Printing to stderr...', file=sys.stderr)

# if __name__ == '__main__':

#     app = QtWidgets.QApplication(sys.argv)
#     window = Window()
#     window.setGeometry(500, 300, 300, 200)
#     window.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5 import QtCore, QtWidgets


# class EmbTerminal(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(EmbTerminal, self).__init__(parent)
#         self.process = QtCore.QProcess(self)
#         self.terminal = QtWidgets.QWidget(self)
#         layout = QtWidgets.QVBoxLayout(self)
#         layout.addWidget(self.terminal)
#         # Works also with urxvt:
#         self.process.start('urxvt',['-embed', str(int(self.winId()))])
#         self.setFixedSize(640, 480)


# class mainWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super(mainWindow, self).__init__(parent)

#         central_widget = QtWidgets.QWidget()
#         lay = QtWidgets.QVBoxLayout(central_widget)
#         self.setCentralWidget(central_widget)

#         tab_widget = QtWidgets.QTabWidget()
#         lay.addWidget(tab_widget)

#         tab_widget.addTab(EmbTerminal(), "EmbTerminal")
#         tab_widget.addTab(QtWidgets.QTextEdit(), "QTextEdit")
#         tab_widget.addTab(QtWidgets.QMdiArea(), "QMdiArea")


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     main = mainWindow()
#     main.show()
#     sys.exit(app.exec_())

# class PlainTextEdit(QPlainTextEdit):
#     commandSignal = pyqtSignal(str)
#     commandZPressed = pyqtSignal(str)

#     def __init__(self, parent=None, movable=False):
#         super().__init__(parent)

#         self.name = "[" + str(getpass.getuser()) + "@" + str(socket.gethostname()) + "]" + "  ~" + str(
#             os.getcwd()) + " >$ "
#         self.appendPlainText(self.name)
#         self.movable = movable
#         self.parent = parent
#         self.commands = []
#         self.tracker = 0
#         self.setStyleSheet(
#             "QPlainTextEdit{background-color: #212121; color: white; padding: 8;}")
#         self.font = QFont()
#         self.font.setFamily("Iosevka")
#         self.font.setPointSize(12)
#         self.text = None
#         self.setFont(self.font)
#         self.document_file = self.document()
#         self.previousCommandLength = 0
#         self.document_file.setDocumentMargin(-1)

#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())

#     def mousePressEvent(self, event):
#         if self.movable is True:
#             self.parent.mousePressEvent(event)

#     def mouseMoveEvent(self, event):
#         if self.movable is True:
#             self.parent.mouseMoveEvent(event)

#     def textUnderCursor(self):
#         textCursor = self.textCursor()
#         textCursor.select(QTextCursor.WordUnderCursor)

#         return textCursor.selectedText()

#     def keyPressEvent(self, e):
#         cursor = self.textCursor()

#         if self.parent:

#             if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_A:
#                 return

#             if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Z:
#                 self.commandZPressed.emit("True")
#                 return

#             if e.key() == 16777220:  # This is the ENTER key
#                 text = self.textCursor().block().text()

#                 # This is to prevent adding in commands that were not meant to be added in
#                 if text == self.name + text.replace(self.name, "") and text.replace(self.name, "") != "":
#                     self.commands.append(text.replace(self.name, ""))
#                 self.commandSignal.emit(text)
#                 self.appendPlainText(self.name)

#                 return

#             if e.key() == Qt.Key_Up:
#                 try:
#                     if self.tracker != 0:
#                         cursor.select(QTextCursor.BlockUnderCursor)
#                         cursor.removeSelectedText()
#                         self.appendPlainText(self.name)

#                     self.insertPlainText(self.commands[self.tracker])
#                     self.tracker += 1

#                 except IndexError:
#                     self.tracker = 0

#                 return

#             if e.key() == Qt.Key_Down:
#                 try:
#                     cursor.select(QTextCursor.BlockUnderCursor)
#                     cursor.removeSelectedText()
#                     self.appendPlainText(self.name)

#                     self.insertPlainText(self.commands[self.tracker])
#                     self.tracker -= 1

#                 except IndexError:
#                     self.tracker = 0

#             if e.key() == 16777219:
#                 if cursor.positionInBlock() <= len(self.name):
#                     return

#                 else:
#                     cursor.deleteChar()

#             super().keyPressEvent(e)

#         e.accept()


# class Terminal(QWidget):
#     errorSignal = pyqtSignal(str)
#     outputSignal = pyqtSignal(str)

#     def __init__(self, parent, movable=False):
#         super().__init__()

#         self.setWindowFlags(
#             Qt.Widget |
#             Qt.WindowCloseButtonHint |
#             Qt.WindowStaysOnTopHint |
#             Qt.FramelessWindowHint
#         )
#         self.movable = movable
#         self.layout = QVBoxLayout()
#         self.pressed = False
#         self.process = QProcess()
#         self.parent = parent
#         self.name = None
#         self.setGeometry(0, 0, 300,300)
#         self.process.readyReadStandardError.connect(
#             self.onReadyReadStandardError)
#         self.process.readyReadStandardOutput.connect(
#             self.onReadyReadStandardOutput)
#         self.setLayout(self.layout)
#         self.setStyleSheet("QWidget {background-color:invisible;}")

#         # self.showMaximized() # comment this if you want to embed this widget

#     def ispressed(self):
#         return self.pressed

#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())

#     def add(self):
#         self.added()
#         self.button = QPushButton("Hide terminal")
#         self.button.setFont(QFont("Iosevka", 11))
#         self.button.setStyleSheet("""
#         height: 20;
#         background-color: #212121;
        
#         """)
#         self.button.setFixedWidth(120)
#         self.editor = PlainTextEdit(self, self.movable)
#         self.highlighter = name_highlighter(self.editor.document(), str(getpass.getuser()), str(socket.gethostname()),
#                                             str(os.getcwd()))
#         self.layout.addWidget(self.button)
#         self.layout.addWidget(self.editor)
#         self.editor.commandSignal.connect(self.handle)
#         self.button.clicked.connect(self.remove)
#         self.editor.commandZPressed.connect(self.handle)

#     def added(self):
#         self.pressed = True

#     def remove(self):
#         self.editor.deleteLater()
#         self.button.deleteLater()
#         self.parent.hideConsole()
#         self.pressed = False

#     def onReadyReadStandardError(self):
#         self.error = self.process.readAllStandardError().data().decode()
#         self.editor.appendPlainText(self.error.strip('\n'))
#         self.errorSignal.emit(self.error)

#     def onReadyReadStandardOutput(self):
#         self.result = self.process.readAllStandardOutput().data().decode()
#         self.editor.appendPlainText(self.result.strip('\n'))
#         self.state = self.process.state()
#         self.outputSignal.emit(self.result)

#     def run(self, command):
#         """Executes a system command."""
#         if self.process.state() != 2:
#             self.process.start(command)

#     def handle(self, command):
#         """Split a command into list so command echo hi would appear as ['echo', 'hi']"""
#         real_command = command.replace(self.editor.name, "")

#         if command == "True":
#             if self.process.state() == 2:
#                 self.process.kill()
#                 self.editor.appendPlainText(
#                     "Program execution killed, press enter")

#         if real_command.startswith("python"):
#             pass

#         if real_command != "":
#             command_list = real_command.split()
#         else:
#             command_list = None
#         if real_command == "clear":
#             self.editor.clear()

#         elif command_list is not None and command_list[0] == "echo":
#             self.editor.appendPlainText(" ".join(command_list[1:]))

#         elif real_command == "exit":
#             self.remove()

#         elif command_list is not None and command_list[0] == "cd" and len(command_list) > 1:
#             try:
#                 os.chdir(" ".join(command_list[1:]))
#                 self.editor.name = "[" + str(getpass.getuser()) + "@" + str(socket.gethostname()) + "]" + "  ~" + str(
#                     os.getcwd()) + " >$ "
#                 if self.highlighter:
#                     del self.highlighter
#                 self.highlighter = name_highlighter(self.editor.document(), str(getpass.getuser()),
#                                                     str(socket.gethostname()), str(os.getcwd()))

#             except FileNotFoundError as E:
#                 self.editor.appendPlainText(str(E))

#         elif command_list is not None and len(command_list) == 1 and command_list[0] == "cd":
#             os.chdir(str(Path.home()))
#             self.editor.name = "[" + str(getpass.getuser()) + "@" + str(socket.gethostname()) + "]" + "  ~" + str(
#                 os.getcwd()) + " >$ "

#         elif self.process.state() == 2:
#             self.process.write(real_command.encode())
#             self.process.closeWriteChannel()

#         elif command == self.editor.name + real_command:
#             self.run(real_command)

#         else:
#             pass


# class name_highlighter(QSyntaxHighlighter):

#     def __init__(self, parent=None, user_name=None, host_name=None, cwd=None):
#         super().__init__(parent)
#         self.highlightingRules = []
#         self.name = user_name
#         self.name2 = host_name
#         self.cwd = cwd
#         most_used = ["cd", "clear", "history", "ls", "man", "pwd", "what", "type",
#                      "strace", "ltrace", "gdb", "cat", "chmod", "cp", "chown", "find", "grep", "locate", "mkdir",
#                      "rmdir", "rm", "mv", "vim", "nano", "rename",
#                      "touch", "wget", "zip", "tar", "gzip", "apt", "bg", "fg", "df", "free", "ip", "jobs", "kill",
#                      "killall", "mount", "umount", "ps", "sudo", "echo",
#                      "top", "uname", "whereis", "uptime", "whereis", "whoami", "exit"
#                      ]  # most used linux commands, so we will highlight them!
#         self.regex = {
#             "class": "\\bclass\\b",
#             "function": "[A-Za-z0-9_]+(?=\\()",
#             "magic": "\\__[^']*\\__",
#             "decorator": "@[^\n]*",
#             "singleLineComment": "#[^\n]*",
#             "quotation": "\"[^\"]*\"",
#             "quotation2": "'[^\']*\'",
#             "multiLineComment": "[-+]?[0-9]+",
#             "int": "[-+]?[0-9]+",
#         }
#         """compgen -c returns all commands that you can run"""

#         for f in most_used:
#             nameFormat = QTextCharFormat()
#             nameFormat.setForeground(QColor("#00ff00"))
#             nameFormat.setFontItalic(True)
#             self.highlightingRules.append(
#                 (QRegExp("\\b" + f + "\\b"), nameFormat))

#         hostnameFormat = QTextCharFormat()
#         hostnameFormat.setForeground(QColor("#12c2e9"))
#         self.highlightingRules.append((QRegExp(self.name), hostnameFormat))
#         self.highlightingRules.append((QRegExp(self.name2), hostnameFormat))

#         otherFormat = QTextCharFormat()
#         otherFormat.setForeground(QColor("#f7797d"))
#         self.highlightingRules.append((QRegExp("~\/[^\s]*"), otherFormat))

#         quotation1Format = QTextCharFormat()
#         quotation1Format.setForeground(QColor("#96c93d"))
#         self.highlightingRules.append(
#             (QRegExp("\"[^\"]*\""), quotation1Format))

#         quotation2Format = QTextCharFormat()
#         quotation2Format.setForeground(QColor("#96c93d"))
#         self.highlightingRules.append((QRegExp("'[^\']*\'"), quotation2Format))

#         integerFormat = QTextCharFormat()
#         integerFormat.setForeground(QColor("#cc5333"))
#         integerFormat.setFontItalic(True)
#         self.highlightingRules.append(
#             (QRegExp("\\b[-+]?[0-9]+\\b"), integerFormat))

#     def highlightBlock(self, text):

#         for pattern, format in self.highlightingRules:
#             expression = QRegExp(pattern)
#             index = expression.indexIn(text)
#             while index >= 0:
#                 length = expression.matchedLength()
#                 self.setFormat(index, length, format)
#                 index = expression.indexIn(text, index + length)

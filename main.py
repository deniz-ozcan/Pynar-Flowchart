import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QAction,
    QSizeGrip,
    QTextEdit
)
from PyQt5.QtGui import (
    QIcon,
    QFont,
    QFontMetrics,
    QColor,
    QPixmap,
    QTextCursor,

)
from PyQt5.QtCore import (
    Qt,
    QPropertyAnimation,
    QEasingCurve,
    QObject,
    pyqtSignal,
    QCoreApplication,
)
from debug import Ui_Debug
from os.path import join, dirname
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
import io
from logging import getLogger, DEBUG
LOGGER = getLogger('HelpUs')
LOGGER.setLevel(DEBUG)


class PythonLexer(QsciLexerPython):
    def __init__(self):
        super().__init__()

    def keywords(self, index):
        keywords = QsciLexerPython.keywords(self, index) or ''
        if index == 1:
            return 'self '+'super ' + keywords


class XStream(QObject):
    _stdout = None
    _stderr = None
    messageWritten = pyqtSignal(str)

    @staticmethod
    def flush():
        pass

    @staticmethod
    def fileno():
        return -1

    def write(self, msg):
        if not self.signalsBlocked():
            self.messageWritten.emit(msg)

    @staticmethod
    def stdout():
        if not XStream._stdout:
            XStream._stdout = XStream()
            sys.stdout = XStream._stdout
        return XStream._stdout

    @staticmethod
    def stderr():
        if not XStream._stderr:
            XStream._stderr = XStream()
            sys.stderr = XStream._stderr
        return XStream._stderr

# pyuic5 C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\debug.ui -o C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\debug.py
# pyrcc5 C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\icons.qrc -o C:\Users\sauda\Masaüstü\SOFTWARE\WINDOWS\PyNar\ZDebug\icons_rc.py
# pyinstaller --onefile -w -i .\Brand.png .\_0BankApplication.py


class CodeEditor(QsciScintilla):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.filename = None
        self.fileBrowser = None
        self.mainWindow = parent
        self.debugging = False
        self.pointSize = 13
        self.tabWidth = 4
        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical{border-radius:5px;background:transparent;width:10px;margin:0}QScrollBar::handle:vertical{border-radius:5px;background:#88888888;min-width:5px;max-width:5px;min-height:50px;max-height:50px;width:5px;height:5px}QScrollBar::handle:vertical:hover{background:#888}QScrollBar::add-line:vertical{height:0;subcontrol-position:bottom;subcontrol-origin:margin}QScrollBar::sub-line:vertical{height:0;subcontrol-position:top;subcontrol-origin:margin}QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{background:transparent;border-radius:6px;}")
        self.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal{border-radius:5px;background:transparent;height:10px;margin:0}QScrollBar::handle:horizontal{border-radius:5px;background:#88888888;min-width:50px;max-width:50px;min-height:5px;max-height:5px;width:5px;height:5px}QScrollBar::handle:horizontal:hover{background:#888}QScrollBar::add-line:horizontal{height:0;subcontrol-position:bottom;subcontrol-origin:margin}QScrollBar::sub-line:horizontal{height:0;subcontrol-position:top;subcontrol-origin:margin}QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{background:transparent;border-radius:6px;}")
        self.setMatchedBraceBackgroundColor(QColor('#1e1e1e'))
        self.setMatchedBraceForegroundColor(QColor('green'))
        self.setUnmatchedBraceBackgroundColor(QColor('#1e1e1e'))
        self.setUnmatchedBraceForegroundColor(QColor('red'))
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setEdgeColor(QColor('#1e1e1e'))
        self.font = QFont()
        self.font.setFamily('Consolas')
        self.font.setFixedPitch(True)
        self.font.setPointSize(self.pointSize)
        self.setFont(self.font)
        file_path = join(dirname(__file__), "./main.py")
        self.setText(open(file_path, encoding="utf-8").read())
        fontmetrics = QFontMetrics(self.font)
        self.setMarginsFont(self.font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 5)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#1e1e1e"))
        self.setMarginsForegroundColor(QColor("#858585"))
        self.setMarginSensitivity(1, True)
        self.markericon = QPixmap(":/icons/icons/checkbox2.svg")
        self.markerDefine(self.markericon, 8)
        self.breakpoint = False
        self.breakpointLine = None
        self.setFoldMarginColors(QColor('#1e1e1e'), QColor('#1e1e1e'))
        self.SendScintilla(QsciScintilla.SCI_SETCARETFORE, QColor('#1e1e1e'))
        self.setCaretWidth(0)
        self.setIndentationsUseTabs(False)
        self.setTabWidth(self.tabWidth)
        self.SendScintilla(QsciScintilla.SCI_SETUSETABS, False)
        self.setAutoIndent(True)
        self.setTabIndents(True)
        self.setBackspaceUnindents(True)
        self.setMinimumSize(300, 300)
        self.style = None
        self.style = 'Python'
        self.setAutoIndent(True)
        self.lexer = PythonLexer()
        self.lexer.setFont(self.font)
        self.lexer.setFoldComments(True)
        self.setLexer(self.lexer)
        self.setCaretLineBackgroundColor(QColor("#1E1E1E"))
        self.lexer.setDefaultPaper(QColor("#1E1E1E"))
        self.lexer.setDefaultColor(QColor("#D4D4D4"))
        self.lexer.setColor(QColor('#D4D4D4'), 0)  # default
        self.lexer.setPaper(QColor('#1E1E1E'), -1)  # default
        self.lexer.setColor(QColor('#6A9955'), 1)  # comment
        self.lexer.setColor(QColor('#B5CEA8'), 2)  # Number
        self.lexer.setColor(QColor('#CE9178'), 3)  # DoubleQuotedString
        self.lexer.setColor(QColor('#CE9178'), 4)  # SingleQuotedString
        self.lexer.setColor(QColor('#569cd6'), 5)  # Keyword
        self.lexer.setColor(QColor('#CE9178'), 6)  # TripleSingleQuotedString
        self.lexer.setColor(QColor('#CE9178'), 7)  # TripleDoubleQuotedString
        self.lexer.setColor(QColor('#4EC9B0'), 8)  # ClassName
        self.lexer.setColor(QColor('#FFFFAA'), 9)  # FunctionMethodName
        self.lexer.setColor(QColor('#C586C0'), 10)  # Operator
        self.lexer.setColor(QColor('#9CDCFE'), 11)  # Identifier
        self.lexer.setColor(QColor('#6AFF55'), 12)  # CommentBlock
        self.lexer.setColor(QColor('#ff471a'), 13)  # UnclosedString
        self.lexer.setColor(QColor('#CE9178'), 14)  # HighlightedIdentifier
        self.lexer.setColor(QColor('#5DD3AF'), 15)  # Decorator
        self.lexer.setColor(QColor('#CE9178'), 16)  # DoubleQuotedFString
        self.lexer.setColor(QColor('#CE9178'), 17)  # SingleQuotedFString
        self.lexer.setColor(QColor('#CE9178'), 18)  # TripleSingleQuotedFString
        self.lexer.setColor(QColor('#CE9178'), 19)  # TripleDoubleQuotedFString
        self.setFold()
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        breakpointAction = QAction("", self)
        breakpointAction.triggered.connect(self.breakpointContext)
        self.addAction(breakpointAction)
        self.marginClicked.connect(self.onMarginClicked)
        self.setReadOnly(True)

    def onMarginClicked(self, margin, line, modifiers):
        if self.markersAtLine(line) != 0:
            self.markerDelete(line, 8)
            print(f"cl {join(dirname(__file__), './main.py')}:{line+1} ", end = "")
        else:
            self.markerAdd(line, 8)
            print(f"b {line + 1} ", end = "")

    def breakpointContext(self):
        code = ''
        lines = self.lines()
        if self.breakpointLine:
            for i in range(lines):
                if i < self.breakpointLine:
                    code += self.text(i)

    def setFold(self):
        x = self.FoldStyle(self.FoldStyle(4))
        if not x:
            self.foldAll(False)
        self.setFolding(x)


class MainWindow(QMainWindow, Ui_Debug):
    _stdout = None
    _stderr = None
    messageWritten = pyqtSignal(str)

    HOOK_HEADER = '(Pdb) '
    HOOK_INTERACT = '>>> '
    HOOK_LINE_BREAK = '... '
    HOOKS = [HOOK_HEADER, HOOK_INTERACT]

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.codeToShow()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.closeBut.clicked.connect(self.close)
        self.minimize.clicked.connect(self.restoreOrMaximized)
        self.downBut.clicked.connect(self.showMinimized)
        self.header.mouseMoveEvent = self.moveWindow

        self.button_help.clicked.connect(self.helpMenu)
        QSizeGrip(self.sizegrip)
        self.console = QTextEdit(parent)
        
        self.console.setStyleSheet(
            "border-radius:6px;background-color:#1e1e1e;color:white;	font: 400 10pt 'Segoe UI';")
        self.console.insertPlainText = self.__insert_plain_text
        self.console.keyPressEvent = self.__key_press_event
        self.horizontalLayout_14.addWidget(self.console)
        self.button_step.clicked.connect(self.__push_button)
        self.button_next.clicked.connect(self.__push_button)
        self.button_return.clicked.connect(self.__push_button)
        self.button_continue.clicked.connect(self.__push_button)
        self.buffer = io.StringIO()
        self.__set_enable_gui(False)
        self.showNormal()

    def __set_enable_gui(self, state=True):
        # self.console.setEnabled(state)
        self.button_step.setEnabled(state)
        self.button_next.setEnabled(state)
        self.button_return.setEnabled(state)
        self.button_continue.setEnabled(state)
        if state:
            self.console.setFocus()

    def redirect_outerr_stream(self):
        XStream.stdout().messageWritten.connect(self.console.insertPlainText)
        XStream.stderr().messageWritten.connect(self.console.insertPlainText)

    def readline(self):
        if not self.console.isEnabled():
            self.__set_enable_gui(True)
        self.__reset_buffer()
        while self.buffer.tell() == 0:
            QCoreApplication.processEvents()
        value = self.buffer.getvalue()
        return value

    def __key_press_event(self, event):
        # Get Last Line of console
        document = self.console.document()
        line_index = document.lineCount()
        raw_last_line = document.findBlockByLineNumber(line_index - 1).text()

        text = ''
        current_hook = ''
        # Exclude first 6 chars: (Pdb)\s
        if raw_last_line:
            for hook in self.HOOKS:
                if raw_last_line.startswith(hook):
                    current_hook = hook
                    text = raw_last_line[len(hook):]
                    break
            else:
                text = raw_last_line

        # Get Cursor position
        line_from_zero = line_index - 1
        current_cursor_line = self.console.textCursor().blockNumber()
        current_cursor_column = self.console.textCursor().columnNumber()

        # If Enter was pressed -> Process Expression
        if event.key() == Qt.Key.Key_Return and text:
            # Consider Custom Clear Screen Command
            if text == 'cls':
                self.__clear_screen(raw_last_line)
                return
            # Replace Line Break with Enter
            if self.HOOK_LINE_BREAK == text:
                text = '\r\n'
            elif self.HOOK_LINE_BREAK in text:
                # Replace Line Break with tab
                text = text.replace(self.HOOK_LINE_BREAK, '\t')
                current_hook = self.HOOK_LINE_BREAK

            self.__reset_buffer()
            self.buffer.write(text)
            self.__set_enable_gui(False)

        # If User want to delete something and there is no value in buffer -> Reject
        if event.key() == Qt.Key.Key_Backspace or event.key() == Qt.Key.Key_Delete:
            if current_cursor_line != line_from_zero or current_cursor_column <= len(current_hook):
                return

        if event.key() == Qt.Key.Key_Home and current_cursor_line == line_from_zero:
            if text:
                temp_cursor = self.console.textCursor()
                temp_cursor.movePosition(
                    QTextCursor.MoveOperation.StartOfLine,
                    QTextCursor.MoveMode.MoveAnchor
                )
                temp_cursor.movePosition(
                    QTextCursor.MoveOperation.Right,
                    QTextCursor.MoveMode.MoveAnchor,
                    len(current_hook)
                )
                self.console.setTextCursor(temp_cursor)
            return

        # Set Console Text to Black
        self.console.setTextColor(Qt.GlobalColor.white)
        # Execute default method
        QTextEdit.keyPressEvent(self.console, event)

    def __push_button(self):

        button_scope = self.sender().text().lower()
        self.__reset_buffer()
        self.buffer.write(button_scope)
        self.__set_enable_gui(False)

    def __reset_buffer(self):
        if isinstance(self.buffer, io.StringIO):
            self.buffer.truncate(0)
            self.buffer.seek(0)
        else:
            self.buffer = io.StringIO()

    def __insert_plain_text(self, message):
        if message.startswith(self.HOOK_HEADER):
            self.console.setTextColor(Qt.GlobalColor.magenta)
            QTextEdit.insertPlainText(self.console, message)
            return
        elif message.startswith(self.HOOK_INTERACT):
            self.console.setTextColor(Qt.GlobalColor.darkMagenta)
            QTextEdit.insertPlainText(self.console, message)
            return
        elif message.startswith('b'):
            self.console.setTextColor(Qt.GlobalColor.green)
            QTextEdit.insertPlainText(self.console,message)
            self.__reset_buffer()
            self.buffer.write(message)
            self.__set_enable_gui(False)
            return
        elif message.startswith('cl'):
            self.console.setTextColor(Qt.GlobalColor.yellow)
            QTextEdit.insertPlainText(self.console,message)
            self.__reset_buffer()
            self.buffer.write(message)
            self.__set_enable_gui(False)
            return
        if message.startswith('***'):
            self.console.setTextColor(Qt.GlobalColor.red)

        QTextEdit.insertPlainText(self.console,message)
        self.console.verticalScrollBar().setValue(
            self.console.verticalScrollBar().maximum())

    def __clear_screen(self, text):
        current_hook = text
        for hook in self.HOOKS:
            if hook in current_hook:
                current_hook = hook
                break
        self.console.clear()
        self.console.insertPlainText(current_hook)

    def codeToShow(self):
        editor = CodeEditor()
        self.tabWidget.addTab(editor, "")

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


def get_qtconsole_object():
    if isinstance(sys.stdin, MainWindow):
        return sys.stdin.console
    else:
        return MainWindow.console


def setup_breakpoint_hook(parent, method, redirect_streams=False):
    def __method(*args, **kwargs):
        breakpoint()
        return method(*args, **kwargs)

    if not isinstance(sys.stdin, MainWindow):
        sys.stdin = MainWindow(parent)

    if redirect_streams:
        sys.stdin.redirect_outerr_stream()
    return __method


if __name__ == '__main__':
    app = QApplication(sys.argv)
    LOGGER.error('')
    LOGGER.error = setup_breakpoint_hook(
        None, LOGGER.error, redirect_streams=True)
    LOGGER.error('')
    sys.exit(app.exec_())

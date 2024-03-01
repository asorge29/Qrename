from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import QtGui
from .ui.window import Ui_Form
from os import path

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self._setupUI()
        self._connectSignals()
        self._fileQueue = []

    def _setupUI(self):
        self.setupUi(self)
        self._stateNoFiles()

    def _connectSignals(self):
        self.loadButton.clicked.connect(self._loadFiles)
        self.newName.textChanged.connect(self._enableRename)

    def _stateNoFiles(self):
        self.renameButton.setDisabled(True)
        self.imageDisplay.setText("No files selected.")
        self.newName.setDisabled(True)

    def _stateNewFiles(self):
        self.newName.setEnabled(True)
        self.imageDisplay.setPixmap(QtGui.QPixmap(self._fileQueue[0]))

    def _enableRename(self):
        self.renameButton.setEnabled(True)

    def _loadFiles(self):
        self._fileQueue = QFileDialog.getOpenFileNames(self, 'select files to rename.', path.expanduser('~'), "Image files (*.png *.jpg *.bmp *.jpeg)")[0]
        if len(self._fileQueue) > 0:
            self._stateNewFiles()
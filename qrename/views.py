from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import QtGui
from .ui.window import Ui_Form
from pathlib import Path

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self._fileQueue = []
        self._queueSize = len(self._fileQueue)
        self._currentFile = None
        self.setWindowIcon(QtGui.QIcon("Qrename_Logo.jpeg"))
        self._setupUI()
        self._connectSignals()

    def _setupUI(self):
        self.setupUi(self)
        self._stateNoFiles()

    def _connectSignals(self):
        self.loadButton.clicked.connect(self._loadFiles)
        self.newName.textChanged.connect(self._enableRename)
        self.renameButton.clicked.connect(self._renameFile)
        self.newName.returnPressed.connect(self._renameFile)

    def _stateNoFiles(self):
        self.renameButton.setDisabled(True)
        self.imageDisplay.setText("No files selected.")
        self.newName.setDisabled(True)
        self.itemsRemaining.setText(f"Remaining in Queue: {self._queueSize}")

    def _stateNewFiles(self):
        self.newName.setEnabled(True)
        self.imageDisplay.setPixmap(QtGui.QPixmap(str(self._currentFile)))
        self.imageDisplay.setScaledContents(True)
        self.itemsRemaining.setText(f"Remaining in Queue: {self._queueSize - 1}")

    def _enableRename(self):
        self.renameButton.setEnabled(True)

    def _loadFiles(self):
        self._fileQueue = QFileDialog.getOpenFileNames(self, 'select files to rename.', str(Path.home()), "Image files (*.png *.jpg *.bmp *.jpeg)")[0]
        self._fileQueue = [Path(file) for file in self._fileQueue]
        self._queueSize = len(self._fileQueue)
        if self._queueSize > 0:
            self._currentFile = self._fileQueue[0]
            self._stateNewFiles()

    def _renameFile(self):
        self._currentFile.rename(self._currentFile.parent.joinpath(f'{self.newName.text()}{self._currentFile.suffix}'))
        self._nextFile()

    def _nextFile(self):
        self._fileQueue.pop(0)
        self._queueSize = len(self._fileQueue)
        self.newName.setText('')
        if self._queueSize == 0:
            self._stateNoFiles()
        else:
            self._currentFile = self._fileQueue[0]
            self.imageDisplay.setPixmap(QtGui.QPixmap(str(self._currentFile)))
            self.itemsRemaining.setText(f'Remaining in Queue: {self._queueSize - 1}')
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore
from .ui.window import Ui_Form
from pathlib import Path
import sys, os

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self._fileQueue = []
        self._queueSize = len(self._fileQueue)
        self._currentFile = None
        try:
            wd = sys._MEIPASS
        except AttributeError:
            wd = os.getcwd()
        qrenameLogoPath = os.path.join(wd, "Qrename_Logo.jpeg")
        self.setWindowIcon(QtGui.QIcon(qrenameLogoPath))
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
        self.deleteButton.clicked.connect(self._deleteFile)
        self.newName.textChanged.connect(self._validatePrefixChars)

    def _stateNoFiles(self):
        self.renameButton.setDisabled(True)
        self.imageDisplay.setText("No files selected.")
        self.newName.setDisabled(True)
        self.itemsRemaining.setText(f"Remaining in Queue: {self._queueSize}")

    def _stateNewFiles(self):
        self.newName.setEnabled(True)
        newImage = QtGui.QPixmap(str(self._currentFile))
        w, h = self.imageDisplay.width(), self.imageDisplay.height()
        self.imageDisplay.setPixmap(newImage.scaled(w, h, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
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
        if not Path.exists(self._currentFile.parent.joinpath(f'{self.newName.text()}{self._currentFile.suffix}')):
            self._currentFile.rename(self._currentFile.parent.joinpath(f'{self.newName.text()}{self._currentFile.suffix}'))
        else:
            count = 1
            while True:
                if not Path.exists(self._currentFile.parent.joinpath(f'{self.newName.text()}({count}){self._currentFile.suffix}')):
                    self._currentFile.rename(self._currentFile.parent.joinpath(f'{self.newName.text()}({count}){self._currentFile.suffix}'))
                    break
                else:
                    count += 1
        self._nextFile()

    def _nextFile(self):
        self._fileQueue.pop(0)
        self._queueSize = len(self._fileQueue)
        self.newName.setText('')
        if self._queueSize == 0:
            self._stateNoFiles()
            self._currentFile = None
        else:
            self._currentFile = self._fileQueue[0]
            newImage = QtGui.QPixmap(str(self._currentFile))
            w, h = self.imageDisplay.width(), self.imageDisplay.height()
            self.imageDisplay.setPixmap(newImage.scaled(w, h, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
            self.itemsRemaining.setText(f'Remaining in Queue: {self._queueSize - 1}')

    def _deleteFile(self):
        if self._currentFile != None:
            self._currentFile.unlink()
            self._nextFile()
    
    def _validatePrefixChars(self):
        #check for characters that are not allowed in file names
        prefix = self.newName.text()
        invalidCharacters = '"\/:*?"<>|'
        for i in invalidCharacters:
            if i in prefix:
                self._spawnMessageBox(
                    "Invalid Prefix",
                    f"The prefix cannot contain the following characters: {invalidCharacters}"
                )
                self.newName.clear()
                self.newName.setFocus(True)
                break

    def _spawnMessageBox(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()
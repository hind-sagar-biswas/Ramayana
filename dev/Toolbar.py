from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QLabel, QToolBar
from PyQt5.QtGui import QIcon
import sys

class Toolbar(QToolBar):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.reader = self.app.reader

        self.setup_widget()
        
    def setup_widget(self):
        # Read tool
        read_tool = QAction('Read aloud', self)
        read_tool.triggered.connect(self.initiate_reading)
        self.addAction(read_tool)
        
    def initiate_reading(self):
       self.reader.read()

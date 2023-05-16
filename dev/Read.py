import pyttsx3
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class Read(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.button = QPushButton("Read Text", self)
        self.button.clicked.connect(self.read)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def set_text(self, text):
        self.text_to_read = text

    def read(self):
        self.engine.say(self.text_to_read)
        self.engine.runAndWait()
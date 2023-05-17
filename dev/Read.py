import pyttsx3
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class Read(QWidget):
    def __init__(self):
        super().__init__()

        self.text_to_read = "Nothinng found to read."
        self.running = False
        self.single = True

        # self.setup_widget()
        self.setup_engine()

    def setup_widget(self):
        layout = QVBoxLayout(self)
        self.button = QPushButton("Read Text", self)
        self.button.clicked.connect(self.read)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def setup_engine(self):
        self.stop(True)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)
        self.engine.connect('finished-utterance', self.on_utterance_finished)

    def set_text(self, text):
        self.text_to_read = text

    def read(self):
        self.stop()
        self.engine.say(self.text_to_read)
        if not self.running: self.engine.startLoop()
        self.running = True

    def pause(self):
        if self.running:
            self.engine.pause()

    def stop(self, close=False):
        if self.running:
            self.engine.stop()
            if close: self.engine.endLoop()
            self.running = False

    def resume(self):
        if self.running:
            self.engine.resume()

    def renew(self, text):
        self.setup_engine()
        self.set_text(text)

    def on_utterance_finished(self, name, completed):
        self.running = False
        self.engine.endLoop()
        print("Finished reading", name, completed)
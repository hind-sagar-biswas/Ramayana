import pyttsx3
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class TTSWorker(QThread):
    finished = pyqtSignal()

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.engine = None

    def run(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)
        self.engine.connect('finished-utterance', self.on_utterance_finished)
        self.engine.say(self.text)
        if not self.engine._inLoop:
            self.engine.startLoop()

    def on_utterance_finished(self, name, completed):
        self.engine.endLoop()
        self.finished.emit()

class Read(QWidget):
    def __init__(self):
        super().__init__()

        self.text_to_read = "Nothinng found to read."
        self.running = False
        self.single = True
        self.worker = None

        self.setup_widget()

    def setup_widget(self):
        layout = QVBoxLayout(self)
        self.button = QPushButton("Read Text", self)
        self.button.clicked.connect(self.read)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def set_text(self, text):
        self.text_to_read = text

    def read(self):
        print("reading", self.running)
        self.stop()
        self.worker = TTSWorker(self.text_to_read)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()
        self.running = True

    def stop(self):
        print("Going to stop")
        if self.running and self.worker is not None:
            print("stopped")
            if self.worker.isRunning():
                self.worker.terminate()
            self.worker.finished.disconnect(self.on_finished)
            self.worker = None
        self.running = False

    def on_finished(self):
        self.running = False
        print("Finished reading")
        # Perform any additional actions after reading is finished

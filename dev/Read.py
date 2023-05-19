import pyttsx3
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class TTSWorker(QThread):
    finished = pyqtSignal()

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.engine = None

    def set_text(self, text):
        self.text = text

    def run(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)
        self.engine.connect('finished-utterance', self.on_utterance_finished)
        self.engine.say(self.text)
        if not self.engine._inLoop:
            self.engine.startLoop()

    def on_utterance_finished(self, name, completed):
        self.engine.stop()
        self.engine.endLoop()
        self.finished.emit()
        self.worker.join()

class Read(QWidget):
    def __init__(self):
        super().__init__()

        self.text_to_read = "Nothinng found to read."
        self.worker = TTSWorker(self.text_to_read)

        self.running = False
        self.single = True
        self.debug = True

        self.setup_widget()

    def setup_widget(self):
        layout = QVBoxLayout(self)

        self.button_read = QPushButton("Read Text", self)
        self.button_read.clicked.connect(lambda: self.log("Read", self.read))
        layout.addWidget(self.button_read)

        self.button_stop = QPushButton("Stop Read", self)
        self.button_stop.clicked.connect(lambda: self.log("Stop", self.stop))
        layout.addWidget(self.button_stop)

        self.setLayout(layout)

    def set_text(self, text):
        self.text_to_read = text

    def read(self):
        self.stop()
        self.worker.set_text(self.text_to_read)
        self.worker.start()
        self.running = True

    def stop(self):
        if self.running:
            if self.worker.isRunning():
                self.worker.engine.stop()
                self.worker.engine.endLoop()
        self.running = False

    def on_finished(self):
        self.running = False
        print("Finished reading")
        # Perform any additional actions after reading is finished

    def log(self, name, function):
        if self.debug:
            print("\n>>> " + ("=" * 60))
            print(f"@ Start of {name}:", "$Running:", self.running, "$Worker:", type(self.worker))
        function()
        if self.debug:
            print(f"@ End of {name}:", "$Running:", self.running, "$Worker:", type(self.worker))
            print("<<< " + ("=" * 60))


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Read()
    window.show()
    sys.exit(app.exec_())

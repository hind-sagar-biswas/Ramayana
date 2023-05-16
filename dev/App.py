from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from Verse import Verse
from Form import Form
from Ui import UI

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UI()
        self.title = 'Valmiki Ramayana'
        self.colors = self.ui.colors
        self.kandas = {
            'BALA': {
                'sarga_count': 77,
                'content': []
            },
            'AYODHYA': {
                'sarga_count': 119,
                'content': []
            },
            'ARANYA': {
                'sarga_count': 75,
                'content': []
            },
            'KISHKINDHA': {
                'sarga_count': 67,
                'content': []
            },
            'SUNDARA': {
                'sarga_count': 68,
                'content': []
            },
            'YUDDHA': {
                'sarga_count': 128,
                'content': []
            }
        }
        self.selected_kanda = None
        self.selected_sarga = None
        self.selected_sarga_number = None
        self.selected_verse = None
        self.selected_verse_number = None
        self.verse_widget = None

        self.setWindowTitle(self.title)
        self.setGeometry(self.ui.x, self.ui.y, self.ui.width, self.ui.height)
        self.set_window()
    
    def set_window(self):
        self.form = Form(self)
        self.central_widget = QWidget()

        self.central_layout = QVBoxLayout()
        self.central_layout.setAlignment(Qt.AlignTop)
        self.central_layout.addWidget(self.form)

        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        self.form.select_kanda()
        self.form.select_sarga()
        self.form.select_verse()
        return
    
    def update_window(self):
        self.set_verse()
        return

    def set_verse(self):
        if (self.verse_widget != None):
            self.central_layout.removeWidget(self.verse_widget)
        self.verse_widget = self.get_verse(self.selected_verse)
        self.central_layout.addWidget(self.verse_widget)

    def get_verse(self, verse):    
        verse_widget = self.verse_widget = Verse(verse)
        return verse_widget

    def fetch_kanda(self, kanda):
        self.selected_kanda = kanda
        self.kandas[kanda]['content'] = self.fetch_content(kanda)

    def fetch_sarga(self, sarga):
        sarga -= 1
        self.selected_sarga = self.kandas[self.selected_kanda]['content'][sarga]
        self.selected_sarga_number = sarga

    def fetch_verse(self):
        verse -= 1
        self.selected_verse = self.selected_sarga[verse]
        self.selected_verse_number = verse




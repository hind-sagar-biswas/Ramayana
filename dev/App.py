from PyQt5.QtWidgets import QMainWindow
from Verse import Verse

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Valmiki Ramayana'
        self.colors = {
            "dark": "#333333",
            "light": "white",
            "main": "#99506d",
            "sub": "#cf605f",
            "sub_light": "#fe994c"
        }
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

        self.setWindowTitle(self.title)
        self.setGeometry(50, 50, 800, 200)
        self.set_window()

    def get_verse(self, verse):    
        verse_widget = Verse(verse)
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




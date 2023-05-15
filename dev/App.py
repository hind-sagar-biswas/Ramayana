import os
import json
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QSplitter, QSpinBox


class App(QWidget):
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

        #select default kanda
        self.select_kanda()
        self.select_sarga()
        self.select_verse()
    
    def get_font(self, tag):
        font = QFont()
        if 'h' in tag:
            font.setBold(True) 
        match tag:
            case 'verse':
                font.setPointSize(13)
                font.setFamily('Kalam Regular')
            case 'p':
                font.setPointSize(13)
            case 'h1':
                font.setPointSize(17)
            case 'h2':
                font.setPointSize(15)
            case 'h3':
                font.setPointSize(14)
        return font

    def split(self, sections, sections_widgets, mode = "ltr"):
        splitter = QSplitter()
        splitter.setHandleWidth(1)
        
        for i in range(sections):
            if (mode == "ltr"): 
                layout = QHBoxLayout()
            else: 
                layout = QVBoxLayout()
            for widget in sections_widgets[i]:
                layout.addWidget(widget)
            
            splitter.addWidget(QWidget())
            splitter.setStretchFactor(i, 1)
            splitter.widget(i).setLayout(layout)
        
        return splitter

    def heading_widget(self):
        heading_widget = QWidget()
        heading_layout = QVBoxLayout(heading_widget) 
        heading_layout.addWidget(self.heading)
        return heading_widget
    
    def form_widget(self):
        sections = 3
        widgets = [
            [self.kanda_select_label, self.kanda_select],
            [self.sarga_select_label, self.sarga_select, self.sarga_select_button],
            [self.verse_select_label, self.verse_select, self.verse_select_button]
        ]
        form_widget = self.split(sections, widgets)
        form_widget.setStyleSheet(f'background: {self.colors["sub"]};' 'border-radius: 10px;')
        return form_widget
    
    def content_widget(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget) 
        content_layout.addWidget(self.verse_label)
        content_layout.addWidget(self.verse)
        content_layout.addWidget(self.pratipadam_label)
        content_layout.addWidget(self.pratipadam)
        content_layout.addWidget(self.tat_label)
        content_layout.addWidget(self.tat)
        return content_widget
    
    def spin_box_widget(self):
        spin_box = QSpinBox()
        spin_box.setMinimum(1)  # Set the minimum value
        spin_box.setMaximum(1)  # Set the maximum value
        spin_box.setSingleStep(1)  # Set the step value
        return spin_box

    def set_window(self):
        # main Layout
        vbox = QVBoxLayout()
        
        # Create labels and line edits
        ## KANDA
        self.kanda_select_label = QLabel('KANDA:', self)
        self.kanda_select = QComboBox(self)
        self.kanda_select.setStyleSheet(
                                            f'background-color: {self.colors["light"]};' 
                                            f'color: {self.colors["dark"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        for kanda in self.kandas:
            self.kanda_select.addItem(kanda)
        
        self.kanda_select.currentIndexChanged.connect(self.select_kanda)
        ## SARGA
        self.sarga_select = self.spin_box_widget()
        self.sarga_select.setStyleSheet(
                                            f'background-color: {self.colors["light"]};' 
                                            f'color: {self.colors["dark"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.sarga_select_label = QLabel('SARGA:', self)
        self.sarga_select_button = QPushButton('SELECT', self)
        self.sarga_select_button.setStyleSheet(
                                            f'background: {self.colors["sub_light"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.sarga_select_button.clicked.connect(self.select_sarga)
        ## VERSE
        self.verse_select = self.spin_box_widget()
        self.verse_select.setStyleSheet(
                                            f'background-color: {self.colors["light"]};' 
                                            f'color: {self.colors["dark"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.verse_select_label = QLabel('VERSE:', self)
        self.verse_select_button = QPushButton('SELECT', self)
        self.verse_select_button.setStyleSheet(
                                            f'background: {self.colors["sub_light"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.verse_select_button.clicked.connect(self.select_verse)

        # heading font
        self.heading = QLabel('Valmiki Ramayana', self)
        self.heading.setFont(self.get_font('h1'))

        self.verse_label = QLabel('Verse:', self)
        self.verse = QLabel('', self)
        self.pratipadam_label = QLabel('Pratipadam:', self)
        self.pratipadam = QLabel('', self)
        self.tat_label = QLabel('Meaning:', self)
        self.tat = QLabel('', self)

        self.verse_label.setFont(self.get_font('h3'))
        self.verse.setFont(self.get_font('verse'))
        self.pratipadam_label.setFont(self.get_font('h3'))
        self.pratipadam.setFont(self.get_font('p'))
        self.tat_label.setFont(self.get_font('h3'))
        self.tat.setFont(self.get_font('p'))

        
        heading = self.heading_widget()
        form = self.form_widget()
        content = self.content_widget()
        vbox.addWidget(heading)
        vbox.addWidget(form)
        vbox.addWidget(content)
        
        self.setLayout(vbox)

    def fetch_content(self, kanda):
        file_name = f'VALMIKI_RAMAYANA__{kanda}_KANDA'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, f'book\\{file_name}.json')

        with open(file_path, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
        return data

    def select_kanda(self):
        kanda = self.kanda_select.currentText()
        self.selected_kanda = kanda
        self.kandas[kanda]['content'] = self.fetch_content(kanda)
        self.sarga_select.setMaximum(self.kandas[kanda]["sarga_count"])
        self.sarga_select_label.setText(f'SARGA ({self.kandas[kanda]["sarga_count"]}): ')

    def select_sarga(self):
        sarga = int(self.sarga_select.text()) - 1
        self.selected_sarga = self.kandas[self.selected_kanda]['content'][sarga]
        self.selected_sarga_number = sarga
        self.verse_select.setMaximum(len(self.selected_sarga))
        self.verse_select_label.setText(f'VERSE ({len(self.selected_sarga)}): ')

    def select_verse(self):
        verse = int(self.verse_select.text()) - 1
        self.selected_verse = self.selected_sarga[verse]
        self.selected_verse_number = verse

        sloka = self.selected_verse["SanSloka"]
        pratipada = ';\n'.join(self.selected_verse["pratipada"].split(';'))
        tat = self.selected_verse["tat"]

        self.verse.setText(f'{sloka}')
        self.pratipadam.setText(f'{pratipada}')
        self.tat.setText(f'{tat}')



import os
import json
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QSplitter, QSpinBox


class Form(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app

        self.set_window()

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
    
    def form_widget(self):
        sections = 3
        widgets = [
            [self.kanda_select_label, self.kanda_select],
            [self.sarga_select_label, self.sarga_select, self.sarga_select_button],
            [self.verse_select_label, self.verse_select, self.verse_select_button]
        ]
        form_widget = self.split(sections, widgets)
        form_widget.setStyleSheet(f'background: {self.app.colors["sub"]};' 'border-radius: 10px;')
        return form_widget
    
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
                                            f'background-color: {self.app.colors["light"]};' 
                                            f'color: {self.app.colors["dark"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        for kanda in self.app.kandas:
            self.kanda_select.addItem(kanda)
        
        self.kanda_select.currentIndexChanged.connect(self.select_kanda)
        ## SARGA
        self.sarga_select = self.spin_box_widget()
        self.sarga_select.setStyleSheet(
                                            f'background-color: {self.app.colors["light"]};' 
                                            f'color: {self.app.colors["dark"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.sarga_select_label = QLabel('SARGA:', self)
        self.sarga_select_button = QPushButton('SELECT', self)
        self.sarga_select_button.setStyleSheet(
                                            f'background: {self.app.colors["sub_light"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.sarga_select_button.clicked.connect(self.select_sarga)
        ## VERSE
        self.verse_select = self.spin_box_widget()
        self.verse_select.setStyleSheet(
                                            f'background-color: {self.app.colors["light"]};' 
                                            f'color: {self.app.colors["dark"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.verse_select_label = QLabel('VERSE:', self)
        self.verse_select_button = QPushButton('SELECT', self)
        self.verse_select_button.setStyleSheet(
                                            f'background: {self.app.colors["sub_light"]};'
                                            'border: none;'
                                            'padding: 10px;'
                                            'border-radius: 5px;'
                                        )
        self.verse_select_button.clicked.connect(self.select_verse)

    
        form = self.form_widget()
        vbox.addWidget(form)
        
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
        self.app.selected_kanda = kanda
        self.app.kandas[kanda]['content'] = self.fetch_content(kanda)
        self.sarga_select.setMaximum(self.app.kandas[kanda]["sarga_count"])
        self.sarga_select_label.setText(f'SARGA ({self.app.kandas[kanda]["sarga_count"]}): ')

    def select_sarga(self):
        sarga = int(self.sarga_select.text()) - 1
        self.app.selected_sarga = self.app.kandas[self.app.selected_kanda]['content'][sarga]
        self.app.selected_sarga_number = sarga
        self.verse_select.setMaximum(len(self.app.selected_sarga))
        self.verse_select_label.setText(f'VERSE ({len(self.app.selected_sarga)}): ')

    def select_verse(self):
        verse = int(self.verse_select.text()) - 1
        self.app.selected_verse = self.app.selected_sarga[verse]
        self.app.selected_verse_number = verse

        self.app.update_window()
import os
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSizePolicy


class Form(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ui = self.app.ui
        self.set_window()
    
    def form_widget(self):
        sections = 3
        widgets = [
            [self.kanda_select_label, self.kanda_select],
            [self.sarga_select_label, self.sarga_select],
            [self.verse_select_label, self.verse_select]
        ]
        form_widget = self.ui.split(sections, widgets)
        form_widget.setStyleSheet(f'background: {self.app.colors["sub"]};' 'border-radius: 10px;')
        return form_widget

    def set_window(self):
        # main Layout
        vbox = QVBoxLayout()
        
        # Create labels and line edits
        ## KANDA
        self.kanda_select_label = QLabel('KANDA:', self)
        self.kanda_select = QComboBox(self)
        self.kanda_select.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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
        self.sarga_select = self.ui.spin_box_widget()
        self.sarga_select.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.sarga_select.valueChanged.connect(self.select_sarga)
        self.sarga_select.setStyleSheet(
            f'background-color: {self.app.colors["light"]};' 
            f'color: {self.app.colors["dark"]};'
            'border: none;'
            'padding: 10px;'
            'border-radius: 5px;'
        )
        self.sarga_select_label = QLabel('SARGA:', self)
        ## VERSE
        self.verse_select = self.ui.spin_box_widget()
        self.verse_select.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.verse_select.valueChanged.connect(self.select_verse)
        self.verse_select.setStyleSheet(
            f'background-color: {self.app.colors["light"]};' 
            f'color: {self.app.colors["dark"]};'
            'border: none;'
            'padding: 10px;'
            'border-radius: 5px;'
        )
        self.verse_select_label = QLabel('VERSE:', self)

    
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            if (int(self.verse_select.text()) == len(self.app.selected_sarga)):
                self.sarga_select.setValue(int(self.sarga_select.text()) + 1)
                self.select_sarga()
                self.verse_select.setValue(1)
            else:
                self.verse_select.setValue(int(self.verse_select.text()) + 1)
            self.select_verse()
        elif event.key() == Qt.Key_Left:
            if (int(self.verse_select.text()) == 1):
                self.sarga_select.setValue(int(self.sarga_select.text()) - 1)
                self.select_sarga()
                self.verse_select.setValue(len(self.app.selected_sarga))
            else:
                self.verse_select.setValue(int(self.verse_select.text()) - 1)
            self.select_verse()

        super().keyPressEvent(event)
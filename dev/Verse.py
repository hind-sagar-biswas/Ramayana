import os
import json
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QSplitter, QSpinBox


class Verse(QWidget):
    def __init__(self, verse):
        super().__init__()

        self.selected_verse = verse
        self.set_widget()
        self.set_content()
    
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

    def set_widget(self):
        # main Layout
        vbox = QVBoxLayout()

        self.verse_label = QLabel('Verse:', self)
        self.verse = QLabel('', self)
        self.verse_label.setFont(self.get_font('h3'))
        self.verse.setFont(self.get_font('verse'))

        self.pratipadam_label = QLabel('Pratipadam:', self)
        self.pratipadam = QLabel('', self)
        self.pratipadam_label.setFont(self.get_font('h3'))
        self.pratipadam.setFont(self.get_font('p'))

        self.tat_label = QLabel('Meaning:', self)
        self.tat = QLabel('', self)
        self.tat_label.setFont(self.get_font('h3'))
        self.tat.setFont(self.get_font('p'))

        vbox.addWidget(self.verse_label)
        vbox.addWidget(self.verse)
        vbox.addWidget(self.pratipadam_label)
        vbox.addWidget(self.pratipadam)
        vbox.addWidget(self.tat_label)
        vbox.addWidget(self.tat)
        
        self.setLayout(vbox)

    def set_content(self):
        sloka = self.selected_verse["SanSloka"]
        pratipada = ';\n'.join(self.selected_verse["pratipada"].split(';'))
        tat = self.selected_verse["tat"]

        self.verse.setText(f'{sloka}')
        self.pratipadam.setText(f'{pratipada}')
        self.tat.setText(f'{tat}')


from Ui import UI
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy


class Verse(QWidget):
    def __init__(self, verse):
        super().__init__()

        self.ui = UI()
        self.selected_verse = verse
        self.set_widget()
        self.set_content()

    def set_widget(self):
        # main Layout
        vbox = QVBoxLayout()

        self.verse_label = QLabel('Verse:', self)
        self.verse_label.setStyleSheet(f"color: {self.ui.colors['heading']};")
        self.verse = QLabel('', self)
        self.verse_label.setFont(self.ui.get_font('h3'))
        self.verse.setFont(self.ui.get_font('verse'))

        self.pratipadam_label = QLabel('Pratipadam:', self)
        self.pratipadam_label.setStyleSheet(f"color: {self.ui.colors['heading']};")
        self.pratipadam = QLabel('', self)
        self.pratipadam_label.setFont(self.ui.get_font('h3'))
        self.pratipadam.setFont(self.ui.get_font('p'))

        self.tat_label = QLabel('Meaning:', self)
        self.tat_label.setStyleSheet(f"color: {self.ui.colors['heading']};")
        self.tat = QLabel('', self)
        self.tat.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tat_label.setFont(self.ui.get_font('h3'))
        self.tat.setFont(self.ui.get_font('p'))

        sections = 2
        widgets = [
            [self.verse_label, self.verse, self.tat_label, self.tat],
            [self.pratipadam_label, self.pratipadam]
        ]
        section_styles = [
            f"background-color: {self.ui.colors['sub']}; border-radius: 10px;",
            ""
        ]
        ratios = [3, 2]
        content_widget = self.ui.split(sections, widgets, mode="ttb", section_styles=section_styles, ratio=ratios)

        vbox.addWidget(content_widget)
        
        self.setLayout(vbox)

    def set_content(self):
        sloka = self.selected_verse["SanSloka"]
        pratipada_list = list(map(lambda x: x.strip(), self.selected_verse["pratipada"].split(';')))
        pratipada = ';\n'.join(pratipada_list)
        tat = self.selected_verse["tat"]

        self.verse.setText(f'{sloka}')
        self.pratipadam.setText(f'{pratipada}')
        self.tat.setText(f'{tat}')
        
        self.pratipadam.setWordWrap(True)
        self.tat.setWordWrap(True)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QSpinBox

class UI(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app

        self.themes = {
            "dark": {
                "dark": "#333333",
                "light": "white",
                "main": "#111111",
                "sub": "#333333",
                "sub_light": "#fe994c",
                "heading": "#ccaa35"
            },
            "peach": {
                "dark": "#333333",
                "light": "white",
                "main": "#99506d",
                "sub": "#cf605f",
                "sub_light": "#fe994c",
                "heading": "white"  
            }
        }

        self.colors = self.themes["dark"]
        self.x = 100
        self.y = 100
        self.width = 1100
        self.height = 200

        # self.set_styles()

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
    
    def split(self, sections, sections_widgets, mode = "ltr", section_styles = None, ratio = None):
        splitter = QSplitter()
        splitter.setHandleWidth(1)

        for i in range(sections):
            layout = QHBoxLayout() if (mode == "ltr") else QVBoxLayout()
            for widget in sections_widgets[i]:
                layout.addWidget(widget)

            r = 1 if ratio is None else ratio[i]
            splitter.addWidget(QWidget())
            splitter.setStretchFactor(i, r)
            splitter.widget(i).setLayout(layout)
            if section_styles != None:
                splitter.widget(i).setStyleSheet(f"QWidget {{ {section_styles[i]} }}")

        return splitter
    
    def spin_box_widget(self):
        spin_box = QSpinBox()
        spin_box.setMinimum(1)  # Set the minimum value
        spin_box.setMaximum(1)  # Set the maximum value
        spin_box.setSingleStep(1)  # Set the step value
        spin_box.setStyleSheet(
            f'background-color: {self.colors["light"]};' 
            f'color: {self.colors["dark"]};'
            'border: none;'
            'padding: 10px;'
            'border-radius: 5px;'
        )
        return spin_box
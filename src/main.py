import sys
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication
import App 

if __name__ == '__main__':
    # init
    app = QApplication(sys.argv)

    # fonts
    kalam_font_id = QFontDatabase.addApplicationFont("fonts/Kalam-Regular.ttf")
    font_family = QFontDatabase.applicationFontFamilies(kalam_font_id)[0]

    # window
    window = App.App()
    window.setStyleSheet(f'background-color: {window.colors["main"]};' f'color: {window.colors["light"]};' "font-family: sans-serif")
    window.show()
    sys.exit(app.exec_())
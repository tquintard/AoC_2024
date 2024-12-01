import sys
from PyQt6.QtWidgets import QApplication
from userform import UserForm

if __name__ == '__main__':
    app = QApplication([])
    form = UserForm()
    app.exec()
    sys.exit()

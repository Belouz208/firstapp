import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLineEdit, QLabel
from PyQt5 import uic
import proced


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        self.champ_1.textChanged.connect(lambda: proced.verifier_contenu(self.champ_1, self.label_1))
        self.champ_2.textChanged.connect(lambda: proced.verifier_contenu(self.champ_2, self.label_2))
        self.champ_3.textChanged.connect(lambda: proced.verifier_contenu(self.champ_3, self.label_3))
        self.champ_4.textChanged.connect(lambda: proced.verifier_contenu(self.champ_4, self.label_4))

        # self.champ_1.textChanged.connect(lambda: proced.champ_2_change(self.champ_1, self.champ_2))
        self.button_calc.clicked.connect(lambda :proced.calc_tri(self.champ_1, self.champ_2,self.champ_3,self.champ_4,self.label_10))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

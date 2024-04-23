import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.images = ['1.jpg', '2.jpg', '3.jpg']
        self.sumacakalorie = 0
        self.show()
        self.setWindowTitle("Kalkulator kalorii")
        self.ui.add.clicked.connect(self.calCalories)
        self.ui.add.clicked.connect(self.addToList)

    def addToList(self):
        text = self.ui.dishe.text()
        calories = int(self.ui.calories.text())
        self.ui.dishe.setText("")
        self.ui.calories.setText("")
        print(self.sumacakalorie)
        finall = "Danie: " + text + " " + str(calories) + " kalorii"
        self.ui.List.addItem(finall)

    def calCalories(self):
        global pixmap
        calories = int(self.ui.calories.text())
        self.sumacakalorie += calories
        if self.ui.male.isChecked():
            if self.ui.small.isChecked():
                kcal = (self.sumacakalorie / 1900.00) * 100
                if kcal <= 80.0:
                    self.ui.sumcalories.setStyleSheet("background-color: rgb(0, 255, 0); color: rgb(0, 255, 255);")
                    pixmap = QPixmap(self.images[0])
                if 80.0 < kcal <= 100.0:
                    self.ui.sumcalories.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[1])
                if kcal > 100.0:
                    self.ui.sumcalories.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[2])
            if self.ui.medium.isChecked():
                kcal = (self.sumacakalorie / 2200.00) * 100
                if kcal <= 80.0:
                    self.ui.sumcalories.setStyleSheet(
                        "background-color: rgb(0, 255, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[0])
                if 80.0 < kcal <= 100.0:
                    self.ui.sumcalories.setStyleSheet(
                        "background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[1])
                if kcal > 100.0:
                    self.ui.sumcalories.setStyleSheet(
                        "background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[2])
            if self.ui.big.isChecked():
                kcal = (self.sumacakalorie / 2500.00) * 100
                if kcal <= 80.0:
                    self.ui.sumcalories.setStyleSheet(
                        "background-color: rgb(0, 255, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[0])
                if 80.0 < kcal <= 100.0:
                    self.ui.sumcalories.setStyleSheet(
                        "background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[1])
                if kcal > 100.0:
                    self.ui.sumcalories.setStyleSheet(
                        "background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);")
                    pixmap = QPixmap(self.images[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.exec()
    sys.exit(app.exec())

import sys

from PyQt5.QtCore import QItemSelection, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSpinBox, QLineEdit, QPushButton, QWidget, \
    QComboBox, QGridLayout, QLabel, QGraphicsRectItem, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Определение себестоимости продукции растениеводства")
        layout = QGridLayout()

        layout.addWidget(QLabel("Тип культуры:"), 0, 0)
        self.cb = QComboBox()
        self.cb.addItems(["ячмень", "озимая пшеница", "подсолнечник"])
        layout.addWidget(self.cb, 0, 1)
        layout.addWidget(QLabel("Производственная себестоимость 1 ц, тыс. руб.:"), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)
        layout.addWidget(QLabel("Объем реализации, ц:"), 2, 0)
        layout.addWidget(QLineEdit(), 2, 1)
        layout.addWidget(QLabel("Аренда торговой точки, тыс. руб.:"), 3, 0)
        layout.addWidget(QLineEdit(), 3, 1)
        layout.addWidget(QLabel("Заработная плата продавцам, тыс. руб.:"), 4, 0)
        self.zp = QLineEdit("0")
        layout.addWidget(self.zp, 4,1)
        self.btn1 = QPushButton("Страховые взносы, тыс. руб.")
        layout.addWidget(self.btn1, 5, 0)
        self.stvnz = QLineEdit()
        layout.addWidget(self.stvnz, 5, 1)
        layout.addWidget(QLabel("Маркетинговые расходы, тыс. руб.:"), 6, 0)
        layout.addWidget(QLineEdit(), 6, 1)
        self.btn2 = QPushButton("Уровень наценки, %")
        layout.addWidget(self.btn2, 7, 0)
        layout.addWidget(QLineEdit(), 7, 1)
        self.btn3 = QPushButton("Цена реализации")
        layout.addWidget(self.btn3, 8, 0)
        layout.addWidget(QLineEdit(), 8, 1)
        self.btn4 = QPushButton("Сравнение цен")
        layout.addWidget(self.btn4, 9, 0)
        self.graph = QWidget()
        self.graph.resize(800, 600)
        layout.addWidget(self.graph, 10, 0, 1, 2)

        #(self.zp is float)
        if self.btn1:
            self.btn1.clicked.connect(self.strahvznos)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def strahvznos(self):
        stra = float(self.zp.text()) * 0.3
        self.stvnz.setText(str(stra))




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

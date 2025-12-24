import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, \
    QComboBox, QGridLayout, QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent='None', width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Определение себестоимости продукции растениеводства")
        layout = QGridLayout()
        self.setFixedHeight(800)

        layout.addWidget(QLabel("Тип культуры:"), 0, 0)
        self.cb = QComboBox()
        self.cb.addItems(["ячмень", "озимая пшеница", "подсолнечник"])
        layout.addWidget(self.cb, 0, 1)
        layout.addWidget(QLabel("Производственная себестоимость 1 ц, тыс. руб.:"), 1, 0)
        self.prseb = QLineEdit("0")
        layout.addWidget(self.prseb, 1, 1)
        layout.addWidget(QLabel("Объем реализации, ц:"), 2, 0)
        self.objem = QLineEdit("0")
        layout.addWidget(self.objem, 2, 1)
        layout.addWidget(QLabel("Аренда торговой точки, тыс. руб.:"), 3, 0)
        self.arenda = QLineEdit("0")
        layout.addWidget(self.arenda, 3, 1)
        layout.addWidget(QLabel("Заработная плата продавцам, тыс. руб.:"), 4, 0)
        self.zp = QLineEdit("0")
        layout.addWidget(self.zp, 4,1)
        self.btn1 = QPushButton("Страховые взносы, тыс. руб.")
        layout.addWidget(self.btn1, 5, 0)
        self.stvnz = QLineEdit()
        layout.addWidget(self.stvnz, 5, 1)
        layout.addWidget(QLabel("Маркетинговые расходы, тыс. руб.:"), 6, 0)
        self.mark = QLineEdit("0")
        layout.addWidget(self.mark, 6, 1)
        self.btn2 = QPushButton("Уровень наценки, %")
        layout.addWidget(self.btn2, 7, 0)
        self.uroven = QLineEdit()
        layout.addWidget(self.uroven, 7, 1)
        self.btn3 = QPushButton("Цена реализации")
        layout.addWidget(self.btn3, 8, 0)
        self.tsenlabel = QLineEdit("0")
        layout.addWidget(self.tsenlabel, 8, 1)
        self.btn4 = QPushButton("Сравнение цен")
        layout.addWidget(self.btn4, 9, 0)
        self.graph = QWidget()
        self.graph.resize(800, 600)
        layout.addWidget(self.graph, 10, 0, 1, 2)

        if self.btn1:
            self.btn1.clicked.connect(self.strahvznos)
        if self.btn2:
            self.btn2.clicked.connect(self.urnats)
        if self.btn3:
            self.btn3.clicked.connect(self.tsenareal)
        if self.btn4:
            self.btn4.clicked.connect(self.graphic)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def strahvznos(self):
        try:
            stra = float(self.zp.text()) * 0.3
            self.stvnz.setText(str(stra))
        except ValueError:
            self.stvnz.setText("ошибка")

    #Зачем эта функция? Транспортные расходы в задаче не используются
    def transport(self):
        try:
            tran = float(self.objem.text()) * 0.1
        except ValueError:
            print("ошибка")

    def urnats(self):
        try:
            if self.cb.currentIndex() == 0:
                ur = 50
            if self.cb.currentIndex() == 1:
                ur = 35
            if self.cb.currentIndex() == 2:
                ur = 45
            self.uroven.setText(str(ur))
        except ValueError:
            print("ошибка")

    def tsenareal(self):
        try:
            tsena = (float(self.prseb.text()) +
                     (float(self.arenda.text()) + float(self.zp.text())+ float(self.stvnz.text()) + float(self.mark.text()))
                     * (1 + float(self.uroven.text())/100))
            self.tsenlabel.setText(str(tsena))
        except ValueError:
            self.tsenlabel.setText("ошибка")

    def graphic(self):
        try:
            if self.graph.layout():
                while self.graph.layout().count():
                    item = self.graph.layout().takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            else:
                layout = QVBoxLayout(self.graph)
                self.graph.setLayout(layout)

            sc = MplCanvas(self)
            x = ['Фактическая цена', 'Плановая цена']
            y = [float(self.tsenlabel.text()), 100] #я не понял, как плановую расчитать
            sc.axes.bar(x, y, width=0.8, color=['blue', 'red'])
            sc.draw()
            self.graph.layout().addWidget(sc)
        except Exception:
            print("Провал")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

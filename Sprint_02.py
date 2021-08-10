import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import sys, math
import numpy as np

def parabolas(f, a, b, n):
    if n%2 == 1:
        n += 1
    dx = 1.0 * (b - a) / n
    sum = (f(a) + 4 * f(a + dx) + f(b))
    for i in range(1, int(n / 2)):
        sum += 2 * f(a + (2 * i) * dx) + 4 * f(a + (2 * i + 1) * dx)

    return sum * dx / 3

def trapezii(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h

def middle_rectangle(f, a, b, n):
    result = 0.0
    h = (b - a) / n
    for i in range(n):
        result += f(a + h * (i + 0.5))
    result *= h
    return result

def right_rectangle(f, a, b, n):
    h = (b - a) / n
    result = f((a+h) + h * 0)
    for i in range(n):
        result += f((a+h) + h * i)
    result *= h
    return result

def left_rectangle(f, a, b, n):
    result = 0.0
    h = (b - a) / n
    for i in range(n):
        result += f(a + h * i)
    result *= h
    return result

def euler(f, a, b, y, N):
    step = (b - a) / N
    mass = np.array(range(N+1), float)
    mass.fill(0)
    mass[0] = y
    for i in range(N):
        k1 = step * f(a,mass[i])
        mass[i+1] = mass[i] + k1
        a = a + step
    return mass

def runge_kuta_scnd(f, a, b, y, N):
    step = (b - a) / N
    mass = np.array(range(N+1), float)
    mass.fill(0.0)
    mass[0] = y
    for i in range(N):
        k1 = step * f(a,mass[i])
        k2 = step * f(a + step/2, mass[i] + k1/2)
        mass[i+1] = mass[i] + k2
        a+=step
    return mass

def runge_kuta_thrd(f, a, b, y, N):
    step = (b - a) / N
    mass = np.array(range(N+1), float)
    mass.fill(0)
    mass[0] = y
    for i in range(N):
        k1 = step * f(a, mass[i])
        k2 = step * f(a + step/2, mass[i] + k1/2)
        k3 = step * f(a + step, mass[i] + 2*k2 - k1)
        mass[i+1] = mass[i] + (k1 + 4*k2 + k3)/6
        a+=step
    return mass

def runge_kuta_frth(f, a, b, y, N):
    step = (b - a) / N
    mass = np.array(range(N+1), float)
    mass.fill(0)
    mass[0] = y
    for i in range(N):
        k1 = step * f(a, mass[i])
        k2 = step * f(a + step/2, mass[i] + k1/2)
        k3 = step * f(a + step/2, mass[i] + k2/2)
        k4 = step * f(a + step, mass[i] + k3)
        mass[i+1] = mass[i] + (k1 + 2*k2 + 2*k3 + k4)/6
        a= a + step
    return mass

method = "Левых прямоугольников"
method_diff = "Эйлера"
function = "f(x)=cosf0(x)"

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 500
        self.top = 200
        self.width = 750
        self.height = 500
    
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QFormLayout(self)
        self.all_tabs = QTabWidget()
        self.fst_tab = QWidget()
        self.scnd_tab = QWidget()
        self.thrd_tab = QWidget()
        self.all_tabs.resize(750, 500)

        self.all_tabs.addTab(self.fst_tab, "Интегралы")
        self.all_tabs.addTab(self.scnd_tab, "Дифузы")
        self.all_tabs.addTab(self.thrd_tab, "График")
        self.fst_tab.layout = QGridLayout(self)
        self.scnd_tab.layout = QGridLayout(self)
        self.thrd_tab.layout = QGridLayout(self)
        self.text_label = QLabel()
        self.text_label.setText("Метод интегрирования")
        self.text_label_fst = QLabel()
        self.text_label_fst.setText("Метод решения")
        self.methods = QComboBox(self)
        self.methods.addItems(["Левых прямоугольников", "Центральных прямоугольников", "Правых прямоугольников", "Трапеций", "Симпсона"])
        self.methods.activated.connect(self.handle)
        self.fst_tab.layout.addWidget(self.text_label, 0, 0)
        self.fst_tab.layout.addWidget(self.methods, 0, 1)

        self.text_label_down = QLabel('Нижняя граница:', self)
        self.text_label_up = QLabel('Верхняя граница:', self)

        self.methods_diff = QComboBox(self)
        self.text_label_h = QLabel('Количество шагов:', self)
        self.text_label_start_diff = QLabel('Начало отрезка:', self)
        self.methods_diff.addItems(["Эйлера", "Рунге-Кутта второго порядка", "Рунге-Кутта третьего порядка", "Рунге-Кутта четвертого порядка"])
        self.equations = QComboBox(self)
        self.equations.addItems(["f(x)=cosf0(x)", "f(x)=expf0(-x/2)", "f(x)=sinf0(-x)", "f(x)=f0((-x/3)^3+5x-6", "f(x)=expf0(-5x^3+6x^2-3)"])
        self.methods_diff.activated.connect(self.handle_diff)
        self.text_label_end_diff = QLabel('Конец отрезка:', self)
        self.text_label_step_diff = QLabel('Количество шагов:', self)
        self.equations.activated.connect(self.handle_funcs)
        self.answer_butt = QPushButton('Решение', self)
        self.answer_butt.clicked.connect(self.on_click)
        self.equations_diff = QComboBox(self)
        self.equations_diff.addItems(["y'=x+2y", "y'=sin(x)+sin(y)", "y'=exp(-6x)+y", "y'=cos(x*y)"])
        self.text_label_y_diff = QLabel('Начальное значение y:', self)
        self.equations_diff.activated.connect(self.handle_funcs_diff)

        self.fst_tab.layout.addWidget(self.equations, 1, 0, 1, 2)
        self.answer_butt_table = QPushButton('Таблица', self)
        self.fst_tab.layout.addWidget(self.text_label_down)
        self.down = QLineEdit("", self)
        self.fst_tab.layout.addWidget(self.down)
        self.answer_butt_table.clicked.connect(self.on_click_table)
        self.answer_butt_graphic = QPushButton('График', self)
        self.answer_butt_graphic.clicked.connect(self.on_click_graphic)
        self.scnd_tab.layout.addWidget(self.text_label_fst, 0, 0)
        self.scnd_tab.layout.addWidget(self.methods_diff, 0, 1)
        self.view = view = pg.PlotWidget()
        self.curve = view.plot(name="Line")

        self.fst_tab.layout.addWidget(self.text_label_up)
        self.up = QLineEdit("", self)
        self.start_diff = QLineEdit("", self)
        self.scnd_tab.layout.addWidget(self.equations_diff, 1, 0, 1, 2)
        self.scnd_tab.layout.addWidget(self.text_label_start_diff)
        self.fst_tab.layout.addWidget(self.up)
        self.fst_tab.layout.addWidget(self.text_label_h)
        self.step = QLineEdit("", self)
        self.scnd_tab.layout.addWidget(self.start_diff)
        self.scnd_tab.layout.addWidget(self.text_label_end_diff)
        self.fst_tab.layout.addWidget(self.step)
        self.fst_tab.layout.addWidget(self.answer_butt, 5, 0, 1, 2)
        self.fst_tab.setLayout(self.fst_tab.layout)

        self.end_diff = QLineEdit("", self)
        self.scnd_tab.layout.addWidget(self.end_diff)
        self.scnd_tab.layout.addWidget(self.text_label_y_diff)
        self.y_diff = QLineEdit("", self)
        self.scnd_tab.layout.addWidget(self.y_diff)
        self.scnd_tab.layout.addWidget(self.text_label_step_diff)
        self.step_diff = QLineEdit("", self)
        self.scnd_tab.layout.addWidget(self.step_diff)
        self.scnd_tab.layout.addWidget(self.answer_butt_table, 6, 0)
        self.scnd_tab.layout.addWidget(self.answer_butt_graphic, 6, 1)
        self.scnd_tab.setLayout(self.scnd_tab.layout)

        self.layout.addWidget(self.all_tabs)
        self.setLayout(self.layout)

    def handle(self, index):
        global method
        method = self.methods.itemText(index)

    def handle_funcs(self, index):
        global function
        function = self.equations.itemText(index)

        if function == "f(x)=cosf0(x)":
            function = lambda x: math.cos(x)

        if function == "f(x)=expf0(-x/2)":
            function = lambda x: math.exp(-x/2)

        if function == "f(x)=sinf0(-x)":
            function = lambda x: math.sin(-x)

        if function == "f(x)=f0((-x/3)^3+5x-6":
            function = lambda x: (-x/3)^3 + 5*x - 6

        if function == "f(x)=expf0(-5x^3+6x^2-3)":
            function = lambda x: math.exp(-5*x^3+6*x^2-3)

    def handle_diff(self, index):
        global method_diff
        method_diff = self.methods_diff.itemText(index)

    def handle_funcs_diff(self, index):
        global function
        function = self.equations_diff.itemText(index)

        if function == "y'=x+2y":
            function = lambda x, y: x+2*y

        if function == "y'=sin(x)+sin(y)":
            function = lambda x, y: math.sin(x) + math.sin(y)

        if function == "y'=exp(-6x)+y":
            function = lambda x, y: math.exp(-6*x)+y

        if function == "y'=cos(x*y)":
            function = lambda x, y: math.cos(x*y)


    @pyqtSlot()
    def on_click(self):        
        global function
        if function == "f(x)=cosf0(x)":
            function = lambda x: math.cos(x)

        if function == "f(x)=expf0(-x/2)":
            function = lambda x: math.exp(-x/2)

        if function == "f(x)=sinf0(-x)":
            function = lambda x: math.sin(-x)

        if function == "f(x)=f0((-x/3)^3+5x-6":
            function = lambda x: (-x/3)^3 + 5*x - 6

        if function == "f(x)=expf0(-5x^3+6x^2-3)":
            function = lambda x: math.exp(-5*x^3+6*x^2-3)

        if method == "Левых прямоугольников":
            massive = left_rectangle(function, float(self.down.text()), float(self.up.text()), int(self.step.text()))

        if method == "Центральных прямоугольников":
            massive = middle_rectangle(function, float(self.down.text()), float(self.up.text()), int(self.step.text()))

        if method == "Правых прямоугольников":
            massive = right_rectangle(function, float(self.down.text()), float(self.up.text()), int(self.step.text()))

        if method == "Трапеций":
            massive = trapezii(function, float(self.down.text()), float(self.up.text()), int(self.step.text()))

        if method == "Симпсона":
            massive = parabolas(function, float(self.down.text()), float(self.up.text()), int(self.step.text()))
        
        self.answer = QLabel('', self)
        self.fst_tab.layout.addWidget(self.answer, 7, 0, 1, 2)
        self.answer.setText("Ответ: " + str(massive))
        
        massive = [left_rectangle(function, float(self.down.text()), float(self.up.text()), int(self.step.text())),
        middle_rectangle(function, float(self.down.text()), float(self.up.text()), int(self.step.text())),
        right_rectangle(function, float(self.down.text()), float(self.up.text()), int(self.step.text())),
        trapezii(function, float(self.down.text()), float(self.up.text()), int(self.step.text())),
        parabolas(function, float(self.down.text()), float(self.up.text()), int(self.step.text()))]

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)

        temp = ["Левых прямоугольников", "Центральных прямоугольников", "Правых прямоугольников", "Трапеций", "Симпсона"]

        for i in range(5):
            self.tableWidget.setItem(i,0, QTableWidgetItem(temp[i]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(massive[i])))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        
        self.fst_tab.layout.addWidget(self.tableWidget, 8, 0, 1, 2)
        self.fst_tab.setLayout(self.fst_tab.layout)

    def on_click_graphic(self):        

        global function
        if function == "y'=x+2y":
            function = lambda x, y: x+2*y

        if function == "y'=sin(x)+sin(y)":
            function = lambda x, y: math.sin(x) + math.sin(y)

        if function == "y'=exp(-6x)+y":
            function = lambda x, y: math.exp(-6*x)+y

        if function == "y'=cos(x*y)":
            function = lambda x, y: math.cos(x*y)

        if method_diff == "Эйлера":
            massive = euler(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))

        if method_diff == "Рунге-Кутта второго порядка":
            massive = runge_kuta_scnd(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))

        if method_diff ==  "Рунге-Кутта третьего порядка":
            massive = runge_kuta_thrd(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))

        if method_diff == "Рунге-Кутта четвертого порядка":
            massive = runge_kuta_frth(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))


        self.curve.setData(massive)
        self.thrd_tab.layout.addWidget(self.view, 8, 0, 1, 2)
        self.thrd_tab.setLayout(self.thrd_tab.layout)
        self.all_tabs.setCurrentIndex(2)

    def on_click_table(self):

        global function
        if function == "y'=x+2y":
            function = lambda x, y: x+2*y

        if function == "y'=sin(x)+sin(y)":
            function = lambda x, y: math.sin(x) + math.sin(y)

        if function == "y'=exp(-6x)+y":
            function = lambda x, y: math.exp(-6*x)+y

        if function == "y'=cos(x*y)":
            function = lambda x, y: math.cos(x*y)

        if method_diff == "Эйлера":
            massive = euler(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))

        if method_diff == "Рунге-Кутта второго порядка":
            massive = runge_kuta_scnd(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))

        if method_diff ==  "Рунге-Кутта третьего порядка":
            massive = runge_kuta_thrd(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))

        if method_diff == "Рунге-Кутта четвертого порядка":
            massive = runge_kuta_frth(function, float(self.start_diff.text()), float(self.end_diff.text()), float(self.y_diff.text()), int(self.step_diff.text()))
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(massive))
        self.tableWidget.setColumnCount(1)

        temp = []
        for i in range(len(massive)):
            temp.append(str(i))
        self.tableWidget.setVerticalHeaderLabels(temp)

        for i in range(len(massive)):
            self.tableWidget.setItem(0,i, QTableWidgetItem(str(massive[i])))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.scnd_tab.layout.addWidget(self.tableWidget, 8, 0, 10, 2)
        
        self.scnd_tab.setLayout(self.scnd_tab.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
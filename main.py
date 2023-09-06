from PyQt5 import QtCore, QtGui, QtWidgets
from matrix import Ui_MainWindow
from er import Ui_Dialog
from hp import Ui_Form
import numpy as np
import random
import sys

class ErrorWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ErrorWindow, self).__init__()
        self.ew = Ui_Dialog()
        self.ew.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img/err_inc.ico'))

class HelpWindow(QtWidgets.QWidget):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.hw = Ui_Form()
        self.hw.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img/MIREA.ico'))
        self.styleB()
        self.rus()

    def eng(self):
        self.hw.label.setText('Instructions for using the calculator:\n\nIf you need operations on matrices:\n1) Fill in the matrices;\n2) Select the required operation\n3) If you need to swap the matrices, click on "<- ->". \n\nIf you need an operation on one matrix: \n1) Select a matrix; \n2) Fill in the matrix \n3) If you need a unit matrix, then select the number 1 and click on the "Fill matrix" button; \n4) Select the required operation.')
        self.setWindowTitle('Help')

    def rus(self):
        self.hw.label.setText('Инструкция по использованию калькулятора:\n\nЕсли нужны операции над матрицами:\n1) Заполнить матрицы;\n2) Выбрать необходимую операцию\n3) Если необходимо поменять матрицы местами, нажмите на "<- ->".\n\nЕсли нужна операция над одной матрицей:\n1) Выбрать матрицу;\n2) Заполнить матрицу \n3) Если нужна единичная матрица то выбрать цифру 1 и нажать на кнопку "Заполнить матрицу";\n4) Выбрать необходимую операцию.')
        self.setWindowTitle('Помощь')

    def styleB(self):
        self.setStyleSheet(open('styles/style_win_b.css').read())
        self.update()

    def styleW(self):
        self.setStyleSheet(open('styles/style_win_w.css').read())
        self.update()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img/MIREA.ico'))
        self.ui.butchn.clicked.connect(self.change)
        self.ui.butplus.clicked.connect(self.plus)
        self.ui.butmin.clicked.connect(self.min)
        self.ui.butmul.clicked.connect(self.mul)
        self.ui.butdiv.clicked.connect(self.div)
        self.ui.butcopy.clicked.connect(self.copy_m)
        self.ui.butpaste.clicked.connect(self.paste)
        self.ui.butclear.clicked.connect(self.clear)
        self.ui.butTran.clicked.connect(self.tran)
        self.ui.butInv.clicked.connect(self.inv)
        self.ui.butRank.clicked.connect(self.rank)
        self.ui.butMult.clicked.connect(self.mult)
        self.ui.butDet.clicked.connect(self.det)
        self.ui.butPow.clicked.connect(self.pow)
        self.ui.butMat.clicked.connect(self.mat)
        self.ui.butRows.clicked.connect(self.rows)
        self.ui.butCol.clicked.connect(self.col)
        self.ui.spinBox_A_rows.valueChanged.connect(self.rows_a)
        self.ui.spinBox_A_col.valueChanged.connect(self.cols_a)
        self.ui.spinBox_B_rows.valueChanged.connect(self.rows_b)
        self.ui.spinBox_B_col.valueChanged.connect(self.cols_b)
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionRussian.triggered.connect(self.langR)
        self.ui.actionEnglish.triggered.connect(self.langE)
        self.ui.actionBlack.triggered.connect(self.themeB)
        self.ui.actionWhite.triggered.connect(self.themeW)

    def langR(self):
        lr = HelpWindow()
        lr.rus()
        list_rus = [
    self.tr('Матрица А'),
    self.tr('Матрица В'),
    self.tr('Результат'),
    self.tr('Выбрать матрицу:'),
    self.tr('Копировать'),
    self.tr('Вставить'),
    self.tr('Очистить'),
    self.tr('Ранг'),
    self.tr('Транспонировать'),
    self.tr('Обратная матрица'),
    self.tr('Умножить на число'),
    self.tr('Определитель'),
    self.tr('Возвести в степень'),
    self.tr('Заполнить матрицу'),
    self.tr('Заполнить строку'),
    self.tr('Заполнить столбец'),
    self.tr('Все матрицы'),
    self.tr('Все поля'),
    self.tr('0'),
    self.tr('1'),
    self.tr('2'),
    self.tr('3'),
    self.tr('4'),
    self.tr('5'),
    self.tr('6'),
    self.tr('7'),
    self.tr('8'),
    self.tr('9'),
    self.tr('Рандом'),
    self.tr('Настройки'),
    self.tr('Помощь'),
    self.tr('Смена языка'),
    self.tr('Русский'),
    self.tr('Английский'),
    self.tr('Смена темы'),
    self.tr('Тёмная'),
    self.tr('Светлая')
    ]
        font = QtGui.QFont()
        font2 = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(7)
        self.setWindowTitle('Матричный калькулятор')
        font2.setPointSize(14)
        font2.setFamily("Bahnschrift")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(True)
        self.ui.label_A.setText(list_rus[0])
        self.ui.label_A.setFont(font2)
        self.ui.label_B.setText(list_rus[1])
        self.ui.label_B.setFont(font2)
        self.ui.label_C.setText(list_rus[2])
        self.ui.label_M.setText(list_rus[3])
        self.ui.butcopy.setText(list_rus[4])
        self.ui.butpaste.setText(list_rus[5])
        self.ui.butclear.setText(list_rus[6])
        self.ui.butTran.setText(list_rus[8])
        self.ui.butTran.setFont(font)
        self.ui.butInv.setText(list_rus[9])
        self.ui.butInv.setFont(font)
        self.ui.butRank.setText(list_rus[7])
        self.ui.butRank.setFont(font)
        self.ui.butMult.setText(list_rus[10])
        self.ui.butMult.setFont(font)
        self.ui.butDet.setText(list_rus[11])
        self.ui.butDet.setFont(font)
        self.ui.butPow.setText(list_rus[12])
        self.ui.butPow.setFont(font)
        self.ui.butMat.setText(list_rus[13])
        self.ui.butMat.setFont(font)
        self.ui.butRows.setText(list_rus[14])
        self.ui.butRows.setFont(font)
        self.ui.butCol.setText(list_rus[15])
        self.ui.butCol.setFont(font)
        self.ui.comboBox_fmat.clear()
        self.ui.comboBox_fmat.addItem(list_rus[28])
        self.ui.comboBox_fmat.addItems(list_rus[18:28:1])
        self.ui.comboBox_m.clear()
        self.ui.comboBox_m.addItems(list_rus[0:3:1])
        self.ui.comboBox_m_2.clear()
        self.ui.comboBox_m_2.addItems(list_rus[0:2:1])
        self.ui.comboBox_clear.clear()
        self.ui.comboBox_clear.addItems(list_rus[0:3:1])
        self.ui.comboBox_clear.addItem(list_rus[16])
        self.ui.comboBox_clear.addItem(list_rus[17])
        self.ui.menuSettings.setTitle(list_rus[29])
        self.ui.actionHelp.setText(list_rus[30])
        self.ui.menuLanguage.setTitle(list_rus[31])
        self.ui.actionRussian.setText(list_rus[32])
        self.ui.actionEnglish.setText(list_rus[33])
        self.ui.menuChange_theme.setTitle(list_rus[34])
        self.ui.actionBlack.setText(list_rus[35])
        self.ui.actionWhite.setText(list_rus[36])

    def langE(self):
        le = HelpWindow()
        le.eng()
        list_eng = [
    self.tr('Matrix A'),
    self.tr('Matrix B'),
    self.tr('Result'),
    self.tr('Select matrix:'),
    self.tr('Copy'),
    self.tr('Paste'),
    self.tr('Clear'),
    self.tr('Rank'),
    self.tr('Transpose'),
    self.tr('Inverse'),
    self.tr('Multiply on number'),
    self.tr('Determinant'),
    self.tr('Raise to power'),
    self.tr('Fill matrix'),
    self.tr('Fill row'),
    self.tr('Fill column'),
    self.tr('Matrices'),
    self.tr('All'),
    self.tr('0'),
    self.tr('1'),
    self.tr('2'),
    self.tr('3'),
    self.tr('4'),
    self.tr('5'),
    self.tr('6'),
    self.tr('7'),
    self.tr('8'),
    self.tr('9'),
    self.tr('random'),
    self.tr('Settings'),
    self.tr('Help'),
    self.tr('Language'),
    self.tr('Russian'),
    self.tr('English'),
    self.tr('Theme'),
    self.tr('Black'),
    self.tr('White')
    ]
        font = QtGui.QFont()
        font2 = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setFamily("3ds")
        font2.setFamily("Bahnschrift")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(True)
        self.setWindowTitle('Matrix calculator')
        self.ui.label_A.setText(list_eng[0])
        self.ui.label_A.setFont(font2)
        self.ui.label_B.setText(list_eng[1])
        self.ui.label_B.setFont(font2)
        self.ui.label_C.setText(list_eng[2])
        self.ui.label_C.setFont(font2)
        self.ui.label_M.setText(list_eng[3])
        self.ui.butcopy.setText(list_eng[4])
        self.ui.butpaste.setText(list_eng[5])
        self.ui.butclear.setText(list_eng[6])
        self.ui.butTran.setText(list_eng[8])
        self.ui.butTran.setFont(font)
        self.ui.butInv.setText(list_eng[9])
        self.ui.butInv.setFont(font)
        self.ui.butRank.setText(list_eng[7])
        self.ui.butRank.setFont(font)
        self.ui.butMult.setText(list_eng[10])
        self.ui.butMult.setFont(font)
        self.ui.butDet.setText(list_eng[11])
        self.ui.butDet.setFont(font)
        self.ui.butPow.setText(list_eng[12])
        self.ui.butPow.setFont(font)
        self.ui.butMat.setText(list_eng[13])
        self.ui.butMat.setFont(font)
        self.ui.butRows.setText(list_eng[14])
        self.ui.butRows.setFont(font)
        self.ui.butCol.setText(list_eng[15])
        self.ui.butCol.setFont(font)
        self.ui.comboBox_fmat.clear()
        self.ui.comboBox_fmat.addItem(list_eng[28])
        self.ui.comboBox_fmat.addItems(list_eng[18:28:1])
        self.ui.comboBox_m.clear()
        self.ui.comboBox_m.addItems(list_eng[0:3:1])
        self.ui.comboBox_m_2.clear()
        self.ui.comboBox_m_2.addItems(list_eng[0:2:1])
        self.ui.comboBox_clear.clear()
        self.ui.comboBox_clear.addItems(list_eng[0:3:1])
        self.ui.comboBox_clear.addItem(list_eng[16])
        self.ui.comboBox_clear.addItem(list_eng[17])
        self.ui.menuSettings.setTitle(list_eng[29])
        self.ui.actionHelp.setText(list_eng[30])
        self.ui.menuLanguage.setTitle(list_eng[31])
        self.ui.actionRussian.setText(list_eng[32])
        self.ui.actionEnglish.setText(list_eng[33])
        self.ui.menuChange_theme.setTitle(list_eng[34])
        self.ui.actionBlack.setText(list_eng[35])
        self.ui.actionWhite.setText(list_eng[36])

    def themeB(self):
        tb = HelpWindow()
        tb.styleB()
        self.setStyleSheet(open('styles/styleB.css').read())
        self.ui.line.setStyleSheet('color: grey')
        self.ui.line_2.setStyleSheet('color: grey')
        self.ui.line_3.setStyleSheet('color: grey')
        self.ui.line_4.setStyleSheet('color: grey')
        self.ui.line_5.setStyleSheet('color: grey')
        self.update()

    def themeW(self):
        tw = HelpWindow()
        tw.styleW()
        self.setStyleSheet(open('styles/styleW.css').read())
        self.update()

    def open(self, window, msg):
        if window == 1:
            self.help_form = HelpWindow()
            self.help_form.show()
        elif window == 2:
            self.errmsg = ErrorWindow()
            self.errmsg.ew.label.setText(msg)
            self.errmsg.show()

    def help(self):
        self.open(1, msg = None)

    def matA(self):
        row = self.ui.table_A.rowCount()
        column = self.ui.table_A.columnCount()
        mat_a = []
        for i in range(0, row):
            mat_a.append([])
            for j in range(0, column):
                mat_a[i].append(float(self.ui.table_A.item(i, j).text()))
        self.ui.table_A.resizeColumnsToContents()
        self.ui.table_A.resizeRowsToContents()
        mat_a = np.array(mat_a)
        return mat_a

    def matB(self):
        row = self.ui.table_B.rowCount()
        column = self.ui.table_B.columnCount()
        mat_b = []
        for i in range(0, row):
            mat_b.append([])
            for j in range(0, column):
                mat_b[i].append(float(self.ui.table_B.item(i, j).text()))
        self.ui.table_B.resizeColumnsToContents()
        self.ui.table_B.resizeRowsToContents()
        mat_b = np.array(mat_b)
        return mat_b

    def matC(self, ans):
        size = np.shape(ans)
        self.ui.table_C.setRowCount(size[0])
        self.ui.table_C.setColumnCount(size[1])
        row = self.ui.table_C.rowCount()
        column = self.ui.table_C.columnCount()
        for i in range(0, row):
            for j in range(0, column):
                mat_c = QtWidgets.QTableWidgetItem()
                mat_c.setText(str(ans[i][j]))
                self.ui.table_C.setItem(i, j, mat_c)
        self.ui.table_C.resizeColumnsToContents()
        self.ui.table_C.resizeRowsToContents()

    def matCC(self):
        row = self.ui.table_C.rowCount()
        column = self.ui.table_C.columnCount()
        mat_c = []
        for i in range(0, row):
            mat_c.append([])
            for j in range(0, column):
                mat_c[i].append(int(self.ui.table_C.item(i, j).text()))

    def rows_a(self, value):
        self.ui.table_A.setRowCount(value)
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            spin_row = self.ui.spinBox_A_rows.text()
            self.ui.comboBox_frows.clear()
            for i in range(1, int(spin_row)+1):
                self.ui.comboBox_frows.addItem(str(i))

    def cols_a(self, value):
        self.ui.table_A.setColumnCount(value)
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            spin_col = self.ui.spinBox_A_col.text()
            self.ui.comboBox_fcol.clear()
            for i in range(1, int(spin_col)+1):
                self.ui.comboBox_fcol.addItem(str(i))

    def rows_b(self, value):
        self.ui.table_B.setRowCount(value)
        if self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            spin_row_b = self.ui.spinBox_B_rows.text()
            self.ui.comboBox_frows.clear()
            for i in range(1, int(spin_row_b)+1):
                self.ui.comboBox_frows.addItem(str(i))
        else: pass

    def cols_b(self, value):
        self.ui.table_B.setColumnCount(value)
        if self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            spin_col_b = self.ui.spinBox_B_col.text()
            self.ui.comboBox_fcol.clear()
            for i in range(1, int(spin_col_b)+1):
                self.ui.comboBox_fcol.addItem(str(i))
        else: pass

    def change(self):
        try:
            row = self.ui.table_A.rowCount()
            column = self.ui.table_A.columnCount()
            mat_a = []
            for i in range(0, row):
                mat_a.append([])
                for j in range(0, column):
                    mat_a[i].append(self.ui.table_A.item(i, j).text())
            row = self.ui.table_B.rowCount()
            column = self.ui.table_B.columnCount()
            mat_b = []
            for i in range(0, row):
                mat_b.append([])
                for j in range(0, column):
                    mat_b[i].append(self.ui.table_B.item(i, j).text())
            a = np.array(mat_a)
            b = np.array(mat_b)
            a = np.float64(a)
            b = np.float64(b)
            ans_a = a
            ans_b = b
            self.ui.table_B.setRowCount(row)
            self.ui.table_B.setColumnCount(column)
            for i in range(0, row):
                for j in range(0, column):
                    res = QtWidgets.QTableWidgetItem()
                    res.setText(str(ans_a[i][j]))
                    self.ui.table_B.setItem(i, j, res)
            self.ui.table_A.setRowCount(row)
            self.ui.table_A.setColumnCount(column)
            for i in range(0, row):
                for j in range(0, column):
                    res = QtWidgets.QTableWidgetItem()
                    res.setText(str(ans_b[i][j]))
                    self.ui.table_A.setItem(i, j, res)
        except:
            self.open(2, msg = 'Ошибка!')

    def plus(self):
        try:
            a = self.matA()
            b = self.matB()
            ans = a + b
            self.matC(ans)
        except:
            self.open(2, msg = 'Ошибка!')

    def min(self):
        try:
            a = self.matA()
            b = self.matB()
            ans = a - b
            self.matC(ans)
        except:
            self.open(2, msg = 'Ошибка!')

    def mul(self):
        try:
            a = self.matA()
            b = self.matB()
            ans = a.dot(b)
            ans = np.round(ans, 2)
            self.matC(ans)
        except:
            self.open(2, msg = 'Ошибка!')

    def div(self):
        try:
            a = self.matA()
            b = self.matB()
            ans = a.dot(np.linalg.inv(b))
            ans = np.round(ans, 5)
            self.matC(ans)
        except:
            self.open(2, msg = 'Ошибка!')

    def copy_m(self):
        try:
            if self.ui.comboBox_m.currentText() == 'Matrix A' or self.ui.comboBox_m.currentText() == 'Матрица А':
                mat_a = self.matA()
                ans_copy = np.copy(mat_a)
                ans_copy = ans_copy.tolist()
                ans_copy = tuple(ans_copy)
            elif self.ui.comboBox_m.currentText() == 'Matrix B' or self.ui.comboBox_m.currentText() == 'Матрица В':
                mat_b = self.matB()
                ans_copy = np.copy(mat_b)
                ans_copy = ans_copy.tolist()
                ans_copy = tuple(ans_copy)
            elif self.ui.comboBox_m.currentText() == 'Result' or self.ui.comboBox_m.currentText() == 'Результат':
                mat_c = self.matCC()
                ans_copy = np.copy(mat_c)
                ans_copy = ans_copy.tolist()
                ans_copy = tuple(ans_copy)
            globals()['ans'] = ans_copy
        except:
            self.open(2, msg = 'Ошибка!')

    def paste(self):
        try:
            ans_past = globals()['ans']
            ans_paste = np.array(ans_past)
            x = np.shape(ans_paste)
            if self.ui.comboBox_m.currentText() == 'Matrix A' or self.ui.comboBox_m.currentText() == 'Матрица А':
                self.ui.table_A.setRowCount(x[0])
                self.ui.table_A.setColumnCount(x[1])
                row = self.ui.table_A.rowCount()
                column = self.ui.table_A.columnCount()
                for i in range(0, row):
                    for j in range(0, column):
                        res = QtWidgets.QTableWidgetItem()
                        res.setText(str(ans_paste[i][j]))
                        self.ui.table_A.setItem(i, j, res)
                self.ui.table_A.resizeColumnsToContents()
                self.ui.table_A.resizeRowsToContents()
            elif self.ui.comboBox_m.currentText() == 'Matrix B' or self.ui.comboBox_m.currentText() == 'Матрица В':
                self.ui.table_B.setRowCount(x[0])
                self.ui.table_B.setColumnCount(x[1])
                row = self.ui.table_B.rowCount()
                column = self.ui.table_B.columnCount()
                for i in range(0, row):
                    for j in range(0, column):
                        res = QtWidgets.QTableWidgetItem()
                        res.setText(str(ans_paste[i][j]))
                        self.ui.table_B.setItem(i, j, res)
                self.ui.table_B.resizeColumnsToContents()
                self.ui.table_B.resizeRowsToContents()
            elif self.ui.comboBox_m.currentText() == 'Result' or self.ui.comboBox_m.currentText() == 'Результат':
                self.ui.table_C.setRowCount(x[0])
                self.ui.table_C.setColumnCount(x[1])
                row = self.ui.table_C.rowCount()
                column = self.ui.table_C.columnCount()
                for i in range(0, row):
                    for j in range(0, column):
                        res = QtWidgets.QTableWidgetItem()
                        res.setText(str(ans_paste[i][j]))
                        self.ui.table_C.setItem(i, j, res)
                self.ui.table_C.resizeColumnsToContents()
                self.ui.table_C.resizeRowsToContents()
        except:
            self.open(2, msg = 'Ошибка!')

    def tran(self):
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            try:
                ans = self.matA()
                ans = ans.transpose()
            except:
                self.open(2, msg = 'Ошибка!')
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            try:
                ans = self.matB()
                ans = ans.transpose()
            except:
                self.open(2, msg = 'Ошибка!')
        try:
            ans = self.matC(ans)
        except:
            self.open(2, msg = 'Ошибка!')

    def inv(self):
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            try:
                ans = self.matA()
                ans = np.round(np.linalg.inv(ans), 2)
            except:
                self.open(2, msg = 'Ошибка!')
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            try:
                ans = self.matB()
                ans = np.round(np.linalg.inv(ans), 2)
            except:
                self.open(2, msg = 'Ошибка!')
        try:
            ans = self.matC(ans)
        except:
            self.open(2, msg = 'Ошибка!')

    def rank(self):
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            try:
                ans = self.matA()
            except:
                self.open(2, msg = 'Ошибка!')
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            try:
                ans = self.matB()
            except:
                self.open(2, msg = 'Ошибка!')
        try:
            ans = np.round(np.linalg.matrix_rank(ans), 2)
            self.ui.lineRank.setText(str(ans))
        except:
            self.open(2, msg = 'Ошибка!')

    def mult(self):
        try:
            num_dot = np.float64(self.ui.numult.text())
        except:
            self.open(2, msg = 'Ошибка!')
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            try:
                ans = self.matA()
                ans = np.float64(ans)*num_dot
            except:
                self.open(2, msg = 'Ошибка!')
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            try:
                ans = self.matB()
                ans = np.float64(ans)*num_dot
            except:
                self.open(2, msg = 'Ошибка!')
        ans = np.round(ans, 5)
        ans = self.matC(ans)

    def det(self):
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            try:
                ans = self.matA()
            except:
                self.open(2, msg = 'Ошибка!')
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            try:
                ans = self.matB()
            except:
                self.open(2, msg = 'Ошибка!')
        try:
            ans = np.round(np.linalg.det(ans), 2)
            self.ui.numdet.setText(str(ans))
            if ans == 0:
                self.ui.butInv.hide()
            elif (ans == ' ') or (ans > 0) or (ans < 0):
                self.ui.butInv.show()
        except:
            self.open(2, msg = 'Ошибка!')


    def pow(self):
        try:
            num_pow = np.int64(self.ui.numpow.text())
        except:
            self.open(2, msg = 'Ошибка!')
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            try:
                ans = self.matA()
                ans = np.round(np.linalg.matrix_power(np.float64(ans), num_pow), 2)
            except:
                self.open(2, msg = 'Ошибка!')
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            try:
                ans = self.matB()
                ans = np.round(np.linalg.matrix_power(np.float64(ans), num_pow), 2)
            except:
                self.open(2, msg = 'Ошибка!')
        try:
            ans = self.matC(ans)
        except:
            self.open(2, msg = 'Ошибка!')

    def mat(self):
        array_check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'random', 'Рандом']
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            row = self.ui.table_A.rowCount()
            column = self.ui.table_A.columnCount()
            mat_a = []
            for i in range(0, row):
                mat_a.append([])
                for j in range(0, column):
                    mat_a[i].append(self.ui.table_A.item(i, j))
            mat_a = np.array(mat_a)
            if self.ui.comboBox_fmat.currentText() in array_check:
                check = self.ui.comboBox_fmat.currentText()
                if check != 'random' and check != 'Рандом':
                    mat_a[...] = int(check)
                elif check == 'random' or check == 'Рандом':
                    for i in range(0, row):
                        for j in range(0, column):
                            mat_a[i, j] = random.randint(0, 255)
            ans = mat_a
            self.ui.table_A.setRowCount(row)
            self.ui.table_A.setColumnCount(column)
            for i in range(0, row):
                for j in range(0, column):
                    res = QtWidgets.QTableWidgetItem()
                    res.setText(str(ans[i][j]))
                    self.ui.table_A.setItem(i, j, res)
            self.ui.table_A.resizeColumnsToContents()
            self.ui.table_A.resizeRowsToContents()

        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            row = self.ui.table_B.rowCount()
            column = self.ui.table_B.columnCount()
            mat_b = []
            for i in range(0, row):
                mat_b.append([])
                for j in range(0, column):
                    mat_b[i].append(self.ui.table_B.item(i, j))
            mat_b = np.array(mat_b)
            if self.ui.comboBox_fmat.currentText() in array_check:
                check = self.ui.comboBox_fmat.currentText()
                if check != 'random' and check != 'Рандом':
                    mat_b[...] = int(check)
                elif check == 'random' or check == 'Рандом':
                    for i in range(0, row):
                        for j in range(0, column):
                            mat_b[i, j] = random.randint(0, 255)
                ans = mat_b
                self.ui.table_B.setRowCount(row)
                self.ui.table_B.setColumnCount(column)
                for i in range(0, row):
                    for j in range(0, column):
                        res = QtWidgets.QTableWidgetItem()
                        res.setText(str(ans[i][j]))
                        self.ui.table_B.setItem(i, j, res)
                self.ui.table_B.resizeColumnsToContents()
                self.ui.table_B.resizeRowsToContents()

    def rows(self):
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            for i in range(0, self.ui.table_A.columnCount()):
                res = QtWidgets.QTableWidgetItem()
                res.setText(self.ui.comboBox_fmat.currentText())
                if res.text() != 'random' or res.text() != 'Рандом':
                    self.ui.table_A.setItem(int(self.ui.comboBox_frows.currentText())-1, i, res)
                if res.text() == 'random' or res.text() == 'Рандом':
                    res.setText(str(random.randint(0, 255)))
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            for i in range(0, self.ui.table_B.columnCount()):
                res = QtWidgets.QTableWidgetItem()
                res.setText(self.ui.comboBox_fmat.currentText())
                if res.text() != 'random' or res.text() != 'Рандом':
                    self.ui.table_B.setItem(int(self.ui.comboBox_frows.currentText())-1, i, res)
                if res.text() == 'random' or res.text() == 'Рандом':
                    res.setText(str(random.randint(0, 255)))
    def col(self):
        if self.ui.comboBox_m_2.currentText() == 'Matrix A' or self.ui.comboBox_m_2.currentText() == 'Матрица А':
            for i in range(0, self.ui.table_A.rowCount()):
                res = QtWidgets.QTableWidgetItem()
                res.setText(self.ui.comboBox_fmat.currentText())
                if res.text() != 'random' or res.text() != 'Рандом':
                    self.ui.table_A.setItem(i, int(self.ui.comboBox_fcol.currentText())-1, res)
                if res.text() == 'random' or res.text() == 'Рандом':
                    res.setText(str(random.randint(0, 255)))
        elif self.ui.comboBox_m_2.currentText() == 'Matrix B' or self.ui.comboBox_m_2.currentText() == 'Матрица В':
            for i in range(0, self.ui.table_B.rowCount()):
                res = QtWidgets.QTableWidgetItem()
                res.setText(self.ui.comboBox_fmat.currentText())
                if res.text() != 'random' or res.text() != 'Рандом':
                    self.ui.table_B.setItem(i, int(self.ui.comboBox_fcol.currentText())-1, res)
                if res.text() == 'random' or res.text() == 'Рандом':
                    res.setText(str(random.randint(0, 255)))
    def clear(self):
        if self.ui.comboBox_clear.currentText() == 'Matrix A' or self.ui.comboBox_clear.currentText() == 'Матрица А':
            self.ui.butInv.show()
            self.ui.table_A.clearContents()
            self.ui.table_A.resizeColumnsToContents()
            self.ui.table_A.resizeRowsToContents()
        elif self.ui.comboBox_clear.currentText() == 'Matrix B' or self.ui.comboBox_clear.currentText() == 'Матрица В':
            self.ui.butInv.show()
            self.ui.table_B.clearContents()
            self.ui.table_B.resizeColumnsToContents()
            self.ui.table_B.resizeRowsToContents()
        elif self.ui.comboBox_clear.currentText() == 'Result' or self.ui.comboBox_clear.currentText() == 'Результат':
            self.ui.butInv.show()
            self.ui.table_C.clearContents()
            self.ui.table_C.resizeColumnsToContents()
            self.ui.table_C.resizeRowsToContents()
        elif self.ui.comboBox_clear.currentText() == 'Matrices' or self.ui.comboBox_clear.currentText() == 'Все матрицы':
            self.ui.butInv.show()
            self.ui.table_A.clearContents()
            self.ui.table_B.clearContents()
            self.ui.table_C.clearContents()
            self.ui.table_A.resizeColumnsToContents()
            self.ui.table_A.resizeRowsToContents()
            self.ui.table_B.resizeColumnsToContents()
            self.ui.table_B.resizeRowsToContents()
            self.ui.table_C.resizeColumnsToContents()
            self.ui.table_C.resizeRowsToContents()
        elif self.ui.comboBox_clear.currentText() == 'All' or self.ui.comboBox_clear.currentText() == 'Все поля':
            self.ui.butInv.show()
            self.ui.table_A.clearContents()
            self.ui.table_B.clearContents()
            self.ui.table_C.clearContents()
            self.ui.lineRank.clear()
            self.ui.numdet.clear()
            self.ui.numult.clear()
            self.ui.numpow.clear()
            self.ui.table_A.resizeColumnsToContents()
            self.ui.table_A.resizeRowsToContents()
            self.ui.table_B.resizeColumnsToContents()
            self.ui.table_B.resizeRowsToContents()
            self.ui.table_C.resizeColumnsToContents()
            self.ui.table_C.resizeRowsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    prog = MainWindow()
    prog.themeB()
    prog.langR()
    prog.show()
    app.exec_()

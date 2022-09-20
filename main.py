from pak import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys

data = pd.read_excel('Список госпитализированных.xlsx', sheet_name=0, header=4)
data.dropna(axis=0, how='all', inplace=True)
data.drop(columns=['№ п\п', 'Лечащий врач', 'К\д', 'Адрес регистрации', 'Примечание'], axis=1, inplace=True)
data.Палата.fillna(0, inplace=True)
data.insert(0, 'Флаг', '')
headers = data.columns.values.tolist()
wards = data.Палата.unique()

def set_ward():

    print(wards)

def set_table():
    ui.table_main.setColumnCount(len(headers))
    ui.table_main.setHorizontalHeaderLabels(headers)
    for i, row in data.iterrows():
        ui.table_main.setRowCount(ui.table_main.rowCount() + 1)

        for j in range(ui.table_main.columnCount()):
            item = QTableWidgetItem()
            item.setText(str(row[j]))
            ui.table_main.setItem(i, j, item)

    ui.table_main.resizeColumnsToContents()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    set_table()
    set_ward()
    MainWindow.show()
    sys.exit(app.exec_())

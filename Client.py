import webbrowser

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os
import json

ourdump = None
for x in os.listdir(os.getcwd()):
    if 'LudeonDump' in x and '.json' in x:
        print("found DumpedFile... Loading...")
        try:
            with open(os.path.join(os.getcwd(), x)) as f:
                ourdump = json.load(f)
            f.close()
        except Exception as e:
            print(e)
            print("Failed to load dump!")
        break
if ourdump is None:
    sys.exit("Dumped File Not found.")


def OpenLink(item):
    if item.column() == 1:
        webbrowser.open(item.text())


def main():
    app = QApplication(sys.argv)
    table = QTableWidget()
    table.itemDoubleClicked.connect(OpenLink)
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    table.viewOptions()
    table.verticalHeader().setResizeMode(2)

    table.setWindowTitle("Ludeon Forum Browser [Development Build]")
    table.resize(700, 800)
    table.setRowCount(len(ourdump))
    table.setColumnCount(3)
    rowwork = 0
    for y in ourdump:
        table.setItem(rowwork, 0, QTableWidgetItem(y['title']))
        table.setItem(rowwork, 1, QTableWidgetItem(y['url']))
        table.setItem(rowwork, 2, QTableWidgetItem(y['version']))
        rowwork += 1

    table.setSortingEnabled(True)
    table.show()
    return app.exec_()


if __name__ == '__main__':
    main()

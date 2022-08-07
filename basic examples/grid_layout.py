import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QGridLayout')

layout = QGridLayout()

for i in range(3):
    for j in range(3):
        if(i == 2 and j > 0):
            break
        else:
            layout.addWidget(QPushButton("Botton (%d, %d)" % (i, j)), i, j)

layout.addWidget(QPushButton("Botton (2, 1) + 2 Columns span"), 2, 1, 1, 2)
window.setLayout(layout)

window.show()

sys.exit(app.exec())

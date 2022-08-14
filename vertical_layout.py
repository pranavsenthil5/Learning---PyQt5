import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QVBoxLayout')

layout = QVBoxLayout()

layout.addWidget(QPushButton("Top"), 1)
layout.addWidget(QPushButton("Middle"), 2)
layout.addWidget(QPushButton("Bottom"), 3)

window.setLayout(layout)

window.show()

sys.exit(app.exec())

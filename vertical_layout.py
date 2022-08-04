import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QVBoxLayout')

layout = QVBoxLayout()

layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Middle"))
layout.addWidget(QPushButton("Bottom"))

window.setLayout(layout)

window.show()

sys.exit(app.exec())

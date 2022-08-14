import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit, QPushButton


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        textEdit1 = QTextEdit("LHS rectangle")
        textEdit2 = QTextEdit("Bottom rectangle")
        textEdit3 = QTextEdit("Central square")
        self.gridLayout = QGridLayout()
        # self.gridLayout.addWidget(textEdit1, 0, 0, 2, 0)
        # self.gridLayout.addWidget(textEdit2, 2, 1, 0, 2)
        # self.gridLayout.addWidget(textEdit3, 0, 1, 2, 2)
        self.gridLayout.addWidget(textEdit1, 0, 0)
        self.gridLayout.addWidget(textEdit2, 1, 1)
        self.gridLayout.addWidget(textEdit3, 0, 1)
        # self.gridLayout.setColumnStretch(0, 1)
        # self.gridLayout.setColumnStretch(1, 3)
        # self.gridLayout.setRowStretch(0, 3)
        # self.gridLayout.setRowStretch(1, 1)

        self.setLayout(self.gridLayout)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

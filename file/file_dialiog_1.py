import sys

from PyQt5.QtWidgets import QApplication, QCheckBox, QDialog, QFileDialog


class ChkBxFileDialog(QFileDialog):
    def __init__(self, chkBxTitle="", filter="*.txt"):
        super().__init__(filter=filter)
        self.setSupportedSchemes(["file"])
        self.setOption(QFileDialog.DontUseNativeDialog)
        self.setAcceptMode(QFileDialog.AcceptSave)
        self.selectNameFilter("*.txt")
        chkBx = QCheckBox(chkBxTitle)
        self.layout().addWidget(chkBx)


def main():
    app = QApplication(sys.argv)
    dialog = ChkBxFileDialog()
    if dialog.exec_() == QDialog.Accepted:
        filename = dialog.selectedUrls()[0].toLocalFile()
        print(filename)


if __name__ == "__main__":
    main()

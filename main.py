import sys
import signal

from app.widget import AppWindow
from PySide6 import QtWidgets

# Make QTWindow
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = AppWindow()
    window.show()

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec())

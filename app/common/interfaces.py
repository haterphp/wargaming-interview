from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPoint

from app.common.utils import IWindowBorders, IWindowSetting


class IAppWindow(QMainWindow):
    def __init__(self, settings: IWindowSetting):
        super().__init__()

        # Apply window settings
        self.setWindowTitle(settings.title)
        self.setGeometry(settings.top, settings.left, settings.width, settings.height)

        # Define window borders
        self.borders = IWindowBorders(self)

    # Event for update window borders
    def resizeEvent(self, event):
        self.borders.recalculate()


class IAppModel:
    def __init__(self, window: IAppWindow):
        self.window = window

    def makeANewRectangle(self, point: QPoint):
        pass

    def findAndSetDraggedElement(self, point: QPoint) -> bool:
        return False

    def moveDraggedRectByPoint(self, point: QPoint):
        pass

    def resetDraggedElement(self):
        pass

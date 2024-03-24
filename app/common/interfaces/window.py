from PySide6.QtWidgets import QMainWindow

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
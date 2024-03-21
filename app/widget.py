from settings import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT

from PySide6.QtGui import QPainter

from app.common.utils import IWindowSetting
from app.common.interfaces import IAppWindow

from app.model import AppModel


class AppWindow(IAppWindow):

    def __init__(self):

        # Define window settings
        settings = IWindowSetting(
            title=WINDOW_TITLE,
            top=100,
            left=100,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        super().__init__(settings)

        # Define AppModel
        self.__model = AppModel(self)

    def paintEvent(self, event):
        painter = QPainter(self)

        for rect in self.__model.rectangles:
            rect.draw(painter)

    # Mouse event handlers
    def mouseDoubleClickEvent(self, event):
        self.__model.eventsHandler.mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        self.__model.eventsHandler.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.__model.eventsHandler.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.__model.eventsHandler.mouseReleaseEvent(event)


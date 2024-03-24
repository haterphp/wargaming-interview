from settings import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT

from PySide6.QtGui import QPainter

from app.common.utils import IWindowSetting
from app.common.interfaces.window import IAppWindow

from app.model import AppModel
from app.menu import AppMenuWidget


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

        # Define AppMenu controller
        self.__menu = AppMenuWidget(self, self.__model)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw rectangles on scene
        for rect in self.__model.rectangleModel.rectangles:
            rect.draw(painter)

        # Draw lines on scene
        for line in self.__model.lineModel.lines:
            line.draw(painter)

    # Mouse event handlers
    def mouseDoubleClickEvent(self, event):
        self.__model.eventsHandler.mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        self.__model.eventsHandler.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.__model.eventsHandler.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.__model.eventsHandler.mouseReleaseEvent(event)


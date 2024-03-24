from PySide6.QtWidgets import QMainWindow

from settings import WINDOW_MENU_HEIGHT


class IWindowBorders:
    def __init__(self, window: QMainWindow):
        self.__window = window

        self.__left = 0
        self.__right = window.width()

        self.__top = WINDOW_MENU_HEIGHT
        self.__bottom = window.height()

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def top(self):
        return self.__top

    @property
    def bottom(self):
        return self.__bottom

    def recalculate(self):
        self.__right = self.__window.width()
        self.__bottom = self.__window.height()


class IWindowSetting:
    def __init__(self, top: int, left: int, width: int, height: int, title: str):
        self.__title = title

        self.__top = top
        self.__left = left

        self.__width = width
        self.__height = height

    @property
    def title(self):
        return self.__title

    @property
    def top(self):
        return self.__top

    @property
    def left(self):
        return self.__left

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

class IRectMoveOffsets:
    def __init__(self, x: int, y: int):
        self.__offsetX = x
        self.__offsetY = y

    @property
    def offsetX(self):
        return self.__offsetX

    @property
    def offsetY(self):
        return self.__offsetY


class IRectPosition:
    def __init__(self, left: int, right: int, top: int, bottom: int):
        self.__left = left
        self.__right = right
        self.__top = top
        self.__bottom = bottom

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

    def setLeft(self, left: int):
        self.__left = left

    def setRight(self, right: int):
        self.__right = right

    def setTop(self, top: int):
        self.__top = top

    def setBottom(self, bottom: int):
        self.__bottom = bottom

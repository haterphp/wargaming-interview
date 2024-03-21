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


class IRectMoveBorders:
    def __init__(self, right: int, bottom: int, left: int = 0, top: int = 0):
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

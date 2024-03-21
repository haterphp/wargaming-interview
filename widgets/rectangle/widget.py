from PySide6.QtCore import QRect, QPoint, Qt

from random import choice

from PySide6.QtGui import QPainter

from widgets.common.widget import IProjectWidget
from widgets.rectangle.utils import IRectMoveOffsets, IRectMoveBorders

from settings import RECTANGLE_COLORS


class RectWidget(QRect, IProjectWidget):

    def __init__(self, start: QPoint, end: QPoint):
        super().__init__(start, end)

        # Choice random color
        self.__color = choice(RECTANGLE_COLORS)

    def draw(self, painter: QPainter):
        painter.setPen(Qt.NoPen)

        painter.fillRect(self, self.__color)
        painter.drawRect(self.normalized())

    def recalculate(self, offsets: IRectMoveOffsets, borders: IRectMoveBorders):
        self.__moveXCoordinate(offsets.offsetX, borders)
        self.__moveYCoordinate(offsets.offsetY, borders)

    def __moveXCoordinate(self, offset: int, borders: IRectMoveBorders):
        left = self.left() + offset
        right = self.right() + offset

        if left > borders.left and right < borders.right:
            self.moveLeft(left)

    def __moveYCoordinate(self, offset: int, borders: IRectMoveBorders):
        top = self.top() + offset
        bottom = self.bottom() + offset

        if top > borders.top and bottom < borders.bottom:
            self.moveTop(top)

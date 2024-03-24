from random import choice

from PySide6.QtCore import QRect, QPoint, Qt
from PySide6.QtGui import QPainter

from widgets.common.widget import IProjectWidget
from widgets.rectangle.utils import IRectPosition

from settings import RECTANGLE_HALF_WIDTH, RECTANGLE_HALF_HEIGHT, RECTANGLE_COLORS


class RectWidget(QRect, IProjectWidget):

    def __init__(self, position: IRectPosition):
        start = QPoint(position.left, position.top)
        end = QPoint(position.right, position.bottom)

        super().__init__(start, end)

        # Choice random color
        self.__color = choice(RECTANGLE_COLORS)

    # Get rectangle center coordinate
    def getCenterCoordinates(self) -> QPoint:
        return QPoint(
            self.left() + RECTANGLE_HALF_WIDTH,
            self.top() + RECTANGLE_HALF_HEIGHT
        )

    def draw(self, painter: QPainter):
        painter.setPen(Qt.NoPen)

        painter.fillRect(self, self.__color)
        painter.drawRect(self.normalized())

    # Move rectangle to position
    def move(self, position: IRectPosition):
        self.setLeft(position.left)
        self.setRight(position.right)
        self.setTop(position.top)
        self.setBottom(position.bottom)

        # Emit new position for all connections
        self.emitUpdates(self.getCenterCoordinates())

    # Emit new position for subscribers
    def emitUpdates(self, position: QPoint):
        for callback in self._subscribeCallbacks:
            callback(position)

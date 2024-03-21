from typing import List

from PySide6.QtCore import QPoint

from app.common.interfaces import IAppModel, IAppWindow
from app.events import AppMouseEventsHandler

from widgets.rectangle.widget import RectWidget
from widgets.rectangle.utils import IRectMoveOffsets

from settings import RECTANGLE_WIDTH, RECTANGLE_HEIGHT


class AppModel(IAppModel):
    def __init__(self, window: IAppWindow):
        super().__init__(window)

        self.eventsHandler = AppMouseEventsHandler(self)

        # Define list for our RectWidgets
        self.rectangles: List[RectWidget] = []

        # Define variables for dragged element
        self.__draggedRect: RectWidget | None = None
        self.__lastEventPoint: QPoint | None = None

    def resetDraggedElement(self):
        self.__draggedRect = None
        self.__lastEventPoint = None

    def findAndSetDraggedElement(self, point: QPoint) -> bool:
        self.__draggedRect = self.__getRectByPosition(point)

        if self.__draggedRect is not None:
            self.__lastEventPoint = point
            return True

        super().findAndSetDraggedElement(point)

    def moveDraggedRectByPoint(self, point: QPoint):
        if self.__draggedRect is not None:

            offsets = IRectMoveOffsets(
                x=point.x() - self.__lastEventPoint.x(),
                y=point.y() - self.__lastEventPoint.y()
            )

            self.__draggedRect.recalculate(offsets, self.window.borders)
            self.__lastEventPoint = point

    def makeANewRectangle(self, point: QPoint):
        x = point.x()
        y = point.y()

        HALF_WIDTH = RECTANGLE_WIDTH / 2
        HALF_HEIGHT = RECTANGLE_HEIGHT / 2

        rect = RectWidget(
            QPoint(
                x - HALF_WIDTH,
                y - HALF_HEIGHT
            ),
            QPoint(
                x + HALF_WIDTH,
                y + HALF_HEIGHT
            ),
        )

        self.rectangles.append(rect)

    def __getRectByPosition(self, point: QPoint) -> (RectWidget | None):
        x = point.x()
        y = point.y()

        for rect in self.rectangles:
            if rect.left() < x < rect.right() and rect.top() < y < rect.bottom():
                return rect

        return None

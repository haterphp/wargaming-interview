from typing import Optional

from PySide6.QtCore import QPoint

from widgets.rectangle.widget import RectWidget
from widgets.rectangle.utils import IRectPosition, IRectMoveOffsets

from app.common.interfaces.models import IRectangleModel
from app.common.interfaces.window import IAppWindow

from settings import RECTANGLE_HALF_WIDTH, RECTANGLE_HALF_HEIGHT


class RectangleModel(IRectangleModel):
    def __init__(self, window: IAppWindow):
        super().__init__(window)

        # Define variables for dragged element
        self.__draggedRect: Optional[RectWidget] = None
        self.__lastEventPoint: Optional[QPoint] = None

    # Make new Rect by coordinate
    def makeANewRectangle(self, point: QPoint):
        x = point.x()
        y = point.y()

        position = IRectPosition(
            left=x - RECTANGLE_HALF_WIDTH,
            right=x + RECTANGLE_HALF_WIDTH,
            top=y - RECTANGLE_HALF_HEIGHT,
            bottom=y + RECTANGLE_HALF_HEIGHT,
        )

        if self.__isCollsionDetected(position) is not True:
            rect = RectWidget(position)
            self.rectangles.append(rect)

    # Find rect in painter by coordinate
    def findRectByPosition(self, point: QPoint) -> Optional[RectWidget]:
        x = point.x()
        y = point.y()

        for rect in self.rectangles:
            if rect.left() < x < rect.right() and rect.top() < y < rect.bottom():
                return rect

        return None

    # Find dragged element by coordinates
    def findAndSetDraggedElement(self, point: QPoint) -> bool:
        self.__draggedRect = self.findRectByPosition(point)

        if self.__draggedRect is not None:
            self.__lastEventPoint = point
            return True

        super().findAndSetDraggedElement(point)

    # Move rect to new coordinates
    def moveDraggedRectByPoint(self, point: QPoint):
        if self.__draggedRect is not None:
            offsets = IRectMoveOffsets(
                x=point.x() - self.__lastEventPoint.x(),
                y=point.y() - self.__lastEventPoint.y()
            )

            newPosition = self.__calculateNextRectPosition(offsets)

            self.__draggedRect.move(newPosition)
            self.__lastEventPoint = point

    # Cancel drag event
    def resetDraggedElement(self):
        self.__draggedRect = None
        self.__lastEventPoint = None

    def __calculateNextRectPosition(self, offsets: IRectMoveOffsets) -> IRectPosition:
        rectPosition = IRectPosition(
            left=self.__draggedRect.left(),
            right=self.__draggedRect.right(),
            top=self.__draggedRect.top(),
            bottom=self.__draggedRect.bottom()
        )

        nextRectPosition = IRectPosition(
            left=rectPosition.left + offsets.offsetX,
            right=rectPosition.right + offsets.offsetX,
            top=rectPosition.top + offsets.offsetY,
            bottom=rectPosition.bottom + offsets.offsetY
        )

        if self.__isCollsionDetected(nextRectPosition):
            return rectPosition

        return nextRectPosition

    # Detect collision with window borders and other rects
    def __isCollsionDetected(self, position: IRectPosition) -> bool:
        return self.__isCollisionWithOtherRects(position) or any(self.__isCollisionWithWindowBorders(position))

    def __isCollisionWithWindowBorders(self, position: IRectPosition) -> [bool, bool]:
        collisionX = True
        collisionY = True

        borders = self.window.borders

        if position.left > borders.left and position.right < borders.right:
            collisionX = False

        if position.top > borders.top and position.bottom < borders.bottom:
            collisionY = False

        return [collisionX, collisionY]

    def __isCollisionWithOtherRects(self, position: IRectPosition) -> bool:
        for rect in self.rectangles:
            if rect == self.__draggedRect:
                continue

            if (position.left < rect.right() and
                    rect.left() < position.right and
                    position.top < rect.bottom() and
                    rect.top() < position.bottom):
                return True

        return False
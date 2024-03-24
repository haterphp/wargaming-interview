from typing import Optional

from PySide6.QtCore import QPoint

from app.common.interfaces.models import ILineModel
from app.common.interfaces.window import IAppWindow

from widgets.line.widget import LineWidget
from widgets.rectangle.widget import RectWidget


class LineModel(ILineModel):
    def __init__(self, window: IAppWindow):
        super().__init__(window)

        self.__targetRect: Optional[RectWidget] = None
        self.__targetLine: Optional[LineWidget] = None

    # Function for set first and second points for line
    def makeOrUpdateTargetLine(self, rect: RectWidget):
        if self.__targetLine is None:
            self.__targetRect = rect

            # Make new line
            self.__targetLine = LineWidget(rect.getCenterCoordinates())

            # Subscribe update line position when rect position updated
            self.__targetLine.appendLinkedRect(rect, 'start')

        elif self.__targetRect is not rect:
            self.__targetLine.setEndPosition(rect.getCenterCoordinates())

            # Subscribe update line position when rect position updated
            self.__targetLine.appendLinkedRect(rect, 'end')

            # Append rect to list for render
            self.lines.append(self.__targetLine)

            self.__targetRect = None
            self.__targetLine = None

    # Delete line
    def unlinkLine(self, line: LineWidget):
        line.unlink()
        self.lines.remove(line)
        pass

    # Find line by position
    def findLineByPosition(self, position: QPoint) -> Optional[LineWidget]:
        for line in self.lines:
            if self.__detectPointOnLine(line, position):
                return line
        return None

    def __detectPointOnLine(self, line: LineWidget, position: QPoint) -> bool:
        shadow = 5

        start = line.start
        end = line.end

        v1x = end.x() - start.x()
        v1y = end.y() - start.y()
        v2x = position.x() - start.x()
        v2y = position.y() - start.y()

        u = (v2x * v1x + v2y * v1y) / (v1y * v1y + v1x * v1x)

        if 0 <= u <= 1:
            dist = (start.x() + v1x * u - position.x()) ** 2 + (start.y() + v1y * u - position.y()) ** 2
        else:
            if u < 0:
                dist = (start.x() - position.x()) ** 2 + (start.y() - position.y()) ** 2
            else:
                dist = (end.x() - position.x()) ** 2 + (end.y() - position.y()) ** 2

        return dist <= shadow


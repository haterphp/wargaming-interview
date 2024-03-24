from app.common.interfaces.models import ILineModel
from app.common.interfaces.window import IAppWindow

from widgets.line.widget import LineWidget
from widgets.rectangle.widget import RectWidget

class LineModel(ILineModel):
    def __init__(self, window: IAppWindow):
        super().__init__(window)

        self.__targetRect: RectWidget | None = None
        self.__targetLine: LineWidget | None = None

    def makeOrUpdateTargetLine(self, rect: RectWidget):
        if self.__targetLine is None:
            self.__targetRect = rect

            self.__targetLine = LineWidget(rect.getCenterCoordinates())

            # Subscribe update line position when rect position updated
            rect.subscribeToUpdates(self.__targetLine.setStartPosition)

        elif self.__targetRect is not rect:
            self.__targetLine.setEndPosition(rect.getCenterCoordinates())

            # Subscribe update line position when rect position updated
            rect.subscribeToUpdates(self.__targetLine.setEndPosition)

            self.lines.append(self.__targetLine)

            self.__targetRect = None
            self.__targetLine = None


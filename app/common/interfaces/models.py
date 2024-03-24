from typing import List, Optional

from PySide6.QtCore import QPoint

from widgets.rectangle.widget import RectWidget
from widgets.line.widget import LineWidget

from app.common.interfaces.window import IAppWindow
from app.common.enums.mode import AppModeEnum


class IRectangleModel:
    def __init__(self, window: IAppWindow):
        self.window = window

        # Define list for our RectWidgets
        self.rectangles: List[RectWidget] = []

    def makeANewRectangle(self, point: QPoint):
        pass

    def findAndSetDraggedElement(self, point: QPoint) -> bool:
        return False

    def findRectByPosition(self, point: QPoint) -> Optional[RectWidget]:
        return None

    def moveDraggedRectByPoint(self, point: QPoint):
        pass

    def resetDraggedElement(self):
        pass


class ILineModel:
    def __init__(self, window: IAppWindow):
        self.window = window

        # Define list for our LineWidgets
        self.lines: List[LineWidget] = []

    def makeOrUpdateTargetLine(self, rect: RectWidget):
        pass

    def unlinkLine(self, line: LineWidget):
        pass

    def findLineByPosition(self, position: QPoint) -> Optional[LineWidget]:
        pass


class IAppModel:
    def __init__(self,
                 window: IAppWindow,
                 rectangleModel: IRectangleModel,
                 lineModel: ILineModel,
                 ):
        self.window = window

        self.rectangleModel = rectangleModel
        self.lineModel = lineModel

        self.mode = AppModeEnum.DEFAULT

    def toggleMode(self, mode: AppModeEnum):
        self.mode = mode

    def clear(self):
        self.mode = AppModeEnum.DEFAULT

        self.rectangleModel.rectangles = []
        self.lineModel.lines = []

        self.window.update()

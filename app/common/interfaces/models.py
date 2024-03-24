from typing import List

from PySide6.QtCore import QPoint

from widgets.rectangle.widget import RectWidget

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

    def findRectByPosition(self, point: QPoint) -> (RectWidget | None):
        return None

    def moveDraggedRectByPoint(self, point: QPoint):
        pass

    def resetDraggedElement(self):
        pass


class ILineModel:
    def __init__(self, window: IAppWindow):
        self.window = window

        # Define list for our LineWidgets
        self.lines: List = []

    def makeOrUpdateTargetLine(self, rect: RectWidget):
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

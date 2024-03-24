from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

from app.common.interfaces.models import ILineModel, IRectangleModel
from app.common.interfaces.events import IModelEvent


class LineMouseEventsHandler(IModelEvent):
    def __init__(self, lineModel: ILineModel, rectModel: IRectangleModel):
        self.__lineModel = lineModel
        self.__rectModel = rectModel

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            rect = self.__rectModel.findRectByPosition(event.pos())
            if rect is not None:
                self.__lineModel.makeOrUpdateTargetLine(rect)
                self.__lineModel.window.update()

        if event.button() == Qt.RightButton:
            line = self.__lineModel.findLineByPosition(event.pos())
            if line is not None:
                self.__lineModel.unlinkLine(line)
                self.__lineModel.window.update()



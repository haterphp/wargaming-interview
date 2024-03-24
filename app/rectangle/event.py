from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

from app.common.interfaces.models import IRectangleModel
from app.common.interfaces.events import IModelEvent


class RectangleMouseEventsHandler(IModelEvent):
    def __init__(self, model: IRectangleModel):
        self.__model = model

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.__model.makeANewRectangle(event.pos())
            self.__model.window.update()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            isFind = self.__model.findAndSetDraggedElement(event.pos())
            if isFind is True:
                self.__model.window.setCursor(Qt.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        self.__model.moveDraggedRectByPoint(event.pos())
        self.__model.window.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__model.resetDraggedElement()
            self.__model.window.setCursor(Qt.ArrowCursor)

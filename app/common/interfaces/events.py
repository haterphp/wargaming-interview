from PySide6.QtGui import QMouseEvent


class IModelEvent:
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        pass

    def mousePressEvent(self, event: QMouseEvent):
       pass

    def mouseMoveEvent(self, event: QMouseEvent):
        pass

    def mouseReleaseEvent(self, event: QMouseEvent):
        pass
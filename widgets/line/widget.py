from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import QPoint, QLine

from widgets.common.widget import IProjectWidget

from settings import LINE_SIZE, LINE_COLOR


class LineWidget(IProjectWidget):
    def __init__(self, start: QPoint):
        super().__init__()

        self.start: QPoint = start
        self.end: QPoint | None = None

    def setStartPosition(self, start: QPoint):
        self.start = start

    def setEndPosition(self, end: QPoint):
        self.end = end

    def draw(self, painter: QPainter):
        if self.end is not None:
            line = QLine(self.start, self.end)

            painter.setPen(QPen(LINE_COLOR, LINE_SIZE))
            painter.drawLine(line)

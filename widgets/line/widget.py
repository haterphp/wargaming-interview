from typing import Optional

from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import QPoint, QLine

from widgets.common.widget import IProjectWidget
from widgets.rectangle.widget import RectWidget

from settings import LINE_SIZE, LINE_COLOR


class LineWidget(IProjectWidget):
    def __init__(self, start: QPoint):
        super().__init__()

        # Define line positions
        self.start: QPoint = start
        self.end: Optional[QPoint] = None

        # Define linked rectangles
        self.startRect: Optional[RectWidget] = None
        self.endRect: Optional[RectWidget] = None

    # Set positions
    def setStartPosition(self, start: QPoint):
        self.start = start

    def setEndPosition(self, end: QPoint):
        self.end = end

    # Add link to rectangles
    def appendLinkedRect(self, rect: RectWidget, position: str):
        # Subscribe to updates from start position rect
        if position == 'start':
            self.startRect = rect
            self.startRect.subscribeToUpdates(self.setStartPosition)

        # Subscribe to updates from end position rect
        elif position == 'end':
            self.endRect = rect
            self.endRect.subscribeToUpdates(self.setEndPosition)

    # Remove line callback
    def unlink(self):
        if self.startRect is not None:
            self.startRect.unsubscribeFromUpdates(self.setStartPosition)
        if self.endRect is not None:
            self.endRect.unsubscribeFromUpdates(self.setEndPosition)

    def draw(self, painter: QPainter):
        if self.end is not None:
            line = QLine(self.start, self.end)

            painter.setPen(QPen(LINE_COLOR, LINE_SIZE))
            painter.drawLine(line)

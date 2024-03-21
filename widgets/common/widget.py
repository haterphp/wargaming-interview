from PySide6.QtGui import QPainter


class IProjectWidget:
    # Abstract method for draw our element
    def draw(self, painter: QPainter):
        pass

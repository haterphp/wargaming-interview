from PySide6.QtGui import QColor

# This file need for make project constants and etc

# Window settings
WINDOW_TITLE = "Wargaming Interview Project"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_MENU_HEIGHT = 20

# Rectangle sizes (aspect ratio for rectangle is 2:1)
RECTANGLE_SIZE = 50
RECTANGLE_WIDTH = RECTANGLE_SIZE * 2
RECTANGLE_HEIGHT = RECTANGLE_SIZE

RECTANGLE_HALF_WIDTH = RECTANGLE_WIDTH / 2
RECTANGLE_HALF_HEIGHT = RECTANGLE_HEIGHT / 2

# Rectangle color available for creation in RectWidget
RECTANGLE_COLORS = (
    QColor("#464D77"),
    QColor("#36827F"),
    QColor("#F9DB6D"),
    QColor("#877666"),
)

# Line settings
LINE_SIZE = 5
LINE_COLOR = QColor("#000000")

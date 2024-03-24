from PySide6.QtGui import QAction, QIcon

from app.common.enums.mode import AppModeEnum

from app.common.interfaces.window import IAppWindow
from app.common.interfaces.models import IAppModel


class AppMenuWidget:
    def __init__(self, window: IAppWindow, model: IAppModel):
        modeMenu = window.menuBar().addMenu("Mode")

        self.__model = model

        self.defaultEditorMode = QAction(QIcon('assets/check.png'), "Default", window)
        self.defaultEditorMode.setShortcut("Ctrl+D")
        self.defaultEditorMode.triggered.connect(self.setDefaultModeAction)

        self.lineEditorMode = QAction(QIcon('assets/check.png'), "Line", window)
        self.lineEditorMode.setShortcut("Ctrl+F")
        self.lineEditorMode.setIconVisibleInMenu(False)
        self.lineEditorMode.triggered.connect(self.setLineModeAction)

        modeMenu.addAction(self.defaultEditorMode)
        modeMenu.addAction(self.lineEditorMode)

    # Callback for changing mode to default
    def setDefaultModeAction(self):
        self.defaultEditorMode.setIconVisibleInMenu(True)
        self.lineEditorMode.setIconVisibleInMenu(False)

        self.__model.toggleMode(AppModeEnum.DEFAULT)

    # Callback for changing mode to line
    def setLineModeAction(self):
        self.defaultEditorMode.setIconVisibleInMenu(False)
        self.lineEditorMode.setIconVisibleInMenu(True)

        self.__model.toggleMode(AppModeEnum.LINE)

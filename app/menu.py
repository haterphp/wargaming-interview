from PySide6.QtGui import QAction, QIcon

from app.common.enums.mode import AppModeEnum

from app.common.interfaces.window import IAppWindow
from app.common.interfaces.models import IAppModel


class AppMenuWidget:
    def __init__(self, window: IAppWindow, model: IAppModel):
        fileMenu = window.menuBar().addMenu("File")
        modeMenu = window.menuBar().addMenu("Mode")

        self.__model = model

        # Make toggle to default editor mode action
        self.defaultEditorModeAction = QAction(QIcon('assets/check.png'), "Default", window)
        self.defaultEditorModeAction.setShortcut("Ctrl+D")
        self.defaultEditorModeAction.triggered.connect(self.setDefaultModeAction)

        # Make toggle to line editor mode action
        self.lineEditorModeAction = QAction(QIcon('assets/check.png'), "Line", window)
        self.lineEditorModeAction.setShortcut("Ctrl+F")
        self.lineEditorModeAction.setIconVisibleInMenu(False)
        self.lineEditorModeAction.triggered.connect(self.setLineModeAction)

        # Make clear scene action
        self.clearAction = QAction("Clear Scene", window)
        self.clearAction.setShortcut("Ctrl+C")
        self.clearAction.triggered.connect(self.__model.clear)

        # Append actions for menu bars
        modeMenu.addAction(self.defaultEditorModeAction)
        modeMenu.addAction(self.lineEditorModeAction)

        fileMenu.addAction(self.clearAction)

    # Callback for changing mode to default
    def setDefaultModeAction(self):
        self.defaultEditorModeAction.setIconVisibleInMenu(True)
        self.lineEditorModeAction.setIconVisibleInMenu(False)

        self.__model.toggleMode(AppModeEnum.DEFAULT)

    # Callback for changing mode to line
    def setLineModeAction(self):
        self.defaultEditorModeAction.setIconVisibleInMenu(False)
        self.lineEditorModeAction.setIconVisibleInMenu(True)

        self.__model.toggleMode(AppModeEnum.LINE)

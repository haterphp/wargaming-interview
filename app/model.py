from app.common.enums.mode import AppModeEnum

from app.common.interfaces.models import IAppModel
from app.common.interfaces.window import IAppWindow
from app.common.interfaces.events import IModelEvent

from app.rectangle.event import RectangleMouseEventsHandler
from app.rectangle.model import RectangleModel

from app.line.event import LineMouseEventsHandler
from app.line.model import LineModel


class AppModel(IAppModel):
    def __init__(self, window: IAppWindow):
        super().__init__(
            window,
            RectangleModel(window),
            LineModel(window)
        )

        self.eventsHandler: IModelEvent = RectangleMouseEventsHandler(self.rectangleModel)

    def toggleMode(self, mode: AppModeEnum):
        super().toggleMode(mode)

        if self.mode == AppModeEnum.DEFAULT:
            self.eventsHandler = RectangleMouseEventsHandler(self.rectangleModel)

        if self.mode == AppModeEnum.LINE:
            self.eventsHandler = LineMouseEventsHandler(self.lineModel, self.rectangleModel)
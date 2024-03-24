from PySide6.QtGui import QPainter


class IProjectWidget:
    def __init__(self):
        self._subscribeCallbacks = []

    # Abstract method for draw our element
    def draw(self, painter: QPainter):
        pass

    def subscribeToUpdates(self, callback):
        if callback in self._subscribeCallbacks:
            self._subscribeCallbacks.remove(callback)
        self._subscribeCallbacks.append(callback)

    def unsubscribeFromUpdates(self, callback):
        if callback in self._subscribeCallbacks:
            self._subscribeCallbacks.remove(callback)

    def emitUpdates(self):
        for callback in self._subscribeCallbacks:
            callback()

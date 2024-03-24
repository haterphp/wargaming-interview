from PySide6.QtGui import QPainter


class IProjectWidget:
    def __init__(self):
        self._subscribeCallbacks = []

    # Abstract method for draw our element
    def draw(self, painter: QPainter):
        pass

    # Subscribe to element updates
    def subscribeToUpdates(self, callback):
        if callback in self._subscribeCallbacks:
            self._subscribeCallbacks.remove(callback)
        self._subscribeCallbacks.append(callback)

    # Unsubscribe from element updates
    def unsubscribeFromUpdates(self, callback):
        if callback in self._subscribeCallbacks:
            self._subscribeCallbacks.remove(callback)

    # Emit for subscribers about changes
    def emitUpdates(self):
        for callback in self._subscribeCallbacks:
            callback()

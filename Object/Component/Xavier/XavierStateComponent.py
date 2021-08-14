from Object.Component.StateComponent import *


class XavierStateComponent(StateComponent):
    def __init__(self) -> None:
        super().__init__()

    def onUpdate(self) -> None:
        super().onUpdate()

        self._state.voltage += 0.001
        self._state.cpu += 0.001
        self._state.memory += 0.001
        self._state.disk += 0.001

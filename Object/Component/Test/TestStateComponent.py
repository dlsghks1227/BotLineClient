from Object.Component.StateComponent import *
from Object.Component.Test.TestValueObject import *

class TestStateComponent(StateComponent):
    def __init__(self) -> None:
        super().__init__()
        self.state = TestStateValueObject()

    def onUpdate(self) -> None:
        super().onUpdate()

        self.state.voltage += 0.001
        self.state.cpu += 0.001
        self.state.memory += 0.001
        self.state.disk += 0.001
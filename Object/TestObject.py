from Object.Component.TestStateComponent import TestStateComponent
from Object.Component.TestNetworkComponent import TestNetworkComponent

from Object.BotLineObject import *
from Object.Component.NetworkComponent import *
from Object.Component.StateComponent import *

from Lib.Log import Log

class TestObject(BotLineObject):
    def __init__(self) -> None:
        super().__init__()
        self.networkComponent = TestNetworkComponent(ObjectType.Jetbot, SocketAddress("localhost", 8000))
        self.stateComponent = TestStateComponent()
        self.stateComponent.start()

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)
        self.networkComponent.onUpdate(elapsedTime)
        self.networkComponent.setStateValueObject(self.stateComponent.state)

    def onDestory(self) -> None:
        super().onDestory()
        self.stateComponent.isRunning = False
        self.stateComponent.join()
        self.networkComponent.onDestory()
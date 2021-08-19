from Network.SocketAddress import *

from Object.Component.Jetbot.JetbotValueObject import *

from Object.Component.Test.TestStateComponent import TestStateComponent
from Object.Component.Test.TestNetworkComponent import TestNetworkComponent

from Object.BotLineObject import *
from Object.Component.NetworkComponent import *
from Object.Component.StateComponent import *

from Lib.Log import Log

class TestObject(BotLineObject):
    def __init__(self, address: SocketAddress) -> None:
        super().__init__(address)
        self.networkComponent = TestNetworkComponent(ObjectType.TEST, self._address, JetbotPosition.BOTTOM)
        self.stateComponent = TestStateComponent()
        self.stateComponent.start()

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)
        self.networkComponent.onUpdate(elapsedTime)
        self.networkComponent.setState(self.stateComponent.state)

    def onDestory(self) -> None:
        super().onDestory()
        self.stateComponent.stop()
        self.stateComponent.join()
        self.networkComponent.onDestory()
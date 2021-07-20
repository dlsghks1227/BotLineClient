from Object.Component.Xavier.XavierStateComponent import XavierStateComponent
from Object.Component.Xavier.XavierNetworkComponent import XavierNetworkComponent

from Object.BotLineObject import *
from Object.Component.NetworkComponent import *
from Object.Component.StateComponent import *

from Lib.Log import Log

class XavierObject(BotLineObject):
    def __init__(self, address: SocketAddress) -> None:
        super().__init__(address)
        self.networkComponent = XavierNetworkComponent(ObjectType.XAVIER, self._address)
        self.stateComponent = XavierStateComponent()
        self.stateComponent.start()

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)
        self.networkComponent.onUpdate(elapsedTime)
        self.networkComponent.setObjectState(self.stateComponent.state)

    def onDestory(self) -> None:
        super().onDestory()
        self.stateComponent.isRunning = False
        self.stateComponent.join()
        self.networkComponent.onDestory()
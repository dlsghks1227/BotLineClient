from Object.Component.Jetbot.JetbotValueObject import JetbotPosition, JetbotPositionValueObject
from Object.Component.Jetbot.JetbotStateComponent import JetbotStateComponent
from Object.Component.Jetbot.JetbotNetworkComponent import JetbotNetworkComponent

from Object.BotLineObject import *
from Object.Component.NetworkComponent import *
from Object.Component.StateComponent import *

from jetbot import Robot

from Lib.Log import Log

class JetbotObject(BotLineObject):
    def __init__(self, address: SocketAddress, position: JetbotPosition = JetbotPosition.DEFAULT) -> None:
        super().__init__(address)
        self.stateComponent = JetbotStateComponent()
        self.stateComponent.start()

        self.networkComponent = JetbotNetworkComponent(ObjectType.JETBOT, self._address, position)

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)
        self.networkComponent.onUpdate(elapsedTime)
        self.networkComponent.setState(self.stateComponent.state)

        if not self.networkComponent.isConnected:
            self.networkComponent.isWorking = False
            self.networkComponent.isStop = False

    def onDestory(self) -> None:
        super().onDestory()
        self.stateComponent.stop()
        self.stateComponent.join()

        self.networkComponent.onDestory()
            
    def isStop(self) -> bool:
        return self.networkComponent.isStop
    
    def isWorking(self) -> bool:
        return self.networkComponent.isWorking
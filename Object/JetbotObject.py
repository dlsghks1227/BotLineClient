from Object.Component.TestStateComponent import TestStateComponent
from Object.Component.JetbotNetworkComponent import JetbotNetworkComponent

from Object.BotLineObject import *
from Object.Component.NetworkComponent import *
from Object.Component.StateComponent import *

from Lib.Log import Log

class JetbotObject(BotLineObject):
    def __init__(self) -> None:
        super().__init__()
        self.networkComponent = JetbotNetworkComponent(ObjectType.Jetbot, SocketAddress("localhost", 8000))


    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()
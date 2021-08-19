from Object.Component.Jetbot.JetbotValueObject import JetbotPositionValueObject
from Object.Component.Xavier.XavierNetworkComponent import XavierNetworkComponent

from Object.BotLineObject import *
from Object.Component.NetworkComponent import *
from Object.Component.StateComponent import *

from Lib.Log import Log

class XavierObject(BotLineObject):
    def __init__(self, address: SocketAddress) -> None:
        super().__init__(address)
        self.networkComponent = XavierNetworkComponent(ObjectType.XAVIER, self._address)

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)
        self.networkComponent.onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()
        self.networkComponent.onDestory()

    def setJetbotPositions(self, datas: list) -> None:
        jetbotDatas = list()
        for data in datas:
            pos = JetbotPositionValueObject()
            pos.x = data["pos"][0]
            pos.y = data["pos"][1]
            jetbotDatas.append(pos)
        self.networkComponent.jetbotPositions = jetbotDatas
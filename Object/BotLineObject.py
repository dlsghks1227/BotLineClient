from Network.SocketAddress import *

from Lib.Log import Log

class BotLineObject:
    def __init__(self, address: SocketAddress) -> None:
        self._address = address

    def onUpdate(self, elapsedTime: float) -> None:
        pass

    def onDestory(self) -> None:
        pass
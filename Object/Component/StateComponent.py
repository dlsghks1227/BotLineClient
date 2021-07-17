import threading
import time

from Network.PacketType import *

from Object.StateValueObject import *

class StateComponent(threading.Thread):
    def __init__(self) -> None:
        super().__init__()

        self.__isRunning = True
        self._state = StateValueObject()

    def onUpdate(self) -> None:
        pass

    def run(self) -> None:
        while self.__isRunning:
            self.onUpdate()
            time.sleep(0.5)

    @property
    def isRunning(self) -> bool:
        return self.__isRunning

    @isRunning.setter
    def isRunning(self, isRunning: bool) -> None:
        self.__isRunning = isRunning

    @property
    def state(self) -> StateValueObject:
        return self._state
import threading
import time

from Network.PacketType import *

class StateComponent(threading.Thread):
    def __init__(self) -> None:
        super().__init__()
        self.__isRunning = True

    def onUpdate(self) -> None:
        pass

    def run(self) -> None:
        while self.__isRunning:
            self.onUpdate()
            time.sleep(0.5)

    @property
    def isRunning(self) -> bool:
        return self.__isRunning

    def stop(self) -> None:
        self.__isRunning = False

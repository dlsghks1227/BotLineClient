from Network.SocketAddress import *
from Network.PacketType import *

from Object.BotLineObject import BotLineObject
#from Object.JetbotObject import JetbotObject
from Object.XavierObject import XavierObject
from Object.TestObject import TestObject

class BotLineFactory:
    def __init__(self, address: SocketAddress) -> None:
        self.__address = address

    def getBotLineObject(self, objectType: ObjectType) -> BotLineObject:
        if objectType is ObjectType.JETBOT:
            # return JetbotObject(self.__address)
            return TestObject(self.__address)
        elif objectType is ObjectType.XAVIER:
            return XavierObject(self.__address)
        else:
            return TestObject(self.__address)
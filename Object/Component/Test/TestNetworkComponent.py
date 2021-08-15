from Object.StateValueObject import StateValueObject
from Object.Component.NetworkComponent import *

from Network.PacketType import *

from Lib.Log import Log

class TestNetworkComponent(NetworkComponent):
    def __init__(self, objectType: ObjectType, hostAddress: SocketAddress) -> None:
        super().__init__(objectType, hostAddress)
        
        self.__state = StateValueObject()
        self._storage.add(MessageType.INFORMATION_REQUEST, self.informationRequest)
        self._storage.add(MessageType.ALL_STOP, self.allStop)

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()

    def setObjectState(self, state: StateValueObject) -> None:
        self.__state = state

    def informationRequest(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        outputPacket = OutputPacket(self._objectType)

        outputPacket.writeCommand(MessageType.INFORMATION_REQUEST)
        outputPacket.writeFloat(self.__state.voltage)
        outputPacket.writeFloat(self.__state.cpu)
        outputPacket.writeFloat(self.__state.memory)
        outputPacket.writeFloat(self.__state.disk)

        return outputPacket

    def allStop(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        isStop = inputPacket.readUInt8()
        Log(f"{isStop}")
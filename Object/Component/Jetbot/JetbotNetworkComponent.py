from Object.StateValueObject import StateValueObject
from Object.Component.NetworkComponent import *

class JetbotNetworkComponent(NetworkComponent):
    def __init__(self, objectType: ObjectType, hostAddress: SocketAddress) -> None:
        super().__init__(objectType, hostAddress)
        
        self.__isStop = False

        self.__state = StateValueObject()
        self._store.add(MessageType.INFORMATION_REQUEST, self.informationRequest)
        self._store.add(MessageType.ALL_STOP, self.allStop)


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
        self.__isStop = bool(isStop)

    @property
    def isStop(self) -> bool:
        return self.__isStop
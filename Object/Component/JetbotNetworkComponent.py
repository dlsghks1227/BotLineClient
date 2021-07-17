from Object.StateValueObject import StateValueObject
from Object.Component.NetworkComponent import *

class JetbotNetworkComponent(NetworkComponent):
    def __init__(self, type: ObjectType, hostAddress: SocketAddress) -> None:
        super().__init__(type, hostAddress)
        
        self.__state = StateValueObject()
        self._store.add(MessageType.INFORMATION_REQUEST, self.informationRequest)

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()

    def setStateValueObject(self, state: StateValueObject) -> None:
        self.__state = state

    def informationRequest(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        outputPacket = OutputPacket(self.objectType)

        outputPacket.writeCommand(MessageType.INFORMATION_REQUEST)
        outputPacket.writeFloat(self.__state.voltage)
        outputPacket.writeFloat(self.__state.cpu)
        outputPacket.writeFloat(self.__state.memory)
        outputPacket.writeFloat(self.__state.disk)

        return outputPacket
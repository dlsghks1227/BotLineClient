from Object.Component.Jetbot.JetbotValueObject import *
from Object.Component.NetworkComponent import *

class JetbotNetworkComponent(NetworkComponent):
    def __init__(self, objectType: ObjectType, hostAddress: SocketAddress, position: JetbotPosition = JetbotPosition.DEFAULT) -> None:
        super().__init__(objectType, hostAddress)

        self.__isWorking = False
        self.__isStop = False

        self.position = position
    
        self.__state = JetbotStateValueObject()

        self._storage.add(MessageType.INFO_CURRENT_STATE, self.infoCurrentState)
        self._storage.add(MessageType.JETBOT_CONTROL, self.jetbotControl)
        self._storage.add(MessageType.JETBOT_ARRIVED, self.jetbotArrived)
        self._storage.add(MessageType.INFO_JETBOT_POSITION, self.jetbotControlAllStop)
        self._storage.add(MessageType.JETBOT_POSITION_ERROR, self.jetbotPositionError)


    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()

    def setState(self, state: JetbotStateValueObject) -> None:
        self.__state = state

    @property
    def isWorking(self) -> bool:
        return self.__isWorking

    @property
    def isStop(self) -> bool:
        return self.__isStop

    def infoCurrentState(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        outputPacket = OutputPacket(self._objectType)

        outputPacket.writeCommand(MessageType.INFO_CURRENT_STATE)
        outputPacket.writeFloat(self.__state.voltage)
        outputPacket.writeFloat(self.__state.cpu)
        outputPacket.writeFloat(self.__state.memory)
        outputPacket.writeFloat(self.__state.disk)

        outputPacket.writeUInt8(self.position.value)

        outputPacket.writeUInt8(int(self.isWorking))
        outputPacket.writeUInt8(int(self.isStop))

        return outputPacket

    def jetbotControlAllStop(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        isStop = inputPacket.readUInt8()
        self.__isStop = bool(isStop)

    def jetbotControl(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        pos = inputPacket.readUInt8()

        self.position = JetbotPosition(pos)
        self.isWorking = True

    def jetbotArrived(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        self.isWorking = False

    def jetbotPositionError(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        self.position = JetbotPosition.DEFAULT
        Log("jetbotPositionError")

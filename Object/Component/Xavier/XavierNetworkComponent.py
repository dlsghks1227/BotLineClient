from Object.Component.NetworkComponent import *

class XavierNetworkComponent(NetworkComponent):
    def __init__(self, objectType: ObjectType, hostAddress: SocketAddress) -> None:
        super().__init__(objectType, hostAddress)
        
        self.jetbotPositions = list()
        self._storage.add(MessageType.INFO_JETBOT_POSITION, self.infoJetbotPosition)

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()

    def infoJetbotPosition(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        if len(self.jetbotPositions) != 0:
            for data in self.jetbotPositions:
                outputPacket = OutputPacket(self._objectType)
                outputPacket.writeCommand(MessageType.INFO_JETBOT_POSITION)
                outputPacket.writeFloat(data.x)
                outputPacket.writeFloat(data.y)
                self._networkManager.sendTo(outputPacket, address)

        outputPacket = OutputPacket(self._objectType)
        outputPacket.writeCommand(MessageType.END_DATA)
        outputPacket.writeCommand(MessageType.INFO_JETBOT_POSITION)

        return outputPacket
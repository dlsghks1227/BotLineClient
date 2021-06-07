from SocketAddress import SocketAddress
from Packet import *

from StateUpdateThread import StateUpdateThread
from ObjectState import JetbotObjectState as ObjectState

from BotLine import BotLine

OBJECTTYPE = 1

class BotLineOfJetbot(BotLine):
    def __init__(self, ip: str, port:int):
        super().__init__(OBJECTTYPE, ip, port)

        self.objectState = ObjectState()
        self.stateThread = StateUpdateThread()
        self.stateThread.start()

    def onUpdate(self, elapsedTime):
        super().onUpdate(elapsedTime)

        self.objectState.update(self.stateThread.getState())

    def onDestory(self):
        self.stateThread.setIsRunning(False)
        self.stateThread.join()
        super().onDestory()

    def processPacket(self, inputPacket: InputPacket, address: SocketAddress):
        super().processPacket(inputPacket, address)

        command = inputPacket.readCommand()

        if command == MessageType.CONNECT:
            self.isConnected = True
            objectHash = inputPacket.readUInt64()
            self.objectState.hash = objectHash
            print("Connected success: ", objectHash)
        elif command == MessageType.DISCONNECT:
            self.disconnect()
        elif command == MessageType.INFORMATION_REQUEST:
            packet = OutputPacket(OBJECTTYPE)

            packet.writeCommand(MessageType.INFORMATION_REQUEST)
            packet.writeFloat(self.objectState.voltage)
            packet.writeFloat(self.objectState.cpu)
            packet.writeFloat(self.objectState.memory)
            packet.writeFloat(self.objectState.disk)
            
            self.networkManager.sendTo(packet, address)
        elif command == MessageType.CONTROL:
            pass
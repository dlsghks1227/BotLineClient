from SocketAddress import SocketAddress
from Packet import *

from StateUpdateThread import StateUpdateThread
from ObjectState import XavierObjectState as ObjectState

from BotLine import BotLine

OBJECTTYPE = 3

class BotLineOfXavier(BotLine):
    def __init__(self, ip: str, port:int):
        super().__init__(ip, port)

        self.objectState = ObjectState()
        self.stateThread = StateUpdateThread()
        self.stateThread.start()

        self.wasSent = True
        self.findStopSign = 0

    def onUpdate(self, elapsedTime):
        super().onUpdate(elapsedTime)

        self.objectState.update(self.stateThread.getState())

        if self.findStopSign != self.objectState.isAllStop:
            self.findStopSign = self.objectState.isAllStop
            self.wasSent = False

        if not self.wasSent:
            packet = OutputPacket(OBJECTTYPE)
            packet.writeCommand(MessageType.ALL_STOP)
            packet.writeUInt8(self.objectState.isAllStop)
            self.networkManager.sendTo(packet, SocketAddress(self.host, self.port))
            self.wasSent = True

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
            pass
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
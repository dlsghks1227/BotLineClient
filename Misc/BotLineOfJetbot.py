from SocketAddress import SocketAddress
from Packet import *

from StateUpdateThread import StateUpdateThread
from ObjectState import JetbotObjectState as ObjectState

from BotLine import BotLine
from jetbot import Robot

OBJECTTYPE = 1

class BotLineOfJetbot(BotLine):
    def __init__(self, ip: str, port:int):
        super().__init__(OBJECTTYPE, ip, port)

        self.objectState = ObjectState()
        self.stateThread = StateUpdateThread(OBJECTTYPE)
        self.stateThread.start()

        self.robot = None
    
    def setJetbot(self, robot: Robot):
        self.robot = robot

    def onUpdate(self, elapsedTime):
        super().onUpdate(elapsedTime)

        self.objectState.update(self.stateThread.getState())

        if not self.isConnected or self.objectState.isStop:
            self.objectState.speed = 0

        if self.objectState.isStop:
            print("All Stop")

        if self.robot is not None:
            self.onControl()

    def onDestory(self):
        self.stateThread.setIsRunning(False)
        self.stateThread.join()
        super().onDestory()

    def onControl(self):
        speed = self.objectState.speed * 0.5
        leftWheel = (self.objectState.leftWheelValue * 0.1) * speed
        rightWheel = (self.objectState.rightWheelValue * 0.1) * speed
        self.robot.set_motors(leftWheel, rightWheel)

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
        elif command == MessageType.ALL_STOP:
            isStop = inputPacket.readUInt8()
            self.objectState.isStop = (isStop == 1)
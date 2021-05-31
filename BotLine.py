import socket
from Packet import *
from queue import Queue

from SocketAddress import SocketAddress
from NetworkManager import NetworkManager
from Packet import *

# from ina219 import *


HOST = '14.44.60.68'
PORT = 8000

# class JetbotInformation:
#     def __init__(self):
#         self.ina219 = INA219(addr=0x41)
#         self.voltage = 0.0

#     def updateInformation(self):
#         self.voltage = self.ina219.getBusVoltage_V()

#     def getVoltage(self):
#         return self.voltage

class JetbotInformation:
    def __init__(self):
        self.voltage = 10.0

    def updateInformation(self):
        self.voltage = 10.0

    def getVoltage(self):
        return self.voltage

class BotLine:
    packetQueue = Queue()
    information = JetbotInformation()

    def __init__(self, ip: str, port:int):
        self.networkManager = NetworkManager(SocketAddress(ip, port))
        self.connecting()
    
    def connecting(self):
        packet = OutputPacket()
        packet.writeCommand(MessageType.CONNECT)
        self.networkManager.sendTo(packet, SocketAddress(HOST, PORT))

    def onUpdate(self):
        # 패킷 처리
        self.information.updateInformation()
        self.processIncomingPackets()
    
    def onDestory(self):
        del self.networkManager

    def processIncomingPackets(self):
        self.readIncomingPacketsIntoQueue()
        self.processQueuedPackets()
    
    def readIncomingPacketsIntoQueue(self):
        data = self.networkManager.receiveFrom()
        if data is not None:
            self.packetQueue.put(data)

    def processQueuedPackets(self):
        while not self.packetQueue.empty():
            packet, address = self.packetQueue.get()

            # Process Packet ...
            self.processPacket(InputPacket(packet), SocketAddress(address[0], address[1]))

    def processPacket(self, inputPacket: InputPacket, address: SocketAddress):
        command = inputPacket.readCommand()
        if command == MessageType.INFORMATION_REQUEST:
            packet = OutputPacket()
            packet.writeCommand(MessageType.INFORMATION_REQUEST)
            packet.writeFloat(self.information.getVoltage())
            self.networkManager.sendTo(packet, address)

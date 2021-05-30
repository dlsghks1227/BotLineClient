import socket
from Packet import *
from queue import Queue

from SocketAddress import SocketAddress
from NetworkManager import NetworkManager
from Packet import *


HOST = '127.0.0.1'
PORT = 8000

class MyInformation:
    def __init__(self):
        pass
class BotLine:
    packetQueue = Queue()

    def __init__(self, ip: str, port:int):
        self.networkManager = NetworkManager(SocketAddress(ip, port))
        self.connecting()
    
    def connecting(self):
        packet = OutputPacket()
        packet.writeCommand(MessageType.JETBOT_CONNECT)
        self.networkManager.sendTo(packet, SocketAddress(HOST, PORT))

    def onUpdate(self):
        # 패킷 처리
        self.getMyInformation()
        self.processIncomingPackets()
    
    def onDestory(self):
        del self.networkManager

    def getMyInformation(self):
        pass

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
        if command == MessageType.JETBOT_INFORMATION_REQUEST:
            data = inputPacket.read('H', 4)
            print(data)
            packet = OutputPacket()
            packet.writeCommand(MessageType.JETBOT_INFORMATION_REQUEST)
            packet.writeInformation(10)
            self.networkManager.sendTo(packet, address)
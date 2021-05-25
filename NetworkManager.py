from UdpSocket import UdpSocket
from SocketAddress import SocketAddress
from Packet import Packet
from queue import Queue


class NetworkManager:
    def __init__(self, bindAddress: SocketAddress):
        self.socket = UdpSocket()
        self.socket.bind(bindAddress)
        self.socket.setBlocking(False)
        self.packetQueue = Queue()

    def __del__(self):
        del self.socket

    def processIncomingPackets(self):
        self.readIncomingPacketsIntoQueue()
        self.processQueuedPackets()

    def readIncomingPacketsIntoQueue(self):
        data = self.socket.receiveFrom()
        if data != None:
            self.packetQueue.put(data)

    def processQueuedPackets(self):
        while self.packetQueue.empty() == False:
            packet, address = self.packetQueue.get()

            # Process Packet ...

    def processPacket(self, packet: Packet, address: SocketAddress):
        pass
import socket

from SocketAddress import SocketAddress
from Packet import *
from queue import Queue


class NetworkManager:
    isConnected = False
    packetQueue = Queue()
    def __init__(self, bindAddress: SocketAddress, bufferSize: int=2048):
        self.bufferSize = bufferSize

        self.createSocket(bindAddress)

    def __del__(self):
        del self.udpSocket

    def getIsConnected(self):
        return self.isConnected

    def createSocket(self, bindAddress: SocketAddress):
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpSocket.bind(bindAddress.getAddressAndPort())
        self.udpSocket.setblocking(False)

    def sendTo(self, packet: OutputPacket, address: SocketAddress):
        byteSend = self.udpSocket.sendto(packet.getData(), address.getAddressAndPort())

    def receiveFrom(self):
        try:
            data, address = self.udpSocket.recvfrom(self.bufferSize)
            if len(data) >= 0:
                return data, address
        except BlockingIOError:
            return None

    def processIncomingPackets(self):
        self.readIncomingPacketsIntoQueue()
        self.processQueuedPackets()

    def readIncomingPacketsIntoQueue(self):
        data = self.receiveFrom()
        if data != None:
            self.packetQueue.put(data)

    def processQueuedPackets(self):
        while self.packetQueue.empty() == False:
            packet, address = self.packetQueue.get()

            # Process Packet ...
            self.processPacket(InputPacket(packet), SocketAddress(address[0], address[1]))

    def processPacket(self, inputPacket: InputPacket, address: SocketAddress):
        command = inputPacket.readCommand()
        if command == COMMAND.JETBOT_CONNECT:
            self.isConnected = True
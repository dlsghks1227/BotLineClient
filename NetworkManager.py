import socket

from SocketAddress import SocketAddress
from Packet import *
from queue import Queue


class NetworkManager:
    def __init__(self, objectType: int, address: SocketAddress, bufferSize: int = 2048):
        self.bufferSize = bufferSize

        self.objectType = objectType

        self.host = address.ip
        self.port = address.port

        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpSocket.setblocking(False)

    def __del__(self):
        del self.udpSocket

    def sendTo(self, packet: OutputPacket, address: SocketAddress):
        byteSend = self.udpSocket.sendto(packet.getData(), address.getAddressAndPort())

    def receiveFrom(self):
        try:
            data, address = self.udpSocket.recvfrom(self.bufferSize)
            if len(data) >= 0:
                return data, address
        except ConnectionResetError:
            return -1
        except BlockingIOError:
            return None

    def connecting(self):
        packet = OutputPacket(self.objectType)
        packet.writeCommand(MessageType.CONNECT)
        self.sendTo(packet, SocketAddress(self.host, self.port))
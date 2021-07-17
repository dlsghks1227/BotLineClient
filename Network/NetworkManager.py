import socket

from Network.SocketAddress import SocketAddress
from Network.Packet import *
from queue import Queue


class NetworkManager:
    def __init__(self, address: SocketAddress, bufferSize: int = 2048) -> None:
        self.__bufferSize = bufferSize

        self.__udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__udpSocket.setblocking(False)

    def __del__(self) -> None:
        self.__udpSocket.close()

    def sendTo(self, packet: OutputPacket, address: SocketAddress) -> None:
        self.__udpSocket.sendto(packet.getData(), address.getAddressAndPort())

    def receiveFrom(self) -> tuple or int or None:
        try:
            data, address = self.__udpSocket.recvfrom(self.__bufferSize)
            if len(data) >= 0:
                return data, address
        except ConnectionResetError:
            return -1
        except BlockingIOError:
            return None

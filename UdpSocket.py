import socket
from SocketAddress import SocketAddress


class UdpSocket:
    def __init__(self, bufferSize=2048):
        self.bufferSize = bufferSize
        self.udpSocket = udpSocket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM)

    def __del__(self):
        self.udpSocket.close()

    def bind(self, bindAddress: SocketAddress):
        self.udpSocket.bind(bindAddress.getAddressAndPort())

    def setBlocking(self, flag):
        self.udpSocket.setblocking(flag)

    def sendTo(self, data: bytes, address: SocketAddress):
        byteSend = self.udpSocket.send(data, address.getAddressAndPort())
        if byteSend >= 0:
            return byteSend
        else:
            print("sendTo() failed")
            return None

    def receiveFrom(self):
        try:
            data, address = self.udpSocket.recvfrom(self.bufferSize)
            if data >= 0:
                return data, address
            else:
                return None
        except BlockingIOError as e:
            return None

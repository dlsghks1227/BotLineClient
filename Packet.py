import struct


class MessageType:
    JETBOT_CONNECT = 0
    JETBOT_DISCONNECT = 1

    CONTROL_CONNECT = 2
    CONTROL_DISCONNECT = 3

    CONNECT_CHECK = 4

class Packet:
    data = bytearray(0)

    def getData(self):
        return self.data

class OutputPacket(Packet):
    def __init__(self):
        self.packetHead = 0

    def writeCommand(self, type: MessageType):
        self.data = bytearray(2)
        self.packetHead += 2
        struct.pack_into('>B', self.data, 0, type)

    def write(self, data, size):
        pass


class InputPacket(Packet):
    def __init__(self, data: bytes):
        self.data = data
        self.packetHead = 0

    def readCommand(self):
        self.packetHead += 2
        return struct.unpack_from('>B', self.data, 0)[0]
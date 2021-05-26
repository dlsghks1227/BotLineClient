import struct


class COMMAND:
    DEFAULT = 0
    JETBOT_CONNECT = 1
    JETBOT_DISCONNECT = 2

class Packet:
    data = bytearray(0)

    def getData(self):
        return self.data

class OutputPacket(Packet):
    def __init__(self):
        self.packetHead = 0

    def writeCommand(self, command: COMMAND):
        self.data = self.data + bytearray(2)
        self.packetHead += 2
        struct.pack_into('>B', self.data, 0, command)

    def write(self, data, size):
        pass


class InputPacket(Packet):
    def __init__(self, data: bytes):
        self.data = data
        self.packetHead = 0

    def readCommand(self):
        self.packetHead += 2
        return struct.unpack_from('>B', self.data, 0)[0]
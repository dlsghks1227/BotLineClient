import struct

OBJECTTYPE = 1

class MessageType:
    CONNECT = 0x00
    DISCONNECT = 0x01

    INFORMATION_REQUEST = 0x02
    CONTROL = 0x03

    CONNECT_CHECK = 0x04

    MASTER_STOP = 0x05

    DEFAULT = 0xFF

class MoveState:
    GO = 0x00
    STOP = 0x01

class Packet:
    data = bytearray(0)
    packetHead = 0

    def getData(self):
        return self.data

class OutputPacket(Packet):
    def __init__(self):
        self.data = bytearray(1)
        self.packetHead = 1
        struct.pack_into('<B', self.data, 0, OBJECTTYPE)

    def writeCommand(self, messageType: MessageType):
        self.writeUInt8(messageType)

    def write(self, data, dataType: str, size: int):
        self.data = self.data + bytearray(size)
        struct.pack_into('<' + dataType, self.data, self.packetHead, data)
        self.packetHead += size

    def writeUInt8(self, data: int):
        self.write(data, 'B', 1)

    def writeUInt16(self, data: int):
        self.write(data, 'H', 2)
    
    def writeUInt32(self, data: int):
        self.write(data, 'I', 4)

    def writeUInt64(self, data: int):
        self.write(data, 'Q', 8)

    def writeFloat(self, data: float):
        self.write(data, 'f', 4)
    
    def writeDouble(self, data: float):
        self.write(data, 'd', 8)


class InputPacket(Packet):
    def __init__(self, data: bytes):
        self.data = data
        self.packetHead = 0

    def readCommand(self):
        return self.readUInt8()

    def read(self, dataType: str, size: int):
        data = struct.unpack_from('<' + dataType, self.data, self.packetHead)[0]
        self.packetHead += size
        return data

    def readUInt8(self):
        return self.read('B', 1)
    
    def readUInt16(self):
        return self.read('H', 2)
    
    def readUInt32(self):
        return self.read('I', 4)

    def readUInt64(self):
        return self.read('Q', 8)

    def readFloat(self):
        return self.read('f', 4)
    
    def readDouble(self):
        return self.read('d', 8)
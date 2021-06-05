import struct

OBJECTTYPE_JETBOT = 1

class MessageType:
    CONNECT = 0
    DISCONNECT = 1

    INFORMATION_REQUEST = 2
    CONTROL = 3

    CONNECT_CHECK = 4

class Packet:
    data = bytearray(0)
    packetHead = 0

    def getData(self):
        return self.data

class OutputPacket(Packet):
    def __init__(self):
        self.data = bytearray(1)
        self.packetHead = 1
        struct.pack_into('<B', self.data, 0, OBJECTTYPE_JETBOT)

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
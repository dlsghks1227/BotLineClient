import struct


class MessageType:
    JETBOT_CONNECT = 0
    JETBOT_DISCONNECT = 1

    JETBOT_INFORMATION_REQUEST = 2

    CONTROL_CONNECT = 3
    CONTROL_DISCONNECT = 4

    CONTROLLER_JETOBT_INFORMATION_REQUEST = 5,

    CONNECT_CHECK = 6

class Packet:
    data = bytearray(0)

    def getData(self):
        return self.data

class OutputPacket(Packet):
    def __init__(self):
        self.packetHead = 0

    def writeCommand(self, messageType: MessageType):
        self.data = bytearray(2)
        self.packetHead = 1
        struct.pack_into('!B', self.data, 0, messageType)
    
    def writeInformation(self, voltage):
        self.write(voltage, 'H', 4)

    def write(self, data, dataType, size):
        self.data = self.data + bytearray(size)
        struct.pack_into('!' + dataType, self.data, self.packetHead, data)
        self.packetHead += (size - 1)


class InputPacket(Packet):
    def __init__(self, data: bytes):
        self.data = data
        self.packetHead = 0

    def readCommand(self):
        self.packetHead += 1
        return struct.unpack_from('>B', self.data, 0)[0]
    
    def read(self, dataType, size):
        data = struct.unpack_from('<' + dataType, self.data, self.packetHead)[0]
        self.packetHead += (size - 1)
        return data
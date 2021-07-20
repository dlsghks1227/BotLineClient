import struct

from Network.PacketType import *

class Packet:
    def __init__(self) -> None:
        self._data = bytearray(0)
        self._packetHead = 0

    @property
    def data(self) -> bytearray:
        return self._data

# ┌─────────────────────┬─────────────────┬───────────┐
# │ Object type (1byte) │ Command (1byte) │ Other ... │
# └─────────────────────┴─────────────────┴───────────┘

class OutputPacket(Packet):
    def __init__(self, objectType: ObjectType) -> None:
        self._data = bytearray(1)
        self._packetHead = 1
        struct.pack_into('<B', self._data, 0, objectType.value)

    def writeCommand(self, messageType: MessageType) -> None:
        self.writeUInt8(messageType.value)

    def write(self, data, dataType: str, size: int) -> None:
        self._data = self._data + bytearray(size)
        struct.pack_into('<' + dataType, self._data, self._packetHead, data)
        self._packetHead += size

    def writeUInt8(self, data: int) -> None:
        self.write(data, 'B', 1)

    def writeUInt16(self, data: int) -> None:
        self.write(data, 'H', 2)
    
    def writeUInt32(self, data: int) -> None:
        self.write(data, 'I', 4)

    def writeUInt64(self, data: int) -> None:
        self.write(data, 'Q', 8)

    def writeFloat(self, data: float) -> None:
        self.write(data, 'f', 4)
    
    def writeDouble(self, data: float) -> None:
        self.write(data, 'd', 8)


class InputPacket(Packet):
    def __init__(self, data: bytes) -> None:
        self._data = data
        self._packetHead = 0

    def readCommand(self) -> int:
        return self.readUInt8()

    def read(self, dataType: str, size: int):
        data = struct.unpack_from('<' + dataType, self._data, self._packetHead)[0]
        self._packetHead += size
        return data

    def readUInt8(self) -> int:
        return self.read('B', 1)
    
    def readUInt16(self) -> int:
        return self.read('H', 2)
    
    def readUInt32(self) -> int:
        return self.read('I', 4)

    def readUInt64(self) -> int:
        return self.read('Q', 8)

    def readFloat(self) -> float:
        return self.read('f', 4)
    
    def readDouble(self) -> float:
        return self.read('d', 8)
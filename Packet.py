import struct


class Packet:
    def __init__(self, data: bytes):
        self.data = data

    def readCommand(self):
        return struct.unpack_from('>H', self.data, 0)

    def setData(self, data: bytes):
        self.data = data

    def getData(self):
        return self.data
import struct
import time
from NetworkManager import NetworkManager
from SocketAddress import SocketAddress

# https://docs.python.org/ko/3/library/struct.html


if __name__ == "__main__":
    try:
        bindAddress = SocketAddress('0.0.0.0', 8001)
        network = NetworkManager(bindAddress)

        test = bytearray(10)
        print(test)
        struct.pack_into('>H', test, 0, 2)
        print(test)
        struct.pack_into('>H', test, 2, 2)
        print(test)

        data = struct.unpack_from('>H', test, 0)
        print(data)
        data = struct.unpack_from('>H', test, 2)
        print(data)

        while True:
            network.processIncomingPackets()

    except KeyboardInterrupt:
        del network
'''
data, address = udpSocket.recvfrom(BUFFER_SIZE)
# > : 빅 엔디안
# < : 리틀 엔디안
print("data : ", struct.unpack('>HL', data))
print("address : ", address)
'''
import struct
import time
from NetworkManager import NetworkManager
from SocketAddress import SocketAddress
from Packet import *

# https://docs.python.org/ko/3/library/struct.html

HOST = '127.0.0.1'
PORT = 8000


if __name__ == "__main__":
    try:
        bindAddress = SocketAddress('0.0.0.0', 8001)
        network = NetworkManager(bindAddress)

        while True:
            isConnected = network.getIsConnected()
            if isConnected == True:
                network.processIncomingPackets()
            else:
                packet = OutputPacket()
                serverAddress = SocketAddress(HOST, PORT)

                packet.writeCommand(COMMAND.JETBOT_CONNECT)
                network.sendTo(packet, serverAddress)

            time.sleep(0.001)

    except KeyboardInterrupt:
        del network
'''
data, address = udpSocket.recvfrom(BUFFER_SIZE)
# > : 빅 엔디안
# < : 리틀 엔디안
print("data : ", struct.unpack('>HL', data))
print("address : ", address)
'''
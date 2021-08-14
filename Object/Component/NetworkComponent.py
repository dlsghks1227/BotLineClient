from queue import Queue

from Network.PacketProcessingStore import PacketProcessingStore
from Network.Packet import InputPacket, OutputPacket
from Network.PacketType import *
from Network.SocketAddress import SocketAddress

from Network.NetworkManager import *

from Lib.Log import Log

class NetworkComponent:
    def __init__(self, objectType: ObjectType, hostAddress: SocketAddress) -> None:
        self._objectType = objectType
        self.__hostAddress = hostAddress

        self.__isConnected = False
        self.__timeout = 0.0
        self.__maxTimeout = 5.0

        self.__packetQueue = Queue()

        self._networkManager = NetworkManager(hostAddress)
        self.connecting()

        self._store = PacketProcessingStore()

        self._store.add(MessageType.CONNECT, self.connect)
        self._store.add(MessageType.DISCONNECT, self.disconnect)
        self._store.add(MessageType.CONNECT_CHECK, self.connectCheck)

    def onUpdate(self, elapsedTime: float) -> None:
        self.processIncomingPackets()
        self.connectionManagement()

        self.__timeout += elapsedTime

    def onDestory(self) -> None:
        self._networkManager.onDestory()

    def processIncomingPackets(self) -> None:
        self.readIncomingPacketIntoQueue()
        self.processQueuedPackets()

    def readIncomingPacketIntoQueue(self) -> None:
        data = self._networkManager.receiveFrom()

        if data[0] is not None:
            if data[0] == -1:
                self.__isConnected = False
                return
            self.__packetQueue.put(data)

    def processQueuedPackets(self) -> None:
        while not self.__packetQueue.empty():
            packet, address = self.__packetQueue.get()

            self.__timeout = 0.0
            self.processPacket(InputPacket(packet), SocketAddress(address[0], address[1]))
    
    def processPacket(self, inputPacket: InputPacket, address: SocketAddress) -> None:
        try:
            command = MessageType(inputPacket.readCommand())

            # 함수 실행
            outputPacket = self._store.run(command, inputPacket, address)

            if outputPacket is not None:
                self._networkManager.sendTo(outputPacket, address)
                return

        except ValueError:
            return

    def connectionManagement(self) -> None:
        if self.__timeout >= self.__maxTimeout:

            self.__isConnected = False
            self.__timeout = 0.0

            self.connecting()

    def connecting(self) -> None:
        outputPacket = OutputPacket(self._objectType)
        outputPacket.writeCommand(MessageType.CONNECT)
        self._networkManager.sendTo(outputPacket, self.__hostAddress)

        Log("Connecting...")

    @property
    def isConnected(self) -> bool:
        return self.__isConnected

    def connect(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        self.__isConnected = True
        self.__timeout = 0.0

        uniqueHash = inputPacket.readUInt64()

        Log(f"Connect(Hash: {uniqueHash})")

        return None
    
    def disconnect(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        self.__isConnected = False
        self.__timeout = 0.0

        Log("Disconnect")

        return None

    def connectCheck(self, inputPacket: InputPacket, address: SocketAddress) -> OutputPacket:
        outputPacket = OutputPacket(self._objectType)
        outputPacket.writeCommand(MessageType.CONNECT_CHECK)

        return outputPacket


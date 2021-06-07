from Packet import *
from queue import Queue

from SocketAddress import SocketAddress
from NetworkManager import NetworkManager
from Packet import *

#from JetbotInformation import StateUpdateThread, JetbotInformation

class BotLine:
    def __init__(self, objectType: int, ip: str, port:int):
        self.packetQueue = Queue()

        self.networkManager = NetworkManager(objectType, SocketAddress(ip, port))
        self.networkManager.connecting()
        
        self.host = ip
        self.port = port

        self.isConnected = False
        self.timeout = 0.0
        self.maxTimeout = 5.0
        self.connectingDelay = 3.0
    
    def disconnect(self):
        print("Disconnect")
        self.timeout = 0.0
        self.isConnected = False

    def onUpdate(self, elapsedTime):
        # 패킷 처리
        self.processIncomingPackets()
        self.connectionManagement()

        self.timeout += elapsedTime

        # if self.isConnected is False:
        #     self.information.setSpeed(0)
        #     self.information.controlJetbot()
        #     self.timeout += elapsedTime
        # else:
        #     self.information.controlJetbot()
        #     self.timeout += elapsedTime

    def onDestory(self):
        del self.networkManager

    def connectionManagement(self):
        if not self.isConnected:
            if self.timeout >= self.connectingDelay:
                print("re-send connect packet")
                # 재 연결 시도
                self.networkManager.connecting()
                self.timeout = 0.0
        else:
            if self.timeout >= self.maxTimeout:
                self.isConnected = False

                # 재 연결 시도
                self.networkManager.connecting()

                self.timeout = 0.0
                
    def processIncomingPackets(self):
        self.readIncomingPacketsIntoQueue()
        self.processQueuedPackets()
    
    def readIncomingPacketsIntoQueue(self):
        data = self.networkManager.receiveFrom()
        if data is not None:
            if data == -1:
                self.isConnected = False
                return
            self.packetQueue.put(data)

    def processQueuedPackets(self):
        while not self.packetQueue.empty():
            packet, address = self.packetQueue.get()

            # Process Packet ...
            self.processPacket(InputPacket(packet), SocketAddress(address[0], address[1]))

    def processPacket(self, inputPacket: InputPacket, address: SocketAddress):
        self.timeout = 0.0
            
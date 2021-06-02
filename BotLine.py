import socket
import time
import threading

from Packet import *
from queue import Queue

from SocketAddress import SocketAddress
from NetworkManager import NetworkManager
from Packet import *

from TestInformation import StateUpdateThread, JetbotInformation
#from JetbotInformation import StateUpdateThread, JetbotInformation

HOST = '127.0.0.1'
PORT = 8000

class BotLine:
    packetQueue = Queue()

    def __init__(self, ip: str, port:int):
        self.networkManager = NetworkManager(SocketAddress(ip, port))
        self.connecting()

        self.information = JetbotInformation()
        self.stateThread = StateUpdateThread()
        self.stateThread.start()

        self.isConnected = False
        self.timeout = 0.0
        self.maxTimeout = 5.0
        self.cycleTime = 0.0
        self.connectingDelay = 2.0
    
    def connecting(self):
        packet = OutputPacket()
        packet.writeCommand(MessageType.CONNECT)
        self.networkManager.sendTo(packet, SocketAddress(HOST, PORT))
    
    def disconnect(self):
        print("disconnect")
        self.isConnected = False
        self.connecting()

    def onUpdate(self, elapsedTime):
        # 패킷 처리
        self.information.updateInformation(self.stateThread.getState())
        self.processIncomingPackets()

        if self.isConnected is False:
            self.information.controlJetbot()
            self.cycleTime += elapsedTime
            if self.cycleTime >= self.connectingDelay:
                print("re-send connect packet")
                self.connecting()
                self.cycleTime = 0.0
        else:
            self.information.setWheelsValue(0, 0)
            self.information.controlJetbot()
            self.cycleTime = 0.0
            self.timeout += elapsedTime
            if self.timeout >= self.maxTimeout:
                self.isConnected = False
                self.connecting()
                self.timeout = 0.0

    def onDestory(self):
        self.stateThread.setIsRunning(False)
        self.stateThread.join()
        del self.networkManager

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
        command = inputPacket.readCommand()
        if command == MessageType.CONNECT:
            print("connected success")
            self.isConnected = True
        elif command == MessageType.DISCONNECT:
            self.disconnect()
        elif command == MessageType.INFORMATION_REQUEST:
            packet = OutputPacket()

            packet.writeCommand(MessageType.INFORMATION_REQUEST)
            packet.writeFloat(self.information.getVoltage())
            packet.writeFloat(self.information.getCPU())
            packet.writeFloat(self.information.getMemory())
            packet.writeFloat(self.information.getDisk())

            packet.writeUInt16(self.information.getLeftWheelValue())
            packet.writeUInt16(self.information.getRightWheelValue())
            packet.writeUInt16(self.information.getSpeed())
            
            self.networkManager.sendTo(packet, address)
        elif command == MessageType.CONTROL:
            pass
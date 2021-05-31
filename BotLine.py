import socket
from Packet import *
from queue import Queue

from SocketAddress import SocketAddress
from NetworkManager import NetworkManager
from Packet import *



HOST = '14.44.60.68'
PORT = 8000

'''
from ina219 import *
import subprocess
class JetbotInformation:
    def __init__(self):
        self.ina219 = INA219(addr=0x41)
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0

    def updateInformation(self):
        self.voltage = self.ina219.getBusVoltage_V()
        self.cpu = self.loadCPUAverage()
        self.memory = self.loadMemory()
        self.disk = self.loadDisk()

    def loadCPUAverage(self):
        cmd = "top -bn1 | grep load | awk '{\"%.2f\", $(NF-2)}'"
        return float(subprocess.check_output(cmd, shell=True))

    def loadMemory(self):
        cmd = "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'"
        return float(subprocess.check_output(cmd, shell=True))

    def loadDisk(self):
        cmd = "df -h | awk '$NF==\"/\"{printf \"%.2f\", $3 / $2 * 100}'"
        return float(subprocess.check_output(cmd, shell=True))

    def getVoltage(self):
        return self.voltage
    
    def getCPU(self):
        return self.cpu

    def getMemory(self):
        return self.memory

    def getDisk(self):
        return self.disk
'''

class JetbotInformation:
    def __init__(self):
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0

    def updateInformation(self):
        self.voltage = 10.01
        self.cpu = 15.02
        self.memory = 12.13
        self.disk = 51.15

    def getVoltage(self):
        return self.voltage
    
    def getCPU(self):
        return self.cpu

    def getMemory(self):
        return self.memory

    def getDisk(self):
        return self.disk

class BotLine:
    packetQueue = Queue()
    information = JetbotInformation()

    def __init__(self, ip: str, port:int):
        self.networkManager = NetworkManager(SocketAddress(ip, port))
        self.connecting()
    
    def connecting(self):
        packet = OutputPacket()
        packet.writeCommand(MessageType.CONNECT)
        self.networkManager.sendTo(packet, SocketAddress(HOST, PORT))

    def onUpdate(self):
        # 패킷 처리
        self.information.updateInformation()
        self.processIncomingPackets()
    
    def onDestory(self):
        del self.networkManager

    def processIncomingPackets(self):
        self.readIncomingPacketsIntoQueue()
        self.processQueuedPackets()
    
    def readIncomingPacketsIntoQueue(self):
        data = self.networkManager.receiveFrom()
        if data is not None:
            self.packetQueue.put(data)

    def processQueuedPackets(self):
        while not self.packetQueue.empty():
            packet, address = self.packetQueue.get()

            # Process Packet ...
            self.processPacket(InputPacket(packet), SocketAddress(address[0], address[1]))

    def processPacket(self, inputPacket: InputPacket, address: SocketAddress):
        command = inputPacket.readCommand()
        if command == MessageType.INFORMATION_REQUEST:
            packet = OutputPacket()
            packet.writeCommand(MessageType.INFORMATION_REQUEST)
            packet.writeFloat(self.information.getVoltage())
            packet.writeFloat(self.information.getCPU())
            packet.writeFloat(self.information.getMemory())
            packet.writeFloat(self.information.getDisk())
            self.networkManager.sendTo(packet, address)

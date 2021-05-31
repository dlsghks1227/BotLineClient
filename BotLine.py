import socket
import time
import threading

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

class StateUpdateThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.ina219 = INA219(addr=0x41)
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0
        self.isRunning = True
    
    def run(self):
        while self.isRunning is True:
            self.voltage = self.ina219.getBusVoltage_V()
            self.cpu = self.loadCPUAverage()
            self.memory = self.loadMemory()
            self.disk = self.loadDisk()
            time.sleep(0.5)

    def getState(self):
        return self.voltage, self.cpu, self.memory, self.disk

    def setIsRunning(self, isRunning):
        self.isRunning = isRunning

    def loadCPUAverage(self):
        cmd = "top -bn1 | grep load | awk '{\"%.2f\", $(NF-2)}'"
        return float(subprocess.check_output(cmd, shell=True))

    def loadMemory(self):
        cmd = "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'"
        return float(subprocess.check_output(cmd, shell=True))

    def loadDisk(self):
        cmd = "df -h | awk '$NF==\"/\"{printf \"%.2f\", $3 / $2 * 100}'"
        return float(subprocess.check_output(cmd, shell=True))

class JetbotInformation:
    def __init__(self):
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0

        self.leftWheelValue = 0
        self.rightWheelValue = 0
        self.speed = 0

    def updateInformation(self, state: tuple):
        self.voltage, self.cpu, self.memory, self.disk = state

    def getVoltage(self):
        return self.voltage
    
    def getCPU(self):
        return self.cpu

    def getMemory(self):
        return self.memory

    def getDisk(self):
        return self.disk

    def getLeftWheelValue(self):
        return self.leftWheelValue

    def setLeftWheelValue(self, value: int):
        self.leftWheelValue = value
    
    def getRightWheelValue(self):
        return self.rightWheelValue

    def setRightWheelValue(self, value: int):
        self.rightWheelValue = value

    def getWheelsValue(self):
        return self.leftWheelValue, self.rightWheelValue

    def setWheelsValue(self, leftValue: int, rightValue: int):
        self.leftWheelValue, self.rightWheelValue = leftValue, rightValue
    
    def getSpeed(self):
        return self.speed

    def setSpeed(self, value: int):
        self.speed = value

'''

class StateUpdateThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0
        self.isRunning = True
    
    def run(self):
        while self.isRunning is True:
            self.voltage += 0.1
            self.cpu += 0.1
            self.memory += 0.1
            self.disk += 0.1
            time.sleep(0.5)

    def getState(self):
        return self.voltage, self.cpu, self.memory, self.disk

    def setIsRunning(self, isRunning):
        self.isRunning = isRunning

class JetbotInformation:
    def __init__(self):
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0

        self.leftWheelValue = 0
        self.rightWheelValue = 0
        self.speed = 0

    def updateInformation(self, state: tuple):
        self.voltage, self.cpu, self.memory, self.disk = state

    def getVoltage(self):
        return self.voltage
    
    def getCPU(self):
        return self.cpu

    def getMemory(self):
        return self.memory

    def getDisk(self):
        return self.disk

    def getLeftWheelValue(self):
        return self.leftWheelValue

    def setLeftWheelValue(self, value: int):
        self.leftWheelValue = value
    
    def getRightWheelValue(self):
        return self.rightWheelValue

    def setRightWheelValue(self, value: int):
        self.rightWheelValue = value

    def getWheelsValue(self):
        return self.leftWheelValue, self.rightWheelValue

    def setWheelsValue(self, leftValue: int, rightValue: int):
        self.leftWheelValue, self.rightWheelValue = leftValue, rightValue
    
    def getSpeed(self):
        return self.speed

    def setSpeed(self, value: int):
        self.speed = value

class BotLine:
    packetQueue = Queue()

    def __init__(self, ip: str, port:int):
        self.networkManager = NetworkManager(SocketAddress(ip, port))
        self.connecting()

        self.information = JetbotInformation()
        self.stateThread = StateUpdateThread()
        self.stateThread.start()
    
    def connecting(self):
        packet = OutputPacket()
        packet.writeCommand(MessageType.CONNECT)
        self.networkManager.sendTo(packet, SocketAddress(HOST, PORT))

    def onUpdate(self):
        # 패킷 처리
        self.information.updateInformation(self.stateThread.getState())
        self.processIncomingPackets()
    
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

            packet.writeUInt16(self.information.getLeftWheelValue())
            packet.writeUInt16(self.information.getRightWheelValue())
            packet.writeUInt16(self.information.getSpeed())
            
            self.networkManager.sendTo(packet, address)

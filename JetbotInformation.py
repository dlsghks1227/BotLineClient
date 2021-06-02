import threading
import time
import subprocess
from ina219 import *

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
        cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
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

    def controlJetbot(self):
        pass

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
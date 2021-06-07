import threading
import time
import subprocess

from Packet import MoveState
from Information import Information
from ina219 import *
from jetbot import Robot

class StateUpdateThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.ina219 = INA219(addr=0x41)
        self.robot = Robot()
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

class JetbotInformation(Information):
    def __init__(self):
        super().__init__()

    def updateInformation(self, state: tuple):
        self.voltage, self.cpu, self.memory, self.disk = state

    def controlJetbot(self):
        if self.isMasterStop == MoveState.STOP:
            self.robot.set_motors(0, 0)
        else:
            speedOffset = (self.speed * 0.5)
            leftOffset = (self.leftWheelValue * 0.1) * speedOffset
            rightOffset = (self.leftWheelValue * 0.1) * speedOffset
            self.robot.set_motors(leftOffset, rightOffset)
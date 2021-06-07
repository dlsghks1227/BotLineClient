import threading
import time
import subprocess

from ina219 import *

class StateUpdateThread(threading.Thread):
    def __init__(self, objectType: int):
        super().__init__()
        self.type = objectType
        if self.type == 1:
            self.ina219 = INA219(addr=0x41)
        else:
            self.ina219 = None

        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0
        self.isRunning = True
    
    def run(self):
        while self.isRunning:
            if self.type == 1:
                self.voltage = self.ina219.getBusVoltage_V()
            else:
                self.voltage = 0.0
            self.cpu = self.loadCPUAverage()
            self.memory = self.loadMemory()
            self.disk = self.loadDisk()
            time.sleep(0.5)

    def getState(self):
        return self.voltage, self.cpu, self.memory, self.disk

    def setIsRunning(self, isRunning):
        self.isRunning = isRunning

    def loadCPUAverage(self):
        if self.type == 1 or self.type == 3:
            cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
            return float(subprocess.check_output(cmd, shell=True))
        else:
            return 0.0

    def loadMemory(self):
        if self.type == 1 or self.type == 3:
            cmd = "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'"
            return float(subprocess.check_output(cmd, shell=True))
        else:
            return 0.0

    def loadDisk(self):
        if self.type == 1 or self.type == 3:
            cmd = "df -h | awk '$NF==\"/\"{printf \"%.2f\", $3 / $2 * 100}'"
            return float(subprocess.check_output(cmd, shell=True))
        else:
            return 0.0
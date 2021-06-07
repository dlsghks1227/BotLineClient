import threading
import time
import subprocess

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
        pass

    def updateInformation(self, state: tuple):
        self.voltage, self.cpu, self.memory, self.disk = state

    def controlJetbot(self):
        pass
import threading
import time

class StateUpdateThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0
        self.isRunning = True
    
    def run(self):
        while self.isRunning:
            self.voltage += 0.01
            self.cpu += 0.01
            self.memory += 0.01
            self.disk += 0.01
            time.sleep(0.5)

    def getState(self):
        return self.voltage, self.cpu, self.memory, self.disk

    def setIsRunning(self, isRunning):
        self.isRunning = isRunning
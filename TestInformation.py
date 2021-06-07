import threading
import time

from Information import Information


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
            self.voltage += 0.01
            self.cpu += 0.01
            self.memory += 0.01
            self.disk += 0.01
            time.sleep(0.5)

    def getState(self):
        return self.voltage, self.cpu, self.memory, self.disk

    def setIsRunning(self, isRunning):
        self.isRunning = isRunning

class JetbotInformation(Information):
    def __init__(self):
        self.objectHash = 0
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
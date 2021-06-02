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
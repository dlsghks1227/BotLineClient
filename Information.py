class Information:
    def __init__(self):
        self.objectHash = 0
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0

        self.leftWheelValue = 0
        self.rightWheelValue = 0
        self.speed = 0

    def getVoltage(self):
        return self.voltage
    
    def getCPU(self):
        return self.cpu

    def getMemory(self):
        return self.memory

    def getDisk(self):
        return self.disk

    def getObjectHash(self):
        return self.objectHash

    def setObjectHash(self, objectHash):
        self.objectHash = objectHash

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
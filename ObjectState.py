class ObjectState:
    def __init__(self):
        self.hash = 0
        
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0

    def update(self, value: tuple):
        self.voltage, self.cpu, self.memory, self.disk = value

class JetbotObjectState(ObjectState):
    def __init__(self):
        super().__init__()
        
        self.leftWheelValue = 0
        self.rightWheelValue = 0
        self.speed = 0
    
    def setWheelsValue(self, value: tuple):
        self.leftWheelValue, self.rightWheelValue = value

class XavierObjectState(ObjectState):
    def __init__(self):
        super().__init__()

        self.isStop = 0
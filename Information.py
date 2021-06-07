from Packet import MoveState

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

    def setWheelsValue(self, leftValue: int, rightValue: int):
        self.leftWheelValue, self.rightWheelValue = leftValue, rightValue
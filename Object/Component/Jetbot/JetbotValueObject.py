from enum import Enum

class JetbotStateValueObject:
    def __init__(self) -> None:
        self.voltage = 0.0
        self.cpu = 0.0
        self.memory = 0.0
        self.disk = 0.0

class JetbotPositionValueObject:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

class JetbotPosition(Enum):
    LEFT = 0x00
    RIGHT = 0x01
    TOP = 0x02
    BOTTOM = 0x03

    DEFAULT = 0xFF

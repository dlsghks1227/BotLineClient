from enum import Enum

class MessageType(Enum):
    CONNECT = 0x00
    DISCONNECT = 0x01

    INFORMATION_REQUEST = 0x02
    CONTROL = 0x03

    CONNECT_CHECK = 0x04

    ALL_STOP = 0x05

    DEFAULT = 0xFF
    
class ObjectType(Enum):
    JETBOT = 0x01
    XAVIER = 0x02
    TEST = 0x01

class MoveState:
    GO = 0x00
    STOP = 0x01
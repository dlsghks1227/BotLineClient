from enum import Enum


class MessageType(Enum):
    CONNECT = 0x00
    DISCONNECT = 0x01

    INFORMATION_REQUEST = 0x02
    END_DATA = 0x03

    CONTROL = 0x04

    CONNECT_CHECK = 0x05

    ALL_STOP = 0x06

    DEFAULT = 0xFF


class ObjectType(Enum):
    JETBOT = 0x01
    XAVIER = 0x02
    WEB = 0x03
    TEST = 0x01


class MoveState:
    GO = 0x00
    STOP = 0x01
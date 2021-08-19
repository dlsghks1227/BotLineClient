from enum import Enum


class MessageType(Enum):
    CONNECT = 0x00
    DISCONNECT = 0x01
    CONNECT_CHECK = 0x02

    INFO_CURRENT_STATE = 0x10
    INFO_JETBOT_POSITION = 0x11

    JETBOT_CONTROL = 0x20
    JETBOT_ARRIVED = 0x21
    JETBOT_ALL_STOP = 0x22

    JETBOT_POSITION_ERROR = 0xE0

    END_DATA = 0xFE
    DEFAULT = 0xFF


class ObjectType(Enum):
    JETBOT = 0x01
    XAVIER = 0x02
    WEB = 0x03
    TEST = 0x01
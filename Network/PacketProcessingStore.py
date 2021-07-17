from Network.SocketAddress import SocketAddress
from typing import Callable

from Network.PacketType import *
from Network.Packet import *

class PacketProcessingStore:
    def __init__(self) -> None:
        self.__commands = dict()

    def add(self, command: MessageType, handler: Callable[[InputPacket, SocketAddress], OutputPacket]) -> None:
        self.__commands[command] = handler

    @property
    def commands(self) -> dict:
        return self.__commands
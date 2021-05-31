import struct
import time
from BotLine import BotLine
from SocketAddress import SocketAddress
from Packet import *

# https://docs.python.org/ko/3/library/struct.html


if __name__ == "__main__":
    botLine = BotLine('0.0.0.0', 8080)
    try:
        while True:
            botLine.onUpdate()

            time.sleep(0.001)

    except KeyboardInterrupt:
        botLine.onDestory()

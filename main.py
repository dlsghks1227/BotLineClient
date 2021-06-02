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
            start = time.perf_counter()
            time.sleep(0.001)
            botLine.onUpdate(time.perf_counter() - start)


    except KeyboardInterrupt:
        botLine.onDestory()

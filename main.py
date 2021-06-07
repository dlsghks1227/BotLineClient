import argparse
import time
from BotLineOfTest import BotLineOfTest
from BotLineOfJetbot import BotLineOfJetbot
from BotLineOfXavier import BotLineOfXavier
from Packet import *

# https://docs.python.org/ko/3/library/struct.html


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1', help='Server ip')
    parser.add_argument('--port', dest='port', type=int, default=8000, help='Server port')
    parser.add_argument('--type', dest='type', type=int, default=1, help='Object type')
    args, _ = parser.parse_known_args()
    
    if args.type == 1:
        botLine = BotLineOfJetbot(args.host, args.port)
    elif args.type == 3:
        botLine = BotLineOfXavier(args.host, args.port)
    else:
        botLine = BotLineOfTest(args.host, args.port)
    
    try:
        while True:
            start = time.perf_counter()
            time.sleep(0.001)
            botLine.onUpdate(time.perf_counter() - start)


    except KeyboardInterrupt:
        botLine.onDestory()

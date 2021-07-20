import argparse
import time
# https://docs.python.org/ko/3/library/struct.html

from BotLine import *
from Lib.Log import Log

if __name__ != "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1', help='Server ip')
    parser.add_argument('--port', dest='port', type=int, default=8000, help='Server port')
    parser.add_argument('--type', dest='type', type=str, default="test", help='Object type')
    args, _ = parser.parse_known_args()
    
    botLine = BotLine(args.type.upper(), args.host, args.port)
    
    try:
        while True:
            botLine.onUpdate()

    except KeyboardInterrupt:
        botLine.onDestory()
        Log("Process Stop..")

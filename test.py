from time import time
from Object.BotLineObject import TestObject

import time

if __name__ == "__main__":
    test = TestObject()

    try:
        t0 = 0.0
        elapsedTime = 0.0
        while True:
            # elapsedTime += time.clock_getres(time.CLOCK_PROCESS_CPUTIME_ID) * 1e8
            t0 = time.perf_counter()

            # do something..
            test.onUpdate(elapsedTime)
            
            elapsedTime = time.perf_counter() - t0

    except KeyboardInterrupt:
        test.onDestory()
        print("Stop")
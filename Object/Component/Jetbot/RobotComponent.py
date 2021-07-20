from jetbot import Robot

from Lib.Log import Log

class RobotComponent:
    def __init__(self) -> None:
        super().__init__()

        self.__robot = None

        self.__isStop = False
        self.__leftWheel = 0.0
        self.__rightWheel = 0.0

    def onUpdate(self, elspasedTime: float) -> None:
        if self.__robot is not None:
            if self.__isStop is True:
                self.__leftWheel = 0.0
                self.__rightWheel = 0.0
                self.__robot.stop()
                Log("Stop")
            else:
                self.__robot.set_motors(self.__leftWheel, self.__rightWheel)

    def onDestory(self) -> None:
        pass

    @robot.setter
    def robot(self, value: Robot) -> None:
        self.__robot = value

    @isStop.setter
    def isStop(self, value: bool) -> None:
        self.__isStop = value

    @leftWheel.setter
    def leftWheel(self, value: float) -> None:
        self.__leftWheel = value
    
    @rightWheel.setter
    def rightWheel(self, value: float) -> None:
        self.__rightWheel = value
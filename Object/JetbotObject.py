from Object.Component.Jetbot.JetbotStateComponent import JetbotStateComponent
from Object.Component.Jetbot.JetbotNetworkComponent import JetbotNetworkComponent
from Object.Component.Jetbot.RobotComponent import RobotComponent

from Object.BotLineObject import *
from Object.Component.NetworkComponent import *
from Object.Component.StateComponent import *

from jetbot import Robot

from Lib.Log import Log

class JetbotObject(BotLineObject):
    def __init__(self, address: SocketAddress) -> None:
        super().__init__(address)
        self.stateComponent = JetbotStateComponent()
        self.stateComponent.start()

        self.networkComponent = JetbotNetworkComponent(ObjectType.JETBOT, self._address)

        self.robotComponent = RobotComponent()

    def onUpdate(self, elapsedTime: float) -> None:
        super().onUpdate(elapsedTime)
        self.networkComponent.onUpdate(elapsedTime)
        self.networkComponent.setObjectState(self.stateComponent.state)

        if self.networkComponent.isConnected:
            self.robotComponent.isStop = self.networkComponent.isStop
        else:
            self.robotComponent.isStop = False
        self.robotComponent.onUpdate(elapsedTime)

    def onDestory(self) -> None:
        super().onDestory()
        self.stateComponent.isRunning = False
        self.stateComponent.join()

        self.networkComponent.onDestory()

        self.onDestory()

    def setRobot(self, value: Robot) -> None:
        self.robotComponent.robot = value
    
    def setLeftWheel(self, value: float) -> None:
        self.robotComponent.leftWheel = value

    def setRightWheel(self, value: float) -> None:
        self.robotComponent.rightWheel = value

    def setWheels(self, left: float, right: float) -> None:
        self.robotComponent.leftWheel = left
        self.robotComponent.rightWheel = right
    
    def getIsStop(self) -> bool:
        return self.networkComponent.isStop
import threading
import time
import subprocess

from Packet import MoveState
from Information import Information
from ina219 import *
from jetbot import Robot

class JetbotInformation(Information):
    def __init__(self):
        super().__init__()

    def updateInformation(self, state: tuple):
        self.voltage, self.cpu, self.memory, self.disk = state

    def controlJetbot(self):
        if self.isMasterStop == MoveState.STOP:
            self.robot.set_motors(0, 0)
        else:
            speedOffset = (self.speed * 0.5)
            leftOffset = (self.leftWheelValue * 0.1) * speedOffset
            rightOffset = (self.leftWheelValue * 0.1) * speedOffset
            self.robot.set_motors(leftOffset, rightOffset)
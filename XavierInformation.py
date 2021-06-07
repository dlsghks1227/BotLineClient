from Packet import MoveState
import threading
import time
import subprocess

from Information import Information

class JetbotInformation(Information):
    def __init__(self):
        super().__init__()
        
        self.wasSend = False
        self.isStop = MoveState.GO

    def updateInformation(self, state: tuple):
        self.voltage, self.cpu, self.memory, self.disk = state

    def controlJetbot(self):
        if self.isStop != self.isMasterStop:
            self.isStop = self.isMasterStop
            self.wasSend = False
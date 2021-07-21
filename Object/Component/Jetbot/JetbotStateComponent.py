import subprocess

from Object.Component.StateComponent import *

from Lib.ina219 import *
from Lib.ads1115 import *

class JetbotStateComponent(StateComponent):
    def __init__(self) -> None:
        super().__init__()

        self.__ina219 = INA219(addr=0x41)
        # self.__ads = ADS1115()

    def onUpdate(self) -> None:
        super().onUpdate()

        self._state.voltage = self.__ina219.getBusVoltage_V()
        self._state.cpu = self.loadCPUAverage()
        self._state.memory = self.loadMemory()
        self._state.disk = self.loadDisk()

    def loadCPUAverage(self) -> float:
        cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
        return float(subprocess.check_output(cmd, shell=True))
    
    def loadMemory(self) -> float:
        cmd = "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'"
        return float(subprocess.check_output(cmd, shell=True))
    
    def loadDisk(self) -> float:
        cmd = "df -h | awk '$NF==\"/\"{printf \"%.2f\", $3 / $2 * 100}'"
        return float(subprocess.check_output(cmd, shell=True))
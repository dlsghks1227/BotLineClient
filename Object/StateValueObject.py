class StateValueObject:
    def __init__(self) -> None:
        super().__init__()

        self.__voltage = 0.0
        self.__cpu = 0.0
        self.__memory = 0.0
        self.__disk = 0.0

    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, value: float) -> None:
        self.__voltage = value

    @property
    def cpu(self) -> float:
        return self.__cpu

    @cpu.setter
    def cpu(self, value: float) -> None:
        self.__cpu = value

    @property
    def memory(self) -> float:
        return self.__memory

    @memory.setter
    def memory(self, value: float) -> None:
        self.__memory = value

    @property
    def disk(self) -> float:
        return self.__disk

    @disk.setter
    def disk(self, value: float) -> None:
        self.__disk = value
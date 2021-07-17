from Object.BotLineObject import BotLineObject

class BotLineFactory:
    def __init__(self) -> None:
        pass

    def getBotLineObject(self, type: str) -> BotLineObject:
        if type == "jetbot":
            return None
        elif type == "xavier":
            return None
        else:
            return None
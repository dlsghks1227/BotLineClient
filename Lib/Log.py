import datetime

def Log(text: str) -> None:
    print(f"[{datetime.datetime.now()}] " + text)
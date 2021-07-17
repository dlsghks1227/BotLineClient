import datetime

def Log(text: str):
    print(f"[{datetime.datetime.now()}] " + text)
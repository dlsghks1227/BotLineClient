# BotLineClient

## Introduction

임베디드 기기(Jetbot, Xavier 등등)와 서버간의 통신을 하기 위한 클라이언트 제작

## Requirements

Programming language: Python 3.6

## File structure

```
Client
├── Lib
│    ├── __init__.py
│    ├── ads1115.py
│    ├── ina219.py
│    └── Log.php
├── Network
│    ├── __init__.py
│    ├── NetworkManager.py
│    ├── Packet.py
│    ├── PacketProcessingStore.py
│    ├── PacketType.py
│    └── SocketAddress.py
├── Object
│    ├── Component
│    │    ├── Jetbot
│    │    │    ├── __init__.py
│    │    │    ├── JetbotNetworkComponent.py
│    │    │    ├── JetbotStateComponent.py
│    │    │    └── RobotComponent.py
│    │    ├── Test
│    │    │    ├── __init__.py
│    │    │    ├── TestNetworkComponent.py
│    │    │    └── TestStateComponent.py
│    │    ├── Xavier
│    │    │    ├── __init__.py
│    │    │    ├── XavierNetworkComponent.py
│    │    │    └── XavierStateComponent.py
│    │    ├── __init__.py
│    │    ├── NetworkComponent.py
│    │    └── StateComponent.py
│    ├── __init__.py
│    ├── BotLineObject.py
│    ├── BotLineObjectFactory.py
│    ├── JetbotObject.py
│    ├── StateValueObject.py
│    ├── TestObject.py
│    └── XavierObject.py
├── __init__.py
├── BotLine.py
└── main.py
```

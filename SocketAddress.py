class SocketAddress:
    def __init__(self, ip='0.0.0.0', port=0):
        self.ip = ip
        self.port = port

    def getAddressAndPort(self):
        return self.ip, self.port

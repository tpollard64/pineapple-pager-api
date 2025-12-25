class ReconAPI:
    def __init__(self, client):
        self.client = client

    def connected_clients(self):
        return self.client.exec("iw dev wlan0 station dump")

    def interfaces(self):
        return self.client.exec("ip addr")

    def routes(self):
        return self.client.exec("ip route")

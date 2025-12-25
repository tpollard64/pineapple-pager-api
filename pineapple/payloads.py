class PayloadManager:
    BASE_PATH = "/root/payloads"

    def __init__(self, client):
        self.client = client

    def list_categories(self):
        return self.client.exec(f"ls {self.BASE_PATH}")["stdout"].split()

    def list_payloads(self, category):
        path = f"{self.BASE_PATH}/{category}"
        return self.client.exec(f"ls {path}")["stdout"].split()

    def enable_payload(self, category, payload):
        cmd = f"touch {self.BASE_PATH}/{category}/{payload}/.enabled"
        return self.client.exec(cmd)

    def disable_payload(self, category, payload):
        cmd = f"rm -f {self.BASE_PATH}/{category}/{payload}/.enabled"
        return self.client.exec(cmd)

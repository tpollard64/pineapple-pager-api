class PagerAPI:
    def __init__(self, client):
        self.client = client

    def alert(self, title, message):
        cmd = (
            f"pager alert "
            f"--title '{title}' "
            f"--message '{message}'"
        )
        return self.client.exec(cmd)

    def vibrate(self):
        return self.client.exec("pager vibrate")

    def play_tone(self, tone="default"):
        return self.client.exec(f"pager tone {tone}")

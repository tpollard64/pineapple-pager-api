import paramiko

class PineappleClient:
    def __init__(self, host="172.16.52.1", user="root", password=None, port=22):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self._client = None

    def connect(self):
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(
            hostname=self.host,
            username=self.user,
            password=self.password,
            port=self.port,
            timeout=10,
        )

    def close(self):
        if self._client:
            self._client.close()

    def exec(self, command):
        if not self._client:
            raise RuntimeError("Not connected to Pineapple")

        stdin, stdout, stderr = self._client.exec_command(command)
        return {
            "stdout": stdout.read().decode(),
            "stderr": stderr.read().decode(),
            "exit_code": stdout.channel.recv_exit_status(),
        }

import os
import time
from pineapple.client import PineappleClient
from pineapple.pager import PagerAPI

password = os.getenv("PINEAPPLE_PASSWORD")
client = PineappleClient(password=password)
client.connect()

pager = PagerAPI(client)

# Send an alert every 60 seconds
try:
    while True:
        pager.alert(
            title="Heartbeat",
            message="Python API is connected and running."
        )
        time.sleep(60)
except KeyboardInterrupt:
    print("Stopping scheduled alerts.")
    client.close()

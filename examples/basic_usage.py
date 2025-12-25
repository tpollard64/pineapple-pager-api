import os
from pineapple.client import PineappleClient
from pineapple.pager import PagerAPI
from pineapple.payloads import PayloadManager

# Read password from environment variable
# macOS / Linux: export PINEAPPLE_PASSWORD="your_password"
# Windows: set PINEAPPLE_PASSWORD="your_password"
password = os.getenv("PINEAPPLE_PASSWORD")
if not password:
    raise ValueError("Environment variable PINEAPPLE_PASSWORD is not set")

# Connect to Pineapple
client = PineappleClient(password=password)
client.connect()

# Initialize API interfaces
pager = PagerAPI(client)
payloads = PayloadManager(client)

# Send an alert
pager.alert(
    title="API Connected",
    message="Python API successfully connected to Pineapple Pager"
)

# List payloads
print(payloads.list_categories())
print(payloads.list_payloads("alerts"))

# Close connection
client.close()

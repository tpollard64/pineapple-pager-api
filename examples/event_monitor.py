import os
from pineapple.client import PineappleClient
from pineapple.pager import PagerAPI

password = os.getenv("PINEAPPLE_PASSWORD")
client = PineappleClient(password=password)
client.connect()

pager = PagerAPI(client)

# Callback function for incoming events
def handle_event(event):
    print(f"Event detected: {event['type']} - {event.get('details', '')}")
    # Example: send an alert for critical events
    if event['type'] == 'deauth_flood_detected':
        pager.alert(
            title="Deauth Flood Detected",
            message="A deauth flood was detected by Pineapple!"
        )

# Start monitoring
client.start_event_listener(handle_event)

try:
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    print("Stopping event listener...")
    client.stop_event_listener()
    client.close()

# Pineapple Pager Python API

A Python library for interacting with the Pineapple Pager device. It allows you to connect, monitor events, and manage payloads from your Pineapple device using Python.

## Features

- Connect to a Pineapple device
- Send alerts via Pager API
- List and manage payloads
- Monitor events like deauth floods or handshake captures

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tpollard64/pineapple-pager-python-api.git
cd pineapple-pager-python-api
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

Store your Pineapple password in an environment variable for security:

```bash
export PINEAPPLE_PASSWORD="your_password_here"
```

On Windows PowerShell:

```powershell
setx PINEAPPLE_PASSWORD "your_password_here"
```

## Usage

```python
import os
from pineapple.client import PineappleClient
from pineapple.pager import PagerAPI
from pineapple.payloads import PayloadManager

password = os.getenv("PINEAPPLE_PASSWORD")
if not password:
    raise ValueError("Environment variable PINEAPPLE_PASSWORD is not set")

client = PineappleClient(password=password)
client.connect()

pager = PagerAPI(client)
payloads = PayloadManager(client)

pager.alert(
    title="API Connected",
    message="Python API successfully connected to Pineapple Pager"
)

print(payloads.list_categories())
print(payloads.list_payloads("alerts"))

client.close()
```

## Examples

Check the `examples/` folder for more usage examples.

## Contributing

Contributions are welcome. Open issues or submit pull requests.

## Troubleshooting

* **Connection errors**: Ensure the Pineapple device is reachable, SSH is enabled, and the correct port is used.
* **Environment variable not set**: Make sure `PINEAPPLE_PASSWORD` is exported before running scripts.
* **Dependency issues**: Run `pip install -r requirements.txt` from the project root.

## License

MIT License

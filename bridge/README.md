# WhoFi Local Bridge

The hosted WhoFi PWA cannot reliably read the router admin page directly because browser HTTPS/local-network security restrictions. This small read-only bridge runs on a computer connected to your home Wi-Fi.

## Start it (Mac)

1. Download `bridge/whofi_bridge.py` from this repository.
2. Open Terminal in the folder where it downloaded and run:

```bash
python3 whofi_bridge.py
```

Keep the Terminal window open while using WhoFi. The bridge listens only on your computer (`127.0.0.1:8765`) and does not change router settings.

Then open WhoFi and press **Check local bridge**.

Press Ctrl+C to stop it.

## Current scope

The bridge currently tests router reachability and returns a small response preview. It does not authenticate to the router or expose connected clients yet. Credentials are not collected or stored.

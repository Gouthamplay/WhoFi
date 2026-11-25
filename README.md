# Network Command Center

This branch replaces the app files for the user's home-network dashboard. The original Hydrate project remains available on main and on the backup branch.

Current preview: responsive PWA shell with a router snapshot, device search, network overview, analytics placeholder, and disabled control actions. Data is not live. Authentication is not implemented. Do not deploy publicly as a private service until backend authentication, API authorization, rate limiting and session security are completed.

Router target: GX Titanium T21 Pro / Titanium-2122A, hardware C40-210, firmware T2122-V1.28, gateway 192.168.1.1.

Never store router admin credentials in GitHub or frontend code. Do not expose router administration to the public internet.
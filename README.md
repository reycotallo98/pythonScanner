# pythonScanner
Fast port scanner designed in python for internal pentest which is not possible to use nmap or is very slown to use from our host.

# How to use
- First of all you need to make a file named ips with all host that you want to scan following this parameters:
```file
IP1
IP2
...
```
- After that run pythonNetworkScanner.py on same folder than your file. Afte that it will scan all TCP ports of the targets.
- When your scans will be created, you need to get files into your host.
- After that put them on a folder with pythonServiceNmapScanner.py and run it, it will return al services and fingerprint about these ports. ***THIS LAST SCRIPT IS ADAPTED TO USE PROXYCHAINS, remake command in script to your personal use***

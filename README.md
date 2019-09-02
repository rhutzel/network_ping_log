# Network Ping Log

This is a Python utility that pings a host every 10 seconds and logs
if each attempt was successful. The logs rollover at 1MB.

## Running from source

`python3 main.py hostname`

## Compiling to binary

`make`

## Running from binary

`./bin/network_ping_log hostname`

import socket
import threading
import sys
from string import printable
from blessings import Terminal
import binascii

t = Terminal()

print(t.bold_blue_on_white('Welcome to LAN Chat!'))

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))

while True:
  data, addr = client.recvfrom(1024)
  with t.location(0, t.height - 1):
    name, msg = data.decode().split()
    ucolor = int(binascii.hexlify(name.encode()), 16) % 16
    line = t.on_color(ucolor)(name) + " " +  t.color(ucolor)(msg)
    print(line)
import socket
import sys
from string import printable
from blessings import Terminal

term = Terminal()
username = sys.argv[1]

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

with term.fullscreen():

  while True:
    print(term.clear() + '>>> ', end = '')
    msg = input()
    if msg.rstrip("\n\r") != '':
      payload = "{} {}".format(username, msg)
      client.sendto(payload.encode(), ('<broadcast>', 34567))

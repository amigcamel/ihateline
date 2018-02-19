"""Socket client."""
import socket
import sys

from ajilog import logger

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")

logger.info(f'command: {data})')
logger.info(f'command: {received}')

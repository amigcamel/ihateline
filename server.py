"""Socket server."""
import socketserver
import os

from ajilog import logger


class TCPHandler(socketserver.StreamRequestHandler):
    """TCP server."""

    def handle(self):
        """Handle incoming data."""
        self.data = self.rfile.readline().strip()
        logger.info("{} wrote:".format(self.client_address[0]))
        logger.info(self.data)
        os.system(
            self.data.decode('utf-8')
        )
        self.wfile.write(b'ok')


if __name__ == "__main__":
    HOST, PORT = 'localhost', 9999

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()

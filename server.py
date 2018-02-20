"""Socket server."""
import socketserver
import os

from ajilog import logger

from ihateline.browser import Browser


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
    b = Browser()
    b.login()
    b.cache_session_info()
    HOST, PORT = '', 9999

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        logger.info('server started')
        server.serve_forever()

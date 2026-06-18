#!/usr/bin/env python3
"""
Spidertrap — traps web crawlers in an infinite set of dynamically generated pages.
"""

import logging
import os
import random
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

### Configuration ###
LINKS_PER_PAGE = (5, 50)
LENGTH_OF_LINKS = (3, 20)
PORT = 80
DELAY = 350  # milliseconds
CHAR_SPACE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-/"
LOG_FILE = "/log/spidertrap.log"
### End Configuration ###


def setup_logging() -> logging.Logger:
    logger = logging.getLogger("spidertrap")
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(message)s")

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(fmt)
    logger.addHandler(stream_handler)

    log_dir = os.path.dirname(LOG_FILE)
    if os.path.isdir(log_dir):
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)

    return logger


logger = setup_logging()


class Handler(BaseHTTPRequestHandler):
    webpages = None

    def generate_page(self, seed: str) -> str:
        """Generate a webpage containing only links."""
        html = "<html>\n<body>\n"
        random.seed(seed)
        num_links = random.randint(*LINKS_PER_PAGE)

        if self.webpages is None:
            for _ in range(num_links):
                address = "".join(
                    random.choice(CHAR_SPACE)
                    for _ in range(random.randint(*LENGTH_OF_LINKS))
                )
                html += f'<a href="{address}">{address}</a><br>\n'
        else:
            for _ in range(num_links):
                address = random.choice(self.webpages).strip()
                html += f'<a href="{address}">{address}</a><br>\n'

        html += "</body>\n</html>"
        return html

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        time.sleep(DELAY / 1000.0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.generate_page(self.path).encode())

    def log_message(self, fmt, *args):
        logger.info(
            "%s - - [%s] %s",
            self.address_string(),
            self.log_date_time_string(),
            fmt % args,
        )


def print_usage():
    print(f"Usage: {sys.argv[0]} [FILE]\n")
    print(
        "FILE is a file containing webpage names to serve, one per line.\n"
        "If no file is provided, random links are generated."
    )


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        print_usage()
        return

    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as f:
                lines = f.readlines()
            if lines:
                Handler.webpages = lines
            else:
                logger.warning("File provided was empty. Using randomly generated links.")
        except OSError:
            logger.warning("Can't read input file. Using randomly generated links.")

    try:
        logger.info("Starting server on port %d...", PORT)
        server = HTTPServer(("", PORT), Handler)
        logger.info("Server started. Use <Ctrl-C> to stop.")
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Stopping server...")
        server.socket.close()
        logger.info("Server stopped.")
    except Exception as e:
        logger.error("Error starting HTTP server on port %d: %s", PORT, e)
        logger.error("Ensure you have required permissions and port %d is available.", PORT)
        sys.exit(1)


if __name__ == "__main__":
    main()

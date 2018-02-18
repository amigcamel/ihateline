"""Commandline utilities."""
from argparse import ArgumentParser
from time import sleep

from ajilog import logger

from ihateline.browser import Browser


def select_and_send(friend, message):
    """Select a friend and send message."""
    b = Browser()
    sleep(3)
    b.login()
    sleep(3)
    for i in range(10):
        try:
            b.select_friend(friend)
            sleep(1)
            b.send_msg(message)
            sleep(0.5)
            break
        except Exception:
            logger.warn(f'Unable to select {friend} (retry left: {10 - i})')
        sleep(1)
    b.logout()
    logger.debug('logged out!')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--friend', type=str, required=True,
                        help='LINE friend name or id')
    parser.add_argument('-m', '--message', type=str, required=True,
                        help='Message to be sent')
    args = parser.parse_args()
    select_and_send(args.friend, args.message)

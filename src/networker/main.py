# TODO : Remove this file when the networker module is OK

from src.networker.client import ClientReceiver


if __name__ == '__main__':
    r = ClientReceiver(None)
    r.start()

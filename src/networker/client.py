"""
This file contains all classes and functions to create a game client
"""

from . import BUFF_SIZE
from .handler import Handler
from .data_provider import DataProvider

from threading import Thread
import socket


class GameClient:
    """
    This class represent a game client, that is a template for a sub-class
    """

    # ----- Constructor -----

    def __init__(self):
        """
        Create a new game client with the wanted parameters
        """

        # Assign attributes
        self._server_ip: str = None
        self._server_port: int = None
        self._server_password: str = None
        self._handlers: dict = dict()
        self._providers: set = set()

    # ----- Getter and setters -----

    def get_server_addr(self) -> tuple:
        """
        Get the server address in a tuple

        return -> tuple = The server address in a tuple (ip, port)
        """

        return self._server_ip, self._server_port

    def set_server_addr(self, server_ip: str, server_port: int) -> None:
        """
        Set the game server address

        params :
            - server_ip: str = The server IP address
            - server_port: int = The server port
        """

        # Set the server ip and port
        self._server_ip = server_ip
        self._server_port = server_port

    def get_server_password(self) -> str:
        """
        Get the server password

        return -> str = The server password
        """

        return self._server_password

    def set_server_password(self, password: str) -> None:
        """
        Set the server password

        params :
            - password: str = The server password
        """

        self._server_password = password

    def add_handler(self, handler: Handler) -> None:
        """
        Add an handler to the receiver, if it already exists, the old is replaced

        params :
            - handler: Handler = The handler to add
        """

        if handler.command != "":
            self._handlers[handler.command] = handler

    def remove_handler(self, command: str) -> None:
        """
        Remove the handler of the wanted command

        params :
            - command: str = The command to remove the handler
        """
        if command != "":
            self._handlers[command] = None

    def add_provider(self, data_provider: DataProvider) -> None:
        """
        Add a data provider to the client

        params :
            - data_provider: DataProvider = The data provider to add
        """

        self._providers.add(data_provider)

    def remove_provider(self, data_provider: DataProvider) -> None:
        """
        Remove a data provider from the client

        params :
            - data_provider: DataProvider = The data provider to remove
        """

        self._providers.remove(data_provider)

    # ----- Game Client control methods -----


class ClientReceiver(Thread):
    """
    This class represent a data receiver that handle all received messages in a separate thread
    """

    # ----- Constructor -----

    def __init__(self, game_client: GameClient):
        """
        Create a new Receiver with a given game client

        params :
            - game_client: GameClient : The game client associated with the receiver
        """

        # Call the thread super constructor
        super(ClientReceiver, self).__init__()

        # Set the attributes
        self.game_client: GameClient = game_client
        self._running: bool = False
        self._port: int = 8099
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # ----- Receiver control methods -----

    def run(self):
        """
        This function start the thread that receive all UDP messages
        """

        # Set the running attribute
        self._running = True
        print("Client listener started at port " + str(self._port))

        # Bind the socket
        self._socket.bind(("0.0.0.0", self._port))

        while self._running:
            data, address = self._socket.recvfrom(BUFF_SIZE)

            print(data.decode("utf8", "strict"))

        # Close the socket
        self._socket.close()

    def stop(self):
        """
        Method to stop the receiver
        """

        self._running = False

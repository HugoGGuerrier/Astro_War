class Handler:
    """
    This class represent an UDP message handler
    """

    # ----- Constructor -----

    def __init__(self, command: str, func=None, instance=None):
        """
        Create a new handler with the command and the function to call

        params :
            - command: str = The command that the handler has to handle
            - func = The function to call (can be None)
            - instance = The instance to call the function on (can be None)
        """

        # Assign the attributes
        self.command: str = command
        self.func = func
        self.instance = instance

    # ----- Class methods -----

    def apply(self, data: str) -> None:
        """
        Execute the handler with the wanted data

        params :
            - data: str = The data to call the handler with
        """

        # Test if the func and the instance are not None
        if self.func is not None:
            if self.instance is not None:
                self.func(self.instance, data)
            else:
                self.func(data)

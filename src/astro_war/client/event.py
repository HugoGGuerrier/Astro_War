class Event:
    """
    This class represent an event on the game window
    """

    # ----- Static values -----

    KEY_PRESS: int = 0
    KEY_RELEASE: int = 1

    # ----- Class methods -----

    def __init__(self, elem_type: int, **kwargs):
        """
        Create the event with its name and its parameters

        params :
            - name: str = The name of the event
            - **kwargs = The information to store about the event
        """

        self.elem_type: int = elem_type
        self.info = kwargs
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        """
        Get the string representation of the event
        """

        res = "{ " + str(self.elem_type) + " : "
        for key in self.info:
            res += str(key) + "=" + str(self.info[key]) + " "
        res += "}"
        return res

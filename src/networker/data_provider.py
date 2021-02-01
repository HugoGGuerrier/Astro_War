class DataProvider:
    """
    This class represent a data provider for the server and the client, it should be implemented by subclass
    """

    # ----- Interfaces method -----

    def provide(self):
        """
        This method should be override by the subclass
        """

        raise Exception("DataProvider.provide : Abstract method not implemented !")

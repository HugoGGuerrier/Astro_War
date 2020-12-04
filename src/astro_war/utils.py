import sys


def encrypt_save(save_str: str) -> bytearray:
    """
    Encrypt a save string to avoid user modifying it :)

    params :
        - save_str: str = The non encrypted save string

    return -> bytearray = The encrypted bytes
    """

    # Prepare the result
    int_list: list = list()

    # Iterate over the string and transform it
    for char in save_str:
        int_list.append((ord(char) + 42) % 256)

    # Return the result
    return bytearray(int_list)


def decrypt_save(save_str: bytes) -> str:
    """
    Decrypt a save string in order to load it

    params :
        - save_str: bytes = The encrypted save string

    return -> str = The decrypted json string
    """

    # Prepare the result
    res: str = ""

    # Iterate over encrypted string
    for integer in save_str:
        res += chr((integer - 42) % 256)

    # Return the result
    return res

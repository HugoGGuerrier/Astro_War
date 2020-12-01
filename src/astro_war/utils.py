import sys


def encrypt_save(save_str: str) -> str:
    """
    Encrypt a save string to avoid user modifying it :)

    params :
        - save_str: str = The non encrypted save string

    return -> str = The encrypted string
    """

    # Prepare the result
    res: str = ""

    # Iterate over the string and transform it
    for char in save_str:
        res += chr((ord(char) + 42) % sys.maxunicode)

    # Return the result
    return res


def decrypt_save(save_str: str) -> str:
    """
    Decrypt a save string in order to load it

    params :
        - save_str: str = The encrypted save string

    return -> str = The decrypted json string
    """

    # Prepare the result
    res: str = ""

    # Iterate over encrypted string
    for char in save_str:
        res += chr((ord(char) - 42) % sys.maxunicode)

    # Return the result
    return res

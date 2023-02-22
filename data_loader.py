import random
def load_file_as_binary(path) -> str:
    """
    Returns a binary string generated from the file.

    :param path: Path to the wanted file.
    :return:
    """
    with open(path, "rb") as file:
        f = file.read()

        b = bytearray(f)
        val = int.from_bytes(b, "little")
        return f"{val:b}"

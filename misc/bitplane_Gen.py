import random

def generate8by8bitplane() -> int:
    """
    Generate an 8 by 8 bit plane.

    8*8 = 64
    :return:
    """
    value = random.randint(0, 2**64)
    return value


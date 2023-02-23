from classes.bitplane.BitPlane64 import Bitplane64
from classes.bitplane.BitPlane64ConjugateBit import Bitplane64ConjugateBit


class SecretData:
    """
    Class representing the secret data to hide.

    Prepares the data on initialization.
    """

    blocks: list[Bitplane64ConjugateBit]  # 8 by 8 bit block.
    conjugateMap : list[int]  # list of the indexes (in bitBlocks) of the blocks that got conjugated.
    number_of_blocks : int
    data_length : int

    def __init__(self, bits: str, complexityThreshold : float):
        """
        Initialization, prepares the data to be stored.

        Separate the data into blocks of 8x8 and for each of them, checks if the complexity is superior to the
        complexity threshold otherwise, conjugates it.
        :param bits: A binary string representing the data to store.
        :param complexityT: Complexity threshold.
        """
        self.data_length = len(bits)
        self.number_of_blocks = (len(bits) // 63) + (0 if len(bits) % 63 == 0 else 1 )

        self.blocks = []

        print("Starting block separation for secret data.")
        for i in range(self.number_of_blocks - 1):
            block = Bitplane64ConjugateBit(int(bits[i*63:(63*i)+63], 2))
            if block.complexity < complexityThreshold:
                self.blocks.append(block.conjugate())
            else:
                self.blocks.append(block)

        rest = len(bits) % 63
        if rest != 0:
            # The last block has not been added yet.
            blank_pixel_to_add = 63-rest
            block = Bitplane64ConjugateBit(int(bits[(self.number_of_blocks - 1) * 63:] + "0"*blank_pixel_to_add, 2))
            if block.complexity < complexityThreshold:
                self.blocks.append(block.conjugate())
            else:
                self.blocks.append(block)

        print("Block separation done.")
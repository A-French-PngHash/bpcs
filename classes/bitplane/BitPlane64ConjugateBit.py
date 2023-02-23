from classes.bitplane.BitPlane64 import Bitplane64

class Bitplane64ConjugateBit(Bitplane64):
    """
    A BitPlane64 but with a bit reserved to say if it is conjugated or not.
    """

    def __init__(self, bitplane: int, conjugated: bool = False):
        """
        Initializes.

        The bottom right bit will be reserved for indicating whether the block was
        conjugated, therefore only 63 bits of data must be passed.

        :param bitplane:
        :param conjugation_bit:
        :param conjugated:
        """
        self.conjugated = conjugated
        super().__init__((bitplane << 1) + (1 if conjugated else 0)) # Shifts the bitplane one to the right to add the conjugate bit.

    @property
    def complexity(self) -> float:
        """
        Bit complexity of this bitplane.

        Warning : Computes the complexity by considering all the bits except the bottom right one.
        Iterates over each bytes and check if the border with it's top and right neighbour is a white-black border.
        :return:
        """

        bwborders = 0  # black/white borders.
        for i in range(63):
            # Notice : range(63). We don't want the last byte to check it's borders at is it the conjugation byte.
            if i < 62:  # Can check next bit.
                # Notice : i < 62. We don't want the second last to check it's border with the last byte as the last
                # one is the conjugation byte.
                if self.bitlist[i] != self.bitlist[i + 1]:
                    bwborders += 1
            if i > 8:
                if self.bitlist[i] != self.bitlist[i - 8]:
                    bwborders += 1
        bwbordermax = 7 * 7 * 2 + 7 + 7  # Chess patern.
        bwbordermax -= 2 # Removing the borders counting the conjugation byte.
        return bwborders / bwbordermax


    def conjugate(self):
        wcheck = int(("10"*4 + "01" * 4)*4, 2)
        conjug = (((self.bitplane) ^ wcheck ) >> 1)
        return Bitplane64ConjugateBit(conjug, conjugated=not self.conjugated)

    def __neg__(self):
        """
        Similar as conjugate.
        :return:
        """
        self.conjugate()
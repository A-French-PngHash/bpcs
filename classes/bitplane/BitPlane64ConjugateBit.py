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

    def conjugate(self):
        wcheck = int(("10"*4 + "01" * 4)*4, 2)
        conjug = (((self.bitplane) ^ wcheck ) >> 1)
        return Bitplane64ConjugateBit(conjug, conjugated=not self.conjugated)

    def __neg__(self):
        """
        Similar as conjugate.
        :return:
        """
        return self.conjugate()
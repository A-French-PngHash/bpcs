from matplotlib import pyplot as plt
from abc import ABC, abstractmethod


class Bitplane64:
    """
    An 8 by 8 block of bit.
    """

    _bitlist : list[str] = None
    bitplane : int

    def __init__(self, bitplane: int):
        """
        Initializes an 8x8 block of bit.

        :param bitplane:
        """
        self.bitplane_length = 64
        if bitplane > 2**(self.bitplane_length):
            raise Exception(f"Bitplane value too big. Must be between 0 and 2^{self.bitplane_length - 1} ({bitplane})")
        self.bitplane = bitplane

    @property
    def bitlist(self) -> list[str]:
        if not self._bitlist:
            self._bitlist = list(f"{self.bitplane:064b}")
        return self._bitlist

    @property
    def complexity(self) -> float:
        """
        Bit complexity of this bitplane.

        Warning : Computes the complexity by considering all the bits except the bottom right one.
        Iterates over each bytes and check if the border with it's top and right neighbour is a white-black border.
        :return:
        """

        bwborders = 0  # black/white borders.
        for i in range(64):
            if i < 63:  # Can check next bit.
                if self.bitlist[i] != self.bitlist[i + 1]:
                    bwborders += 1
            if i > 8:
                if self.bitlist[i] != self.bitlist[i - 8]:
                    bwborders += 1
        bwbordermax = 7 * 7 * 2 + 7 + 7  # Chess patern.
        return bwborders / bwbordermax

    def show(self, show_plt = True):
        """
        Using matplotlib to show a graphical representation of the bitplane.

        :param bitplane: Must be between 0 and 2^64
        :return:
        """
        plt.figure()
        bitlist = list(f"{self.bitplane:064b}")
        imdata = [[[255 * int(bitlist[line * 8 + column])] * 3 for column in range(8)] for line in range(8)]

        plt.imshow(imdata)
        if show_plt : plt.show()

    def conjugate(self):
        wcheck = int(("10" * 4 + "01" * 4) * 4, 2)
        conjug = (self.bitplane) ^ wcheck
        return Bitplane64(conjug)

class BitPlane64ConjugateBit(Bitplane64):
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
        return BitPlane64ConjugateBit(conjug, conjugated=not self.conjugated)


class tempBitplane64Conjugable:
    _bitlist : list[str] = None
    bitplane : int
    conjugated : bool

    def __init__(self, bitplane : int, conjugation_bit = False, conjugated : bool = False):
        """
        Initializes.

        If conjugation_bit is True then the bottom right bit will be reserved for indicating whether the block was
        conjugated, therefore only 63 bits of data must be passed.

        :param bitplane:
        :param conjugation_bit:
        :param conjugated:
        """
        self.bitplane_length = 64
        if bitplane > 2**(self.bitplane_length - 1):
            raise Exception(f"Bitplane value too big. Must be between 0 and 2^{self.bitplane_length - 1} ({bitplane})")

        self.conjugated = conjugated
        self.bitplane = (bitplane << 1) + (1 if conjugated else 0) # Shifts the bitplane one to the right to add the conjugate bit.

    @property
    def bitlist(self) -> list[str]:
        if not self._bitlist:
            self._bitlist = list(f"{self.bitplane:064b}")
        return self._bitlist

    @property
    def complexity(self) -> float:
        """
        Bit complexity of this bitplane.

        Warning : Computes the complexity by considering all the bits except the bottom right one.
        Iterates over each bytes and check if the border with it's top and right neighbour is a white-black border.
        :return:
        """

        bwborders = 0  # black/white borders.
        for i in range(64):
            if i < 63: # Can check next bit.
                if self.bitlist[i] != self.bitlist[i+1]:
                    bwborders += 1
            if i > 8:
                if self.bitlist[i] != self.bitlist[i - 8]:
                    bwborders += 1
        bwbordermax = 7*7*2 + 7 + 7 #  Chess patern.
        return bwborders / bwbordermax

    def show(self, show_plt = True):
        """
        Using matplotlib to show a graphical representation of the bitplane.

        :param bitplane: Must be between 0 and 2^64
        :return:
        """
        plt.figure()
        bitlist = list(f"{self.bitplane:064b}")
        imdata = [[[255 * int(bitlist[line * 8 + column])] * 3 for column in range(8)] for line in range(8)]

        plt.imshow(imdata)
        if show_plt : plt.show()

    def conjugate(self):
        wcheck = int(("10"*4 + "01" * 4)*4, 2)
        conjug = (((self.bitplane) ^ wcheck ) >> 1)
        return Bitplane64(conjug, conjugated=not self.conjugated)


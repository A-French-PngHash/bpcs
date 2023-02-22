import math

from matplotlib import pyplot as plt

from classes.bitplane.bitplane_abstract import Bitplane64

class BitLayer:
    """
    A whole CGS layer of the host image.
    """

    data_bin : str
    side_length : int
    bitplanes : list[Bitplane64]
    writable_blocks_count : int = 0

    def __init__(self, data_bin : str, complexity_threshold : float):
        """
        :param data_bin: The binary data composing this layer. This is a decomposed layer of the whole image so 1
        character of data_bin (1 or 0) is linked to one pixel. The data_bin length must be a multiple of 64 to be able
        to make blocks of 8 by 8 out of it.
        """
        self.data_bin = data_bin
        if len(data_bin) % 64 != 0:
            raise Exception(f"data_bin length must be a multiple of 64 ({len(data_bin)})")
        self.side_length = int(math.sqrt(len(data_bin)))
        self.bitplanes = []

        for bloc_index in range(0, int(len(data_bin) / 64)):
            start_line = 8 * ((bloc_index*8) // self.side_length)
            start_column = ((bloc_index*8) % self.side_length)
            bloc_data = [data_bin[(start_line + line) * self.side_length + start_column: (start_line + line) * self.side_length + start_column + 8] for line in range(8)]

            bitplane = Bitplane64(int("".join(bloc_data), 2))
            if bitplane.complexity > complexity_threshold:
                self.writable_blocks_count += 1

            self.bitplanes.append(bitplane)

    def show_whole_layer(self, show_plt = True):
        """
        Display the whole layer.

        :return:
        """
        plt.figure()
        bitlist = list(self.data_bin)
        imdata = [[[255 * int(bitlist[line * self.side_length + column])] * 3 for column in range(self.side_length)] for line in range(self.side_length)]
        plt.imshow(imdata)
        if show_plt : plt.show()

    def show_bloc(self, index, show_plt = True):
        """
        Show the 8x8 block at the [index] for this layer.

        :param index:
        :return:
        """
        self.bitplanes[index].show(show_plt = show_plt)
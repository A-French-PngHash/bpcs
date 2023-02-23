import math

from matplotlib import pyplot as plt

from classes.bitplane.BitPlane64 import Bitplane64

class BitLayer:
    """
    A whole CGS layer of the host image.
    """

    data_bin : str
    side_length : int
    blocks : list[Bitplane64]
    writable_blocks_count : int = 0

    writable_blocks_map : list[int] # The indexes in the [bitplanes] list of the blocks that can be overwritten.

    def __init__(self, data_bin : str, complexity_threshold : float):
        """
        :param data_bin: The binary data composing this layer. This is a decomposed layer of the whole image so 1
        character of data_bin (1 or 0) is linked to one pixel. The data_bin length must be a multiple of 64 to be able
        to make blocks of 8 by 8 out of it.
        """
        self.writable_blocks_map = []
        self.data_bin = data_bin
        if len(data_bin) % 64 != 0:
            raise Exception(f"data_bin length must be a multiple of 64 ({len(data_bin)})")
        self.side_length = int(math.sqrt(len(data_bin)))
        self.blocks = []

        for bloc_index in range(0, int(len(data_bin) / 64)):
            start_line = 8 * ((bloc_index*8) // self.side_length)
            start_column = ((bloc_index*8) % self.side_length)
            bloc_data = []
            for line in range(8):
                bloc_data.append(data_bin[(start_line + line) * self.side_length + start_column: (start_line + line) * self.side_length + start_column + 8])

            #bloc_data = [data_bin[(start_line + line) * self.side_length + start_column: (start_line + line) * self.side_length + start_column + 8] for line in range(8)]

            bitplane = Bitplane64(int("".join(bloc_data), 2))
            if bitplane.complexity > complexity_threshold:
                self.writable_blocks_count += 1
                self.writable_blocks_map.append(bloc_index)

            self.blocks.append(bitplane)

    @property
    def uptodate_layer_data(self) -> str:

        layer_data = ""
        for line in range(self.side_length):
            for column in range(0, self.side_length, 8):
                block_ind = int((self.side_length / 8) * (line // 8) + column // 8)
                block_line_ind = line % 8
                layer_data += self.blocks[block_ind].bitstring[8 * block_line_ind:8 * block_line_ind + 8]
        return layer_data

    def show_whole_original_layer(self, show_plt = True):
        """
        Display the whole layer.

        :return:
        """
        bitlist = list(self.data_bin)
        self._show(bitlist, show_plt)


    def show_whole_layer(self, show_plt = True):
        self._show(list(self.uptodate_layer_data), show_plt)

    def _show(self, bitlist : list[str], show_plt = True):
        plt.figure()
        imdata = [[[255 * int(bitlist[line * self.side_length + column])] * 3 for column in range(self.side_length)] for
                  line in range(self.side_length)]
        plt.imshow(imdata)
        if show_plt: plt.show()

    def show_bloc(self, index, show_plt = True):
        """
        Show the 8x8 block at the [index] for this layer.

        :param index:
        :return:
        """
        self.blocks[index].show(show_plt = show_plt)
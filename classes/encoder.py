import base64

from classes.bitplane.BitPlane64 import Bitplane64, BitplaneOverflow
from classes.bitplane.BitPlane64ConjugateBit import Bitplane64ConjugateBit
from classes.host_image import HostImage
from classes.secret_data import SecretData


class Encoder:
    """
    Encodes the secret data into the host image.

    Before encoding the data, two blocks are placed, the first one corresponds to the name of the file. The second one
    is the binary length of the data stored in the image.
    """

    block_to_hide : int

    def __init__(self, host_image : HostImage, secret_data : SecretData, file_name : str, complexity_threshold : float):
        """

        :param host_image:
        :param secret_data:
        :param file_name: 10 chars max
        """
        try:
            self.file_name_block = Bitplane64ConjugateBit(int.from_bytes(bytearray(str.encode(file_name)), "big"))
        except BitplaneOverflow:
            print(bin(int.from_bytes(bytearray(str.encode(file_name)), 'big')))
            print(len(bin(int.from_bytes(bytearray(str.encode(file_name)), 'big'))))
            raise Exception("file_name length is too long, cannot store it in one bitplane.")

        self.length_block = Bitplane64ConjugateBit(secret_data.data_length)
        if self.file_name_block.complexity < complexity_threshold:
            self.file_name_block = -self.file_name_block
        if self.length_block.complexity < complexity_threshold:
            self.length_block = -self.length_block


        self.host_image = host_image
        self.secret_data = secret_data

        self.block_to_hide = self.secret_data.number_of_blocks + 2
        if self.host_image.writable_blocks_count < self.secret_data.number_of_blocks + 2:
            raise Exception(f"Not enough storage in the host image, available : {self.host_image.writable_blocks_count}, needed : {self.secret_data.number_of_blocks + 2}")

    def encode(self):
        # TODO : encode first two block
        block_ind = 0
        for layer in reversed(self.host_image.layers[3:]):
            for wblock_ind in layer.writable_blocks_map:
                layer.blocks[wblock_ind] = self.secret_data.blocks[block_ind]
                block_ind += 1
                if block_ind >= self.block_to_hide - 2:
                    break

            if block_ind >= self.block_to_hide - 2:
                break
        return self.host_image
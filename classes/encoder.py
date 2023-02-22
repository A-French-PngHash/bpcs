import base64

from classes.bitplane.bitplane_abstract import Bitplane64
from classes.host_image import HostImage
from classes.secret_data import SecretData


class Encoder:
    """
    Encodes the secret data into the host image.

    Before encoding the data, two blocks are placed, the first one corresponds to the name of the file. The second one
    is the binary length of the data stored in the image.
    """

    def __init__(self, host_image : HostImage, secret_data : SecretData, file_name : str):
        """

        :param host_image:
        :param secret_data:
        :param file_name: 10 chars max
        """
        if len(file_name) > 10:
            raise Exception("File name must be less than 10 characters long.")

        self.file_name_block = Bitplane64(int(base64.b64decode(file_name), 2))
        self.length_block = Bitplane64(secret_data.data_length)


        self.host_image = host_image

        self.secret_data = SecretData

    def encode(self):
        pass
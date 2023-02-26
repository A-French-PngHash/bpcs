from typing import Protocol, Iterator

from classes.bit_layer import BitLayer


class HostImage(Protocol):
    """
    Defines what a class must have to be used as a host for BPCS encoding.
    """

    side_length : int
    writable_blocks_count : int

    def show_image(self) -> None:
        """
        Shows the up to date image using data from the CGC layers.
        :return:
        """

    def show_original_image(self, show_plt : bool) -> None:
        pass

    def writing_layers(self, bellow : int) -> Iterator[BitLayer]:
        """
        Generator that yields layers starting from the bottom stopping at the layer bellow (excluded).
        :param bellow:
        :return:
        """

    def write_image_to(self, filepath : str):
        """
        Writes the image to the disk at the given location.
        :param filepath:
        :return:
        """
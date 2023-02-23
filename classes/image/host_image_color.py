from PIL.Image import Image
from matplotlib import pyplot as plt

from classes.bit_layer import BitLayer
from classes.host_image_bw import HostImageBW


class HostImageColor:
    """
    Represents an image with three distinct color channel (rgb).

    This class is creating three instances of HostImageBW, each with their corresponding color channel.
    """
    host_image_decomposition : [HostImageBW]

    def __init__(self, host_path: str, complexity_threshold: float):
        self.host_image_decomposition = []
        for color in range(3):
            self.host_image_decomposition.append(HostImageBW(host_path, complexity_threshold, color))
        self.side_length = self.host_image_decomposition[0].side_length

    @property
    def writable_blocks_count(self):
        return sum([host.writable_blocks_count for host in self.host_image_decomposition])

    def show_original_image(self, show_plt = True):
        plt.figure()
        imdata = [
            [[int(host.pixel_values[line * host.side_length + column], 2) for host in self.host_image_decomposition] for column in range(self.side_length)]
            for line in range(self.side_length)]
        plt.imshow(imdata)
        if show_plt : plt.show()
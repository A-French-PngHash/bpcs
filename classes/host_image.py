import numpy
from PIL import Image
from classes.bit_layer import BitLayer
import data_loader
from matplotlib import pyplot as plt


class HostImage:
    side_length: int  # Side length of the host image
    layers: list[BitLayer]  # Decomposed CGS layers
    pixel_values: list[str]  # A list of binary values corresponding to the r=g=b value of the pixels.
    writable_blocks_count : int = 0

    def __init__(self, host_path : str, complexity_threshold : float):
        """
        :param host_path: Path to the host image. WARNING : The image must be a square and the side length in pixel must
         be a multiple of 8. It should also be black and white.
        """

        image: Image.Image = Image.open(host_path).convert('RGB')
        self.side_length = image.height
        self.pixel_values = [f"{i[0]:08b}" for i in list(image.getdata())]

        self.layers = []
        for layer in range(8):  # 0 is the top most layer.
            layer_data = "".join([i[layer] for i in self.pixel_values])
            bitlayer = BitLayer(layer_data, complexity_threshold)
            self.writable_blocks_count += bitlayer.writable_blocks_count
            self.layers.append(bitlayer)

    def show_image(self):
        """
        Using matplotlib to show a graphical representation of the host image.
        :return:
        """
        imdata = [
            [[int(self.pixel_values[line * self.side_length + column], 2)] * 3 for column in range(self.side_length)]
            for line in range(self.side_length)]
        plt.imshow(imdata)
        plt.show()

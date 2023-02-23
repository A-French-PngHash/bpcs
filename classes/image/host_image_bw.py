import numpy
from PIL import Image
from classes.bit_layer import BitLayer
import data_loader
from matplotlib import pyplot as plt


class HostImageBW:
    """
    Black and white host image.
    """

    side_length: int  # Side length of the host image which is a square.
    layers: list[BitLayer]  # Decomposed CGS layers
    pixel_values: list[str]  # A list of binary values corresponding to the r=g=b value of the pixels.
    writable_blocks_count: int = 0

    def __init__(self, host_path: str, complexity_threshold: float, color_channel: int):
        """
        :param host_path: Path to the host image. WARNING : The image must be a square and the side length in pixel must
         be a multiple of 8. It should also be black and white.
         :param color_channel: This indicates from which channel should the pixel value be taken. If the image is in
         black and white then
        """

        image: Image.Image = Image.open(host_path).convert('RGB')
        self.side_length = image.height
        self.pixel_values = [f"{i[color_channel]:08b}" for i in list(image.getdata())]

        self.layers = []
        for layer in range(8):  # 0 is the top most layer.
            layer_data = "".join([i[layer] for i in self.pixel_values])
            bitlayer = BitLayer(layer_data, complexity_threshold)
            self.writable_blocks_count += bitlayer.writable_blocks_count
            self.layers.append(bitlayer)
            print(f"Layer {layer} done !")

    def show_original_image(self, show_plt = True):
        """
        Using matplotlib to show a graphical representation of the host image.

        The data is taken from [pixel_values], therefore it is not up to date if the blocks were modified.
        :return:
        """
        plt.figure()
        imdata = [
            [[int(self.pixel_values[line * self.side_length + column], 2)] * 3 for column in range(self.side_length)]
            for line in range(self.side_length)]
        plt.imshow(imdata)
        if show_plt : plt.show()

    @property
    def image_bin_data(self):
        """
        The up to date image data computed from the up to date layers.
        :return:
        """
        layers = [list(layer.uptodate_layer_data) for layer in self.layers]
        """
        Layers look like : 
        
        ['0', '1', '0' ..., '1'],
        ['1', '1', '0' ..., '0'],
        ... (5x)
        ['0', '0', '1' ..., '0']
        
        We want to get something that looks like : 
        ['01...0', '11...0', '00...1' ..., '10...0']
        """

        bin_data = [''] * len(layers[0])
        for layer in layers:
            bin_data = list(map(lambda e: bin_data[e] + layer[e], range(len(bin_data))))
        return bin_data

    def show_image(self):
        bin_data = self.image_bin_data
        imdata = [
            [[int(bin_data[line * self.side_length + column], 2)] * 3 for column in range(self.side_length)]
            for line in range(self.side_length)]

        plt.imshow(imdata)
        plt.show()

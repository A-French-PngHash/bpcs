from matplotlib import pyplot as plt

import data_loader
import small_demos
from classes.bitplane.BitPlane64 import Bitplane64
from classes.encoder import Encoder
from classes.host_image import HostImage
from classes.secret_data import SecretData

complexity_threshold=0.4

secret_data = SecretData(data_loader.load_file_as_binary("TestImage/shakespeares_345kb.zip"), complexityThreshold=complexity_threshold)
host = HostImage("TestImage/weed1000.png", complexity_threshold=complexity_threshold)
host.layers[4].show_whole_original_layer(show_plt=False)
encoder = Encoder(host_image=host, secret_data=secret_data, complexity_threshold=complexity_threshold, file_name="hell.txt")
host = encoder.encode()

host.show_image()
host.layers[4].show_whole_layer()

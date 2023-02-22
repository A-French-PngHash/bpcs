from matplotlib import pyplot as plt

import data_loader
import small_demos
from classes.bitplane import Bitplane64
from classes.host_image import HostImage
from classes.secret_data import SecretData

"""
host = HostImage("TestImage/girl256.png")
host.layers[5].show_whole_layer(show_plt=False)
for i in range(1):
    host.layers[5].show_bloc(i, show_plt=False)
plt.show()
"""

#host.show_layer(list(range(8)))

#small_demos.girl256showlayernandsomeblocks(5)
print(len(data_loader.load_file_as_binary("TestImage/hello.txt")))
print(len(data_loader.load_file_as_binary("TestImage/shakespeares.zip")))
#secret = SecretData(data_loader.load_file_as_binary("TestImage/hello.txt"), complexityThreshold=0.4)

host = HostImage("TestImage/girl256.png", complexity_threshold=0.4)
print(host.writable_blocks_count)

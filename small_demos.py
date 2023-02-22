from matplotlib import pyplot as plt

from bitplane_Gen import generate8by8bitplane
from classes.bitplane import Bitplane64
from classes.host_image import HostImage


def girl256showlayernandsomeblocks(n : int):
    host = HostImage("TestImage/girl256.png")
    host.layers[n].show_whole_layer(show_plt=False)
    #for i in range(0):
        #host.layers[n].show_bloc(i, show_plt=False)
    plt.show()

def random_bitplane_and_conjugation():
    num = generate8by8bitplane()
    print(num)
    bitplane = Bitplane64(num)
    bitplane.show(show_plt=False)
    bitplane.conjugate().show()

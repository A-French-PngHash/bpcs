from matplotlib import pyplot as plt

import data_loader
from misc.bitplane_Gen import generate8by8bitplane
from classes.bitplane.BitPlane64 import Bitplane64
from classes.decoder import Decoder
from classes.encoder import Encoder
from classes.image.host_image_bw import HostImageBW
from classes.image.host_image_color import HostImageColor
from classes.secret_data import SecretData


def girl256showlayernandsomeblocks(n : int):
    host = HostImageBW("../TestImage/girl256bw.png", complexity_threshold=0.4)
    print(host.writable_blocks_count)
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




def hide_part_of_shakespear_in_weed_and_show_layer_change():
    complexity_threshold = 0.4
    secret_data = SecretData(data_loader.load_file_as_binary("../TestImage/shakespeares_345kb.zip"),
                             complexityThreshold=complexity_threshold)
    host = HostImageColor("../TestImage/weed1000.png", complexity_threshold=complexity_threshold)
    encoder = Encoder(host_image=host, secret_data=secret_data, complexity_threshold=complexity_threshold,
                      file_name="hell.txt")
    host = encoder.encode()
    host.show_image()

    host.layers[4].show_whole_original_layer(show_plt=False)
    host.layers[4].show_whole_layer()

def hide_hello_file_in_girl_color_and_save_image():
    secret = SecretData(data_loader.load_file_as_binary('../TestImage/hello.txt'), complexityThreshold=0.4)
    host = HostImageColor(host_path='../TestImage/girl128color.png', complexity_threshold=0.4)
    encoder = Encoder(host_image=host, complexity_threshold=0.4, secret_data=secret, file_name='shake')
    new_host = encoder.encode()
    new_host.write_image_to("aoutput/secret.png")


def hide_girl_in_girl_and_decode():
    secret = SecretData(data_loader.load_file_as_binary('../TestImage/girl64bw.png'), complexityThreshold=0.4)
    host = HostImageColor(host_path='../TestImage/girl128color.png', complexity_threshold=0.4)
    encoder = Encoder(host_image=host, complexity_threshold=0.4, secret_data=secret, file_name='a.png')
    new_host = encoder.encode()
    new_host.write_image_to("aoutput/secret.png")

    decoder = Decoder('../aoutput/secret.png', complexity_threshold=0.4, black_white=False)
    decoder.decode()
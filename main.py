from classes.bitplane.BitPlane64 import Bitplane64
from classes.decoder import Decoder
from classes.encoder import Encoder
from classes.image.host_image_bw import HostImageBW
from classes.image.host_image_color import HostImageColor
from classes.image.image_protocol import HostImage
from classes.secret_data import SecretData
from misc import data_loader
"""
secret = SecretData(bits=data_loader.load_file_as_binary('TestImage/girl128color.png'), complexityThreshold=0.4)

encoder = Encoder(host_image=host, secret_data=secret, complexity_threshold=0.4, file_name='hello2.png')
encoder.encode()
host.write_image_to('out.png')
"""
host = HostImageColor("TestImage/girl512color.png", complexity_threshold=0.4)

Decoder('out.png', 0.4, black_white=False).decode()
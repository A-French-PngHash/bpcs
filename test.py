from classes.decoder import Decoder
from classes.encoder import Encoder
from classes.image.host_image_color import HostImageColor
from classes.secret_data import SecretData
from misc import data_loader
print(bin(4))

secret = SecretData(data_loader.load_file_as_binary('TestImage/girl128bw.png'), complexityThreshold=0.3)
host = HostImageColor(host_path='TestImage/girl512color.png', complexity_threshold=0.3)
encoder = Encoder(host_image=host, complexity_threshold=0.3, secret_data=secret, file_name='a.png')
new_host = encoder.encode()
new_host.write_image_to("TestImage/hidden/test.png")


decoder = Decoder('TestImage/hidden/test.png', complexity_threshold=0.3, black_white=False)
decoder.decode()

# first encoded : '100010010101000001001110010001110000110100001010000110100000101'
# first out     : ''
"""
                                    

in :  1111001011011110110111101101111011011110010000001100011011000010010000001110110011000010010000001101111011101010010000001110001011101010110111101101001
out : 1111001011011110110111101101111011011110010000001100011011000011010011111110101100000000000011100010000011101011111110000110100011000110010101010001101
"""
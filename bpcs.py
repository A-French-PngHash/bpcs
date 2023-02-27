"""
Example

secret = SecretData(data_loader.load_file_as_binary('TestImage/girl128bw.png'), complexityThreshold=0.3)
host = HostImageColor(host_path='TestImage/girl512color.png', complexity_threshold=0.3)
encoder = Encoder(host_image=host, complexity_threshold=0.3, secret_data=secret, file_name='a.png')
new_host = encoder.encode()
new_host.write_image_to("TestImage/hidden/test.png")


decoder = Decoder('TestImage/hidden/test.png', complexity_threshold=0.3, black_white=False)
decoder.decode()
"""
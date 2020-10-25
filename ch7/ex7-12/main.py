import binascii
import struct

gif_hex = "47494638396101000100800000000000ffffff21f9" + \
    "0401000000002c000000000100010000020144003b"

gif = binascii.unhexlify(gif_hex)

print(gif)

head = struct.unpack('>6s', gif[0:6])
print(head)
print(head == (b'GIF89a',))

print(gif[0:6] == b'GIF89a')

wh = struct.unpack('<2H', gif[6:10])
print(wh)
print(wh == (1, 1))

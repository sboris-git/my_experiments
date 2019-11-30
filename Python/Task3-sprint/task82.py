import zlib
import bz2


def compress(text):
    '''Question 82
    Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".'''

    # comp_zlib = zlib.compress(text)
    # print("Compressed: ", comp_zlib)
    text = str.encode(text)
    comp_bz = bz2.compress(text)
    # print("Compressed: ", comp_bz)

    return comp_bz


def decompress(comp):
    # decomp_zlib = zlib.decompress(comp)
    # print("Decompressed: ", decomp_zlib)
    decomp_bz = bz2.decompress(comp)
    # print( "Decompressed: ", decomp_bz )
    decode_utf = decomp_bz.decode('utf-8')
    return decode_utf


text = "hello world!hello world!hello world!hello world!"
print(text)
comp = compress(text)
print(decompress(comp))
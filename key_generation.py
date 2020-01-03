#Module to generate a key. Currently, implementation is exceedingly simplistic,
#but open to extension.
def generate_key_SIMPLE():
    key = ''
    bit_counter = 0
    while bit_counter < 64:
        if (bit_counter % 2) == 0:
            key += '1'
        else:
            key += '0'
        bit_counter += 1
    
    return key

#Returns a known weak key of DES.
def generate_key_WEAK():
    key = '1111111011111110111111101111111011111110111111101111111011111110'

    return key
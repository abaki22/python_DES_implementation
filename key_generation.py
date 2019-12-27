#Module to generate a key. Currently, implementation is exceedingly simplistic,
#but open to extension.
def generate_key_SIMPLE():
    key = ''
    #Generate key and parity bits. Parity bits must be appended at the end of 
    #every 'byte'. bit_counter starts at 1 instead of 0 so 0th pos is not a 
    #1
    bit_counter = 1
    while len(key) < 64:
        if (bit_counter % 8) == 0:
            key += '0'
        else: 
            if (bit_counter % 2) == 0:
                key += '0'
            else:
                key += '1'
        bit_counter += 1
        
    return key
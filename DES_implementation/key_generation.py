#Module to generate a key. Currently, implementation is exceedingly simplistic,
#but open to extension.
def generate_key():
    key = ''
    #Generate key
    while len(key) < 56:
        key += '0'
    
    #Generate parity bits
    while len(key) < 64: 
        key += "1"

    return key
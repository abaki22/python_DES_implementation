#Takes a UTF-8 character and turns it into binary. Returns result as a string
def convert_to_binary(char):
    binary_rep_of_char = ""
    utf8_bytes_char = char.encode('utf-8')

    for byte in utf8_bytes_char:
        binary_byte = '{0:08b}'.format(byte)
        binary_rep_of_char += binary_byte

    return binary_rep_of_char
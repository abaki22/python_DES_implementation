#Takes a string of binary bits and returns a list of the characters that string corresponds
#to. 
def convert_to_chars(binary):
    #Turn the input string of binary bits into the corresponding number
    binary_representation = int(binary, 2)


    #Turns the number into bytes using standard int.to_bytes method.
    binary_representation = int(binary_representation).to_bytes(len(binary) // 8, byteorder='big')

    #Decodes the bytes into utf-8
    string = binary_representation.decode('utf-8')

    #Splits string into characters
    chars = []
    for char in string:
        chars.append(char)

    return chars
#Executes a round of DES. 
def perform_round(block, key, data_suite, round_number):
    bit_pointer = 0
    #First, split block into left and right halves.
    left_half = []
    right_half = []
    while bit_pointer <= 31:
        left_half.append(block[bit_pointer])
        bit_pointer += 1

    while bit_pointer <= 63:
        right_half.append(block[bit_pointer])
        bit_pointer += 1

    #Second, apply left shift(s) on key halves, then recombine them
    #and put them through permuted_choice_2

    left_shift_number = data_suite.bit_rotation_table[round_number]
    left_binary_string = parse_binary_string(key[0])
    right_binary_string = parse_binary_string(key[1])

    left_binary_string = rotate_binary_string_bits_left(left_binary_string,\
                                                        left_shift_number)
    right_binary_string = rotate_binary_string_bits_left(right_binary_string,\
                                                        left_shift_number)

    next_rounds_left_key = parse_binary_char_list(left_binary_string)
    next_rounds_right_key = parse_binary_char_list(right_binary_string)
    next_rounds_key = (next_rounds_left_key, next_rounds_right_key)

    recombined_key = left_binary_string + right_binary_string

    permuted_key = []
    bit_pointer = 0
    new_index = 0
    while bit_pointer < 48:
        new_index = data_suite.permuted_choice_2[bit_pointer] - 1
        permuted_key.append(recombined_key[new_index])
        bit_pointer += 1

    #permuted_key should now be loaded and ready to put into the round function. 
    #next_rounds_key can be passed directly to the end of the function

    #Third, begin round function. #TODO
    # i) Apply expansion permutation (E table)
    # ii) XOR with round key
    # iii) Sub boxes (S-boxes)
    # iv) Permutation (P)

    return block, next_rounds_key

#Utility function to parse a binary string from a provided binary char list
def parse_binary_string(binary_char_list):
    binary_string = ""
    for char in binary_char_list:
        binary_string += char
    return binary_string

#Utility function to break a binary string up into a char list (for the return)
def parse_binary_char_list(binary_string):
    binary_char_list = []
    for char in binary_string:
        binary_char_list.append(char)
    return binary_char_list

#Utility function to 'rotate' a string by n. Rotates to the right, so to get 
#a left circular shift you have to use minus numbers. 
def rotate_binary_string_bits_left(binary_string, shift):
    return binary_string[shift:] + binary_string[:shift]
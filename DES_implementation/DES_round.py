#Executes a round of DES. 
def perform_round(block, key, data_suite, round_number):
    bit_pointer = 0
    #First, split block into left and right halves.
    output_block = ""
    left_half = []
    right_half = []
    while bit_pointer < 32:
        left_half.append(block[bit_pointer])
        bit_pointer += 1

    while bit_pointer < 64:
        right_half.append(block[bit_pointer])
        bit_pointer += 1

    #Left half of output is the right half of the input
    output_block += parse_binary_string(right_half)

    next_rounds_key, permuted_key = generate_round_key(key, data_suite, round_number)

    #permuted_key should now be loaded and ready to put into the round function. 
    #next_rounds_key can be passed directly to the end of the function

    #Third, begin round function. #TODO
    # i) Apply expansion permutation (E table)
    expanded_right = expansion_permutation_E(right_half, data_suite)
    # ii) XOR with round key
    xor_result = xor_binary(expanded_right, permuted_key)
    # iii) Sub boxes (S-boxes)
    sub_boxes_result = sub_boxes_transformation(xor_result, data_suite)
    # iv) Permutation (P)
    p_permutation_result = permutation_P(sub_boxes_result, data_suite)

    #XOR output of round function with left half
    final_right_half = xor_binary(p_permutation_result, left_half)

    output_block += parse_binary_string(final_right_half)

    return output_block, next_rounds_key

#Applies permutation_P to the input and returns it.
#Expects a 32 length list/string as an input as well as the data suite. 
def permutation_P(input_p, data_suite):
    permuted_block = []
    bit_pointer = 0
    while bit_pointer < 32:
        permuted_block.append(50)
        bit_pointer += 1

    bit_pointer = 0
    for new_index in data_suite.permutation_p:
        #Reference files for the initial_permutation index from 1-64, but I 
        #need to index from 0-63, so take away 1 from the new_index
        permuted_block[bit_pointer] = input_p[new_index - 1]
        bit_pointer += 1

    return permuted_block

#Takes a 48 bit input and passes it through the sub boxes, return a 32 bit input.
#Expects a binary char list and the data suite as the input
def sub_boxes_transformation(input, data_suite):
    #Prepare inputs
    s_box_inputs = []
    current_input_line = []
    bit_counter = 0
    six_bit_clock = 0
    while bit_counter < 48:
        if(six_bit_clock == 6):
            s_box_inputs.append(current_input_line)
            current_input_line = []
            current_input_line.append(input[bit_counter])
            six_bit_clock = 1
            bit_counter += 1
        else:
            current_input_line.append(input[bit_counter])
            six_bit_clock += 1
            bit_counter += 1    
    s_box_inputs.append(current_input_line)

    s_box_row_col_key = []

    #Translate char bit lists into row/col keys for the s-boxes
    for input_line in s_box_inputs:
        outer_bit_string = input_line[0] + input_line[5]
        inner_bit_string = input_line[1] + input_line[2]\
                         + input_line[3] + input_line[4]
        row_key= int(outer_bit_string, 2)
        col_key = int(inner_bit_string, 2)
        s_box_row_col_key.append([row_key, col_key])

    #Apply s_box transformation
    output_lines = []
    s_boxes = data_suite.s_boxes
    s_box_number = 0
    for box in s_boxes:
        row = s_box_row_col_key[s_box_number][0]
        col = s_box_row_col_key[s_box_number][1]
        substitution = box[row][col]
        output = '{0:04b}'.format(substitution)
        output_lines.append(output)
        s_box_number += 1

    final_output = ""
    for output in output_lines:
        final_output += output

    return final_output

#XORs two binary strings or binary char lists (that are the same length) together
def xor_binary(string_a, string_b):
    result = []
    bit_pointer = 0
    loop_length = len(string_a)

    if len(string_a) != len(string_b):
        raise Exception('XOR_failed: Input strings of unequal length')

    while bit_pointer < loop_length:
        if (string_a[bit_pointer] == '1') & (string_b[bit_pointer] == '1'):
            result.append('0')
        elif (string_a[bit_pointer] == '0') & (string_b[bit_pointer] == '0'):
            result.append('0')
        else: 
            result.append('1')
        bit_pointer += 1
    
    return result

#Applies expansion_permutation_E to a supplied binary char list
def expansion_permutation_E(right_half, data_suite):
    permuted_block = []
    bit_pointer = 0
    while bit_pointer < 48:
        permuted_block.append(50)
        bit_pointer += 1

    bit_pointer = 0
    for new_index in data_suite.expansion_permutation:
        #Reference files for the initial_permutation index from 1-64, but I 
        #need to index from 0-63, so take away 1 from the new_index
        permuted_block[bit_pointer] = right_half[new_index - 1]
        bit_pointer += 1

    return permuted_block
    

#Utility function to generate round-key as well as generate next key. 
def generate_round_key(key, data_suite, round_number):
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
    
    return (next_rounds_key, permuted_key)


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
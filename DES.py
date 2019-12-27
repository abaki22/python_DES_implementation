# Module to implement DES. 
# encryption(key, blocks) - Takes a 64 bit binary string key and a list of 64
# bit blocks that are string represenations of binary blocks and returns a list
# of blocks of equal length that have been encrypted with DES and the supplied
# key.
#
# decryption(key, blocks) - Not yet implemented

import file_parser
import DES_round

#Note to self: This should probably be a dictionary, not a class. 
class DES_Data_Suite:

    initial_permutation = ""
    final_permutation = ""
    permuted_choice_1_left = ""
    permuted_choice_1_right = ""
    permuted_choice_2 = ""
    bit_rotation_table = ""
    
    def __init__(self):
        self.initial_permutation = \
        file_parser.parse_DES_Data('./DES_library/initial_permutation.txt')
        self.final_permutation = \
        file_parser.parse_DES_Data('./DES_library/final_permutation.txt')
        self.permuted_choice_1_left = \
        file_parser.parse_DES_Data('./DES_library/permuted_choice_1_left.txt')
        self.permuted_choice_1_right = \
        file_parser.parse_DES_Data('./DES_library/permuted_choice_1_right.txt')
        self.bit_rotation_table = \
        file_parser.parse_DES_Data('./DES_library/bit_rotation_table.txt')
        self.permuted_choice_2 = \
        file_parser.parse_DES_Data('./DES_library/permuted_choice_2.txt')



def encrypt(key, blocks):
    data_suite = DES_Data_Suite()

    encrypted_blocks = []

    permuted_key_left, permuted_key_right = apply_permuted_choice_1(key, data_suite)
    permuted_key = (permuted_key_left, permuted_key_right)

    for block in blocks:
        encrypted_blocks.append(encrypt_block(permuted_key, block, data_suite))

    return encrypted_blocks




def encrypt_block(key, block, data_suite):
    #Step 1: Apply initial permutation on block

    permuted_block = []
    #Initialise permuted_block size to be the size of the initial block. Not 
    #very python like, but quick and easy. 
    for char in block:
        permuted_block.append(50) 
    #If there are any '50's left in the block after encryption, something went
    #wrong. 

    #Bit pointer points to the bit currently being processed in the block.
    bit_pointer = 0

    for new_index in data_suite.initial_permutation:
        #Reference files for the initial_permutation index from 1-64, but I 
        #need to index from 0-63, so take away 1 from the new_index
        permuted_block[new_index - 1] = block[bit_pointer]
        bit_pointer += 1
    

    #Step 2 - 16 rounds

    round_number = 0
    current_block = permuted_block
    current_key = key
    while round_number < 16:
        current_block, current_key = DES_round.perform_round(current_block,\
                                     current_key, data_suite, round_number)
        round_number += 1

    #Penultimate step - 32 bit swap





    #Final step: Apply final permutation on block and return. 
    final_permuted_block = []
    for char in block:
        final_permuted_block.append(50)

    bit_pointer = 0
    for new_index in data_suite.final_permutation:
        #Use same trick as the initial_permutation: take 1 from the new_index
        final_permuted_block[new_index - 1] = permuted_block[bit_pointer]
        bit_pointer += 1

    #Format final result as a single string, and then return
    final_result = ""
    for digit in final_permuted_block:
        final_result += digit

    return final_result

#Function to generate left and right sides of key after permuted choice 1. 
#Takes a 64 bit key and the data suite and returns left and right of key after
#PC1
def apply_permuted_choice_1(key, data_suite):
    permuted_key_left = []
    permuted_key_right = []
    bit_pointer = 0
    while bit_pointer < 28:
        permuted_key_left.append(50)
        permuted_key_right.append(50)
        bit_pointer += 1

    bit_pointer = 0
    for new_index in data_suite.permuted_choice_1_left:
        permuted_key_left[bit_pointer] = key[new_index - 1]
        bit_pointer += 1

    bit_pointer = 0
    for new_index in data_suite.permuted_choice_1_right:
        permuted_key_right[bit_pointer] = key[new_index - 1]
        bit_pointer += 1
    
    return (permuted_key_left, permuted_key_right)
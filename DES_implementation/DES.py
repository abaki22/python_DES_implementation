# Module to implement DES. 
# encryption(key, blocks) - Takes a 64 bit binary string key and a list of 64
# bit blocks that are string represenations of binary blocks and returns a list
# of blocks of equal length that have been encrypted with DES and the supplied
# key.
#
# decryption(key, blocks) - Not yet implemented

import file_parser

#Note to self: This should probably be a dictionary, not a class. 
class DES_Data_Suite:

    initial_permutation = ""
    final_permutation = ""
    
    def __init__(self):
        self.initial_permutation = \
        file_parser.parse_DES_Data('./DES_library/initial_permutation.txt')
        self.final_permutation = \
        file_parser.parse_DES_Data('./DES_library/final_permutation.txt')



def encrypt(key, blocks):
    data_suite = DES_Data_Suite()

    encrypted_blocks = []

    for block in blocks:
        encrypted_blocks.append(encrypt_block(key, block, data_suite))

    return encrypted_blocks




def encrypt_block(key, block, data_suite):
    #Step 1: Apply initial permutation on block and permuted choice 1 on key

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

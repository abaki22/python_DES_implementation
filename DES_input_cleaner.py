import char_to_binary

#Takes in a list of chars and returns a list of 64 bit binary blocks with the
#final block padded with 0s. Also returns length of padding in bytes. 
def clean_input(list_of_chars):
    DES_input_blocks = []
    full_input = ""

    #First, combine all binary of characters into a large text.
    for char in list_of_chars:
        full_input += char_to_binary.convert_to_binary(char)

    #Then, split the input into 64 bit blocks and put them into DES_input_blocks
    #for conveniance
    input_total_length = len(full_input)
    bit_pointer = 0
    block_pointer = 0
    current_block = ""
    while bit_pointer < input_total_length:
        if block_pointer < 64:
            current_block += full_input[bit_pointer]
            block_pointer += 1
            bit_pointer += 1
        else: 
            block_pointer = 0
            DES_input_blocks.append(current_block)
            current_block = ""
    
    DES_input_blocks.append(current_block)

    #Pad the last block with 0s
    last_block_index = len(DES_input_blocks) - 1
    padding_length = 0
    while len(DES_input_blocks[last_block_index]) < 64:
        DES_input_blocks[last_block_index] += "0"
        padding_length += 1

    #Convert padding_length from length in bits to length in bytes
    padding_length = int(padding_length/8)

    return (DES_input_blocks, padding_length)



    
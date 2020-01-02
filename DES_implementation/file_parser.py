#Module for parsing files into character arrays
def parse(file_name):
    character_array = []
    file_to_parse = open(file_name)
    text_from_file = file_to_parse.read()

    for char in text_from_file:
        character_array.append(char)

    file_to_parse.close()

    return character_array

#Method to purpose-read the DES data files, which are split by /t and /n.
#Also, need to return list of ints and not chars as well as throw away the 
#seperators. 
#TODO - Write test
def parse_DES_Data(file_name):
    file_to_parse = open(file_name)
    text_from_file = file_to_parse.read()

    int_array = text_from_file.split()
    for index, intgr in enumerate(int_array):
        int_array[index] = int(intgr)

    file_to_parse.close()
    return int_array

#Creates the 3D s_boxes list. Reads the 8 s-box files and constructs the 3D
#list. Example of s_boxes usage: s_boxes[3][2][1] refers to the third 
#s-box, 2nd line and 1st character. 
def construct_s_boxes():
    s_boxes = []
    #While the list starts at index 0, indexes 1 to 8 must be sent to parse_DES-
    #sbox, as the files are indexed 1-8. 
    s_box_number = 1
    while s_box_number <= 8:
        s_boxes.append(parse_DES_sbox(s_box_number))
        s_box_number += 1
    return s_boxes


#Parses a 2D list from the specified s-box file. 
def parse_DES_sbox(s_box_number):
    file_name = './DES_library/s-box_' + str(s_box_number) + '.txt'
    file_to_parse = open(file_name)
    text_from_file = file_to_parse.read()

    int_array = text_from_file.split()
    for index, intgr in enumerate(int_array):
        int_array[index] = int(intgr)
    
    file_to_parse.close()

    s_box = []

    row_pointer = 0
    file_intgr_pointer = 0
    while row_pointer < 4:
        col_pointer = 0
        row = []
        while col_pointer < 16:
            row.append(int_array[file_intgr_pointer])
            file_intgr_pointer += 1
            col_pointer += 1
        row_pointer += 1
        s_box.append(row)

    return s_box

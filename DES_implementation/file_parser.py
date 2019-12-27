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

    return int_array

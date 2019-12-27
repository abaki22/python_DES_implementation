#Module for parsing files into character arrays
def parse(file_name):
    character_array = []
    file_to_parse = open(file_name)
    text_from_file = file_to_parse.read()

    for char in text_from_file:
        character_array.append(char)

    file_to_parse.close()

    return character_array



import sys
import file_parser
import DES_input_cleaner
import binary_to_chars
import key_generation
import DES

##### Command line inputs ####
mode = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

###### Format Input #####
input_file_contents = file_parser.parse(input_file)

DES_input_blocks, padding_length = DES_input_cleaner.clean_input(input_file_contents)

##### DES #####

key = key_generation.generate_key_SIMPLE()

DES_output_blocks = DES.encrypt(key, DES_input_blocks)

final_DES_output = ""
for block in DES_output_blocks:
    final_DES_output += block



##### Format Output #####



#binary_string = binary_to_chars.convert_to_chars(final_DES_output)
#final_output = ""
#for char in binary_string:
#    final_output += char
final_output = final_DES_output


output_file = open(output_file, "w")
output_file.write(final_output)
output_file.close()